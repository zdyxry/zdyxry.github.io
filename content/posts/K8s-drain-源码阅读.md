---
title: K8s drain 命令源码阅读
date: 2020-02-15 11:22:13
tags:
- Kubernetes
---


## 背景

之前写过一篇 [《Kubernetes 实战-平滑移除节点》](https://zdyxry.github.io/2019/08/01/Kubernetes-%E5%AE%9E%E6%88%98-%E5%B9%B3%E6%BB%91%E7%A7%BB%E9%99%A4%E8%8A%82%E7%82%B9/) 讲如何从 K8s 集群中移除节点的，今天来看看 `kubectl drain` 命令具体做了什么，怎么实现的。


## kubectl

`drain` 相关命令都属于 `kubectl` 的自命令，因此需要先看下 `kubectl` 的入口，K8s 使用 cobra 作为命令行构建组建（我自己使用 cobra 觉得不怎么好用，而且文档也不清晰。。），统一入口在 `cmd/kubectl/kubectl.go` ，实际的处理逻辑在 `pkg/kubectl/cmd/cmd.go` 中

```go
    ...
	groups := templates.CommandGroups{
		{
			Message: "Basic Commands (Beginner):",
			...
		},
		{
			Message: "Deploy Commands:",
			...
		},
		{
			Message: "Cluster Management Commands:",
			Commands: []*cobra.Command{
				certificates.NewCmdCertificate(f, ioStreams),
				clusterinfo.NewCmdClusterInfo(f, ioStreams),
				top.NewCmdTop(f, ioStreams),
				drain.NewCmdCordon(f, ioStreams),
				drain.NewCmdUncordon(f, ioStreams),
				drain.NewCmdDrain(f, ioStreams),
				taint.NewCmdTaint(f, ioStreams),
			},
		},
    ...
	}
    groups.Add(cmds)
```

可以看到在 `kubectl` 所有子命令的入口，我们今天要看的 `drain` 命令都属于集群管理命令，包含了：
* cordon
* uncordon
* drain

## Cordon

先来看看 `cordon` 命令，这条命令的用途是标记节点为不可调度状态，防止在进行节点维护时 K8s 仍调度资源到该节点上。

```go
func NewCmdCordon(f cmdutil.Factory, ioStreams genericclioptions.IOStreams) *cobra.Command {
	o := NewDrainCmdOptions(f, ioStreams)

	cmd := &cobra.Command{
		Use:                   "cordon NODE",
		DisableFlagsInUseLine: true,
		Short:                 i18n.T("Mark node as unschedulable"),
		Long:                  cordonLong,
		Example:               cordonExample,
		Run: func(cmd *cobra.Command, args []string) {
			cmdutil.CheckErr(o.Complete(f, cmd, args))
			cmdutil.CheckErr(o.RunCordonOrUncordon(true))
		},
	}
	cmd.Flags().StringVarP(&o.drainer.Selector, "selector", "l", o.drainer.Selector, "Selector (label query) to filter on")
	cmdutil.AddDryRunFlag(cmd)
	return cmd
}
```

直接看 `Run` 中的内容，先忽略 `cmdutil.CheckErr` ，这里主要执行了两个方法：`o.Complete` 和 `o.RunCordonOrUncordon` 。这里就必须提一下 `kubectl` 的实现方式，`kubectl` 的根本目的是发送对应的 HTTP 请求到 APIServer，`kubectl` 通过 `Builder` 和 `Visitor` 来实现了一层封装，使每个子命令的实现方式统一、简洁。

```go
// Builder provides convenience functions for taking arguments and parameters
// from the command line and converting them to a list of resources to iterate
// over using the Visitor interface.
type Builder struct {
    ...
}
// Visitor lets clients walk a list of resources.
type Visitor interface {
	Visit(VisitorFunc) error
}
```

在 `o.Complete` 中构建了对应的 `builder`:

```go
...
    // 根据命令行参数构建 builder 实例
	builder := f.NewBuilder().
		WithScheme(scheme.Scheme, scheme.Scheme.PrioritizedVersionsAllGroups()...).
		NamespaceParam(o.Namespace).DefaultNamespace().
		ResourceNames("nodes", args...).
		SingleResourceType().
		Flatten()

	if len(o.drainer.Selector) > 0 {
		builder = builder.LabelSelectorParam(o.drainer.Selector).
			ResourceTypes("nodes")
	}
    // builder.Do 返回带有 Visitor 的 Result 对象
    r := builder.Do()
```

来看看 `builder.Do()` 接下来是怎么做的来返回了 Result 类型资源：

```go
func (b *Builder) Do() *Result {
    // 调用 visitorResult 返回 Result 类型
	r := b.visitorResult()
    ...
	return r
}
...
func (b *Builder) visitorResult() *Result {
    ...
	// 跳过其他步骤，直接看最简单的通过 Name 来获取 Result
	if len(b.names) != 0 {
		return b.visitByName()
    }
    ...
}
...
func (b *Builder) visitByName() *Result {
    // 声明 Result 对象
	result := &Result{
		singleItemImplied:  len(b.names) == 1,
		targetsSingleItems: true,
    }
    ...
    // 获取 K8s client
	client, err := b.getClient(mapping.GroupVersionKind.GroupVersion())
	...
	visitors := []Visitor{}
	for _, name := range b.names {
		info := &Info{
			Client:    client,
			Mapping:   mapping,
			Namespace: selectorNamespace,
			Name:      name,
			Export:    b.export,
		}
		visitors = append(visitors, info)
    }
    // VisitorList 也实现了 Visit 接口，遍历执行 Visitor 的 Visit 方法
	result.visitor = VisitorList(visitors)
	result.sources = visitors
	return result
}
```

看到了如何获取 Result 类型对象，我们再来看 `o.Complete` 如何处理的，传入一个 VisitorFunc，Result 的 visitor 都实现了 `Visit` 接口，`Visit` 接口的作用是接收 `VisitorFunc` 并执行。 ：

```go
return r.Visit(func(info *resource.Info, err error) error {
		...
    })
...
func (v DecoratedVisitor) Visit(fn VisitorFunc) error {
	return v.visitor.Visit(func(info *Info, err error) error {
        ...
		for i := range v.decorators {
			if err := v.decorators[i](info, nil); err != nil {
				return err
			}
		}
		return fn(info, nil)
	})
}
```

接下来看看 `o.RunCordonOrUncordon` 做了什么：

```go
func (o *DrainCmdOptions) RunCordonOrUncordon(desired bool) error {
	cordonOrUncordon := "cordon"
	if !desired {
		cordonOrUncordon = "un" + cordonOrUncordon
	}
    // 通过 Visit 获取到的 nodeInfos 列表
	for _, nodeInfo := range o.nodeInfos {
        ...
		gvk := nodeInfo.ResourceMapping().GroupVersionKind
		if gvk.Kind == "Node" {
			c, err := drain.NewCordonHelperFromRuntimeObject(nodeInfo.Object, scheme.Scheme, gvk)
			if updateRequired := c.UpdateIfRequired(desired); !updateRequired {
				...
			} else {
				if o.drainer.DryRunStrategy != cmdutil.DryRunClient {
                    ...
                    // 修改对应节点的配置
					err, patchErr := c.PatchOrReplace(o.drainer.Client, o.drainer.DryRunStrategy == cmdutil.DryRunServer)
					...
				}
			}
        }
        ...
	}
	return nil
}
...
func (c *CordonHelper) PatchOrReplace(clientset kubernetes.Interface, serverDryRun bool) (error, error) {
	client := clientset.CoreV1().Nodes()
    oldData, err := json.Marshal(c.node)
    // 更新 node Spec 的 Unschedulable 字段
	c.node.Spec.Unschedulable = c.desired
	newData, err := json.Marshal(c.node)
    // merge 数据，通过 diff 然后获取
	patchBytes, patchErr := strategicpatch.CreateTwoWayMergePatch(oldData, newData, c.node)
	if patchErr == nil {
		...
		_, err = client.Patch(context.TODO(), c.node.Name, types.StrategicMergePatchType, patchBytes, patchOptions)
	} 
	...
}
```

## Drain

看完了 Cordon，再来看 Drain：

```go
func NewCmdDrain(f cmdutil.Factory, ioStreams genericclioptions.IOStreams) *cobra.Command {
    ...
	cmd := &cobra.Command{
		...
		Run: func(cmd *cobra.Command, args []string) {
			cmdutil.CheckErr(o.Complete(f, cmd, args))
			cmdutil.CheckErr(o.RunDrain())
		},
    }
    ...
```

直接看 `o.RunDrain`，我们会看到第一件事情就就是执行 `o.RunCordonOrUncordon` ，就是标记节点为不可调度，所以我之前写的那篇博客其实说法不正确，如果是想将节点下线，那么直接执行 `kubectl drain` 就好：

```go
func (o *DrainCmdOptions) RunDrain() error {
    if err := o.RunCordonOrUncordon(true); err != nil {
		return err
	}
    ...
	drainedNodes := sets.NewString()
	var fatal error
	for _, info := range o.nodeInfos {
        // 驱逐 Pod
		if err := o.deleteOrEvictPodsSimple(info); err == nil {
			drainedNodes.Insert(info.Name)
			printObj(info.Object, o.Out)
		} else {
			// 如果驱逐 Pod 失败，则显示对应的 Node 信息
			if len(remainingNodes) > 0 {
				fmt.Fprintf(o.ErrOut, "There are pending nodes to be drained:\n")
				for _, nodeName := range remainingNodes {
					fmt.Fprintf(o.ErrOut, " %s\n", nodeName)
				}
			}
			break
		}
	}
}
```

在 `deleteOrEvictPodsSimple` 中，先通过 Node 名称获取对应的 Pod 信息，然后进行驱逐动作：

```go
func (o *DrainCmdOptions) deleteOrEvictPodsSimple(nodeInfo *resource.Info) error {
	list, errs := o.drainer.GetPodsForDeletion(nodeInfo.Name)
    ...
	if err := o.drainer.DeleteOrEvictPods(list.Pods()); err != nil {
        ...
	}
}
```

这里的 `GetPodsForDeletion` 会进行一个过滤，包含以下几种场景的过滤，需要注意的是，这里的过滤场景是有严格的顺序的：

```go
func (d *Helper) makeFilters() []podFilter {
	return []podFilter{
        // 被标记删除的 Pod(DeletionTimestamp 不为0)
        d.skipDeletedFilter,
        // 属于 DaemonSet 的 Pod
        d.daemonSetFilter,
        // mirror pod 其实就是 static pod，
        // 是我们在 /etc/kubernetes/manifests/ 中定义的由 kubelet 负责生命周期管理的 Pod
        // 在 `Annotations` 中会包含 `kubernetes.io/config.mirror` 
        d.mirrorPodFilter,
        // 包含本地存储的 Pod，Pod 中的 Volume 字段不为空
        d.localStorageFilter,
        // 不属于 replicate 的 pod，`Controlled By` 不为空的 pod
		d.unreplicatedFilter,
	}
}
```

获取到过滤后的 Pod 列表后，就开始执行驱逐动作，每个 Pod 起一个 goroutine ，提交驱逐动作后会等待，直到 Pod 驱逐完成：

```go
func (d *Helper) evictPods(pods []corev1.Pod, policyGroupVersion string, getPodFn func(namespace, name string) (*corev1.Pod, error)) error {
	returnCh := make(chan error, 1)
    ...
	ctx, cancel := context.WithTimeout(d.getContext(), globalTimeout)
	defer cancel()
	for _, pod := range pods {
		go func(pod corev1.Pod, returnCh chan error) {
			for {
				...
				select {
				case <-ctx.Done():
					// 驱逐超时
					returnCh <- fmt.Errorf("error when evicting pod %q: global timeout reached: %v", pod.Name, globalTimeout)
					return
				default:
                }
                // 驱逐 Pod 动作，最终执行 d.Client.PolicyV1beta1().Evictions(eviction.Namespace).Evict(eviction)
				err := d.EvictPod(pod, policyGroupVersion)
				...
			}
			...
			params := waitForDeleteParams{
				...
            }
            // 等待驱逐动作完成
			_, err := waitForDelete(params)
			if err == nil {
				returnCh <- nil
			} else {
				returnCh <- fmt.Errorf("error when waiting for pod %q terminating: %v", pod.Name, err)
			}
		}(pod, returnCh)
    }
```

`waitForDelete` 如果没有立即完成，会将 `ConditionFunc` 传入 `WaitFor` 循环检测，其中 `ConditionFunc` 的检测依据是 Pod 存在且 ObjectMeta UID发生了改变：

```go
func WaitFor(wait WaitFunc, fn ConditionFunc, done <-chan struct{}) error {
	stopCh := make(chan struct{})
	defer close(stopCh)
	c := wait(stopCh)
	for {
		select {
		case _, open := <-c:
			ok, err := runConditionWithCrashProtection(fn)
			if err != nil {
				return err
			}
			if ok {
				return nil
			}
			if !open {
				return ErrWaitTimeout
			}
		case <-done:
			return ErrWaitTimeout
		}
	}
}
```


## 总结

`kubectl drain` 相关命令的实现还是很简单的，没有特别负责的逻辑，K8s 能够做到这种效果一个重要的原因是所有动作都是声明式的，声明之后等待执行完成就好，不需要主动的去做某些很脏的动作。在驱逐 Pod 的行为中，并不是所有的 Pod 都会被驱逐到其他节点，这里需要格外的注意，在节点下线前需要检查是否有单纯的 Pod 资源仍在节点上运行，是否有使用本地存储的 Pod等类似情况。

平时写代码很糙，见到这种多种设计模式组合的形式看了半天，找机会重新学习下设计模式。




## 参考链接
* https://qiankunli.github.io/2018/12/23/kubernetes_source_kubectl.html
* https://juejin.im/post/5a113e686fb9a0452936596c
* https://rootdeep.github.io/k8s-source-code-analysis/kubectl/construct-visitor.html