---
title: Yum 寻找 Best Package 评分机制
date: 2022-04-29 23:04:16
tags:
- Linux
---


## 背景

公司产品最终交付形态是 ISO，在涉及一个产品的多个 OEM 场景时，会选择在标准版本的基础上，删除某些软件包，新增某些软件包的形式来减少构建时间。产品的 BaseOS 是 CentOS，包管理器是 RPM 系，也就需要使用 `rpm` / `yum` 等命令来实现。
其中新增某些软件包是使用 `yumdownloader` 来完成的。在 Yum Repository 中会包含同一软件包的多个版本，预期 `yumdownloader` 会下载 Yum Repository 中某个软件最新版本的包，比如 `yumdownloader zbs-5.1.2*` ，则会下载 zbs-5.1.2 大版本的最新 release 版本。

但是最近发现，从某个版本开始 `yumdownloader` 没有下载最新的软件包，反而停在了一个两个月之前构建的版本，于是开始调查原因。

## Yumdownloader

`yumdownloader` 工具集是由 `yum-utils` 提供，同时还提供了 `repotrack`，`repoquery`, `reposync` 等有用的工具。`yumdownloader` 使用方式是 `yumdownloader $pkg` 即可。在 `yum-utils` 中会大量引用 `yum` module，因此需要同时查找两个 Git repo。

`yum-utils` 代码仓库地址： https://github.com/rpm-software-management/yum-utils/blob/master/yumdownloader.py   
`yum` 代码仓库地址：https://github.com/rpm-software-management/yum

### 下载逻辑

```
def main(self):
    # Add command line option specific to yumdownloader
    self.addCmdOptions()
    ...
    # make yumdownloader work as non root user.
    if not self.setCacheDir():
        self.logger.error("Error: Could not make cachedir, exiting")
        sys.exit(50)
    ...
    # Setup yum (Ts, RPM db, Repo & Sack)
    self.doUtilYumSetup()
    # Do the real action
    self.exit_code = self.downloadPackages(opts)
```

* 解析命令行参数
* 检查执行用户权限
* 配置 Yum Repo 正确性
* 下载 RPM

其中前几项不是很重要，直接看 `self.downloadPackages(opts)` 逻辑。主要做了以下几件事情：  

1. 根据 PKG 列表进行 Repo 中的查询，查询出所有的软件包；  
2. 根据查询结果，进行解析匹配，其中精确匹配和模糊匹配会进行后续处理；
3. 根据 RPM `name+arch` 作为 key 来将所有的 Pkg 列表转换为 Dict；
4. 遍历 Dict，从列表中找到 Best Package ，并将其添加到下载列表中；
5. 根据下载列表信息进行下载。


Github: https://github.com/rpm-software-management/yum-utils/blob/master/yumdownloader.py#L136
```python
def downloadPackages(self,opts):
    
    toDownload = [] # 最终要下载的 RPM

    packages = self.cmds
    for pkg in packages:
        toActOn = []

        if not pkg or pkg[0] != '@':
            pkgnames = [pkg] # 如果 PKG 名称不以 `@` 开头，那么就是单个软件包；如果以 `@` 开头，那么表示是一个 Group；
        else:
            # Group 处理逻辑，忽略
            ...

        pos = self.pkgSack.returnPackages(patterns=pkgnames) # 在 Yum repo 中根据 pkgnames 来获取查询到的包列表
        exactmatch, matched, unmatched = parsePackages(pos, pkgnames) # 根据 pkgnames 名称 从 pos 中解析具体的匹配结果，其中如果精确匹配则添加到 exactmatch，如果模糊匹配则添加到 matched。在本文场景下所有匹配为模糊匹配，所以在 matched 列表中
        installable = (exactmatch + matched) # 最终可安装的是精确匹配和模糊匹配的集合
        if not installable:
            ...

        for newpkg in installable:
            toActOn.extend(_best_convert_pkg2srcpkgs(self, opts, newpkg)) # 根据解析结果，将所有处于 installable 中的包都找到具体来源
        if toActOn:
            pkgGroups = self._groupPackages(toActOn) # 使用 RPM `name` 和 `arch` 针对 toActOn 列表进行初步分组，转换为 dict
            for group in pkgGroups:
                pkgs = pkgGroups[group]
                if opts.source:
                    ...     # 根据 yumdownloader 命令参数进行额外的处理，忽略
                else:
                    toDownload.extend(self.bestPackagesFromList(pkgs)) # 从 pkgs 列表中选择 best Package，然后添加到 toDownload 列表中
                        
    ...
    # set localpaths
    for pkg in toDownload:
        pkg.repo.copy_local = True
        pkg.repo.cache = 0

    # use downloader from YumBase
    exit_code = 0
    probs = self.downloadPkgs(toDownload) # 下载具体 RPM 
    if probs:
        exit_code = 2
        for key in probs:
            for error in probs[key]:
                self.logger.error('%s: %s', key, error)
    return exit_code
```

在我的场景中，问题出在查找 Best Package 步骤中，相关日志如下，可以观察到在 Yum repo 中查询到了 zbs-5.1.2 所有的 release RPM，分别为 rc1 ,rc2 一直到 rc14 ，排序方式是字母序。 parsePackages 解析出所有的 PKG 均在 matched 中，因为都是模糊匹配，最终传入 bestPackagesFromList 方法中的参数是所有到的 release RPM，预期是返回最新的 release RPM ，即 zbs-5.1.2-rc14，但是返回的是 rc7 。接下来需要调查 bestPackagesFromList 是如何判断的。

```bash
['zbs-5.1.2*']
pos: [<YumAvailablePackageSqlite : zbs-5.1.2-rc1.0.release.git.g0cb56434e.el7.SMTX.HCI.x86_64 (0x2bf6e50)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc10.0.release.git.g228f49070.el7.SMTX.HCI.x86_64 (0x2bf6dd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc11.0.release.git.g6d5d763ee.el7.SMTX.HCI.x86_64 (0x2bf6d90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc12.0.release.git.g9a6400652.el7.SMTX.HCI.x86_64 (0x2bf6bd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc13.0.release.git.g339708733.el7.SMTX.HCI.x86_64 (0x2bf6f90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc14.0.release.git.g42733ba17.el7.SMTX.HCI.x86_64 (0x2bf6fd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc2.0.release.git.gfa5212d39.el7.SMTX.HCI.x86_64 (0x2c03050)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc3.0.release.git.ge4ecabe7b.el7.SMTX.HCI.x86_64 (0x2c03090)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc4.0.release.git.g6e9ed979b.el7.SMTX.HCI.x86_64 (0x2c030d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc5.0.release.git.gfa8bab6ad.el7.SMTX.HCI.x86_64 (0x2c03110)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc6.0.release.git.g51f0f1277.el7.SMTX.HCI.x86_64 (0x2c03150)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc7.0.release.git.gccd6dbf2a.el7.SMTX.HCI.x86_64 (0x2c03190)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc8.0.release.git.g763bb9046.el7.SMTX.HCI.x86_64 (0x2c031d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc9.0.release.git.g238ab2320.el7.SMTX.HCI.x86_64 (0x2c03210)>]
exactmatch: []
matched: [<YumAvailablePackageSqlite : zbs-5.1.2-rc14.0.release.git.g42733ba17.el7.SMTX.HCI.x86_64 (0x2bf6fd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc13.0.release.git.g339708733.el7.SMTX.HCI.x86_64 (0x2bf6f90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc2.0.release.git.gfa5212d39.el7.SMTX.HCI.x86_64 (0x2c03050)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc7.0.release.git.gccd6dbf2a.el7.SMTX.HCI.x86_64 (0x2c03190)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc3.0.release.git.ge4ecabe7b.el7.SMTX.HCI.x86_64 (0x2c03090)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc9.0.release.git.g238ab2320.el7.SMTX.HCI.x86_64 (0x2c03210)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc6.0.release.git.g51f0f1277.el7.SMTX.HCI.x86_64 (0x2c03150)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc4.0.release.git.g6e9ed979b.el7.SMTX.HCI.x86_64 (0x2c030d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc10.0.release.git.g228f49070.el7.SMTX.HCI.x86_64 (0x2bf6dd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc8.0.release.git.g763bb9046.el7.SMTX.HCI.x86_64 (0x2c031d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc12.0.release.git.g9a6400652.el7.SMTX.HCI.x86_64 (0x2bf6bd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc11.0.release.git.g6d5d763ee.el7.SMTX.HCI.x86_64 (0x2bf6d90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc1.0.release.git.g0cb56434e.el7.SMTX.HCI.x86_64 (0x2bf6e50)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc5.0.release.git.gfa8bab6ad.el7.SMTX.HCI.x86_64 (0x2c03110)>]
unmatched: []
pkgGroups: {'zbs.x86_64': [<YumAvailablePackageSqlite : zbs-5.1.2-rc14.0.release.git.g42733ba17.el7.SMTX.HCI.x86_64 (0x2bf6fd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc13.0.release.git.g339708733.el7.SMTX.HCI.x86_64 (0x2bf6f90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc2.0.release.git.gfa5212d39.el7.SMTX.HCI.x86_64 (0x2c03050)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc7.0.release.git.gccd6dbf2a.el7.SMTX.HCI.x86_64 (0x2c03190)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc3.0.release.git.ge4ecabe7b.el7.SMTX.HCI.x86_64 (0x2c03090)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc9.0.release.git.g238ab2320.el7.SMTX.HCI.x86_64 (0x2c03210)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc6.0.release.git.g51f0f1277.el7.SMTX.HCI.x86_64 (0x2c03150)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc4.0.release.git.g6e9ed979b.el7.SMTX.HCI.x86_64 (0x2c030d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc10.0.release.git.g228f49070.el7.SMTX.HCI.x86_64 (0x2bf6dd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc8.0.release.git.g763bb9046.el7.SMTX.HCI.x86_64 (0x2c031d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc12.0.release.git.g9a6400652.el7.SMTX.HCI.x86_64 (0x2bf6bd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc11.0.release.git.g6d5d763ee.el7.SMTX.HCI.x86_64 (0x2bf6d90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc1.0.release.git.g0cb56434e.el7.SMTX.HCI.x86_64 (0x2bf6e50)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc5.0.release.git.gfa8bab6ad.el7.SMTX.HCI.x86_64 (0x2c03110)>]}
pkgs: [<YumAvailablePackageSqlite : zbs-5.1.2-rc14.0.release.git.g42733ba17.el7.SMTX.HCI.x86_64 (0x2bf6fd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc13.0.release.git.g339708733.el7.SMTX.HCI.x86_64 (0x2bf6f90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc2.0.release.git.gfa5212d39.el7.SMTX.HCI.x86_64 (0x2c03050)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc7.0.release.git.gccd6dbf2a.el7.SMTX.HCI.x86_64 (0x2c03190)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc3.0.release.git.ge4ecabe7b.el7.SMTX.HCI.x86_64 (0x2c03090)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc9.0.release.git.g238ab2320.el7.SMTX.HCI.x86_64 (0x2c03210)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc6.0.release.git.g51f0f1277.el7.SMTX.HCI.x86_64 (0x2c03150)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc4.0.release.git.g6e9ed979b.el7.SMTX.HCI.x86_64 (0x2c030d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc10.0.release.git.g228f49070.el7.SMTX.HCI.x86_64 (0x2bf6dd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc8.0.release.git.g763bb9046.el7.SMTX.HCI.x86_64 (0x2c031d0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc12.0.release.git.g9a6400652.el7.SMTX.HCI.x86_64 (0x2bf6bd0)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc11.0.release.git.g6d5d763ee.el7.SMTX.HCI.x86_64 (0x2bf6d90)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc1.0.release.git.g0cb56434e.el7.SMTX.HCI.x86_64 (0x2bf6e50)>, <YumAvailablePackageSqlite : zbs-5.1.2-rc5.0.release.git.gfa8bab6ad.el7.SMTX.HCI.x86_64 (0x2c03110)>]
toDownload: [<YumAvailablePackageSqlite : zbs-5.1.2-rc7.0.release.git.gccd6dbf2a.el7.SMTX.HCI.x86_64 (0x2c03190)>]
```


## Yum 

`yumdownloader` 是 `yum` module 的功能分装，具体的 `bestPackagesFromList` 是在 `yum` module 中实现的。`bestPackagesFromList` 自身先根据 pkg arch 来进行分类，其中判断依据为：

Github： https://github.com/rpm-software-management/yum/blob/master/rpmUtils/arch.py#L153:5
```
# dict mapping arch -> ( multicompat, best personality, biarch personality )
multilibArches = { "x86_64":  ( "athlon", "x86_64", "athlon" ),
                   "sparc64v": ( "sparcv9v", "sparcv9v", "sparc64v" ),
                   "sparc64": ( "sparcv9", "sparcv9", "sparc64" ),
                   "ppc64":   ( "ppc", "ppc", "ppc64" ),
                   "s390x":   ( "s390", "s390x", "s390" ),
                   }
```


Github: https://github.com/rpm-software-management/yum/blob/master/yum/__init__.py#L4432  


```python
def bestPackagesFromList(self, pkglist, arch=None, single_name=False,
                            req=None):
    """Return the best packages from a list of packages.  This
    function is multilib aware, so that it will not compare
    multilib to singlelib packages.
    :param pkglist: the list of packages to return the best
        packages from
    :param arch: packages will be selected that are compatible
        with the architecture specified by *arch*
    :param single_name: whether to return a single package name
    :param req: the requirement from the user
    :return: a list of the best packages from *pkglist*
    """
    returnlist = []
    compatArchList = self.arch.get_arch_list(arch)
    multiLib = []
    singleLib = []
    noarch = []
    for po in pkglist: # 根据架构来进行筛选，x86_64 是 multiLibArch
        if po.arch not in compatArchList:
            continue
        elif po.arch in ("noarch"):
            noarch.append(po)
        elif isMultiLibArch(arch=po.arch):
            multiLib.append(po) # 最终所有 pkg 添加到 multiLib 中
        else:
            singleLib.append(po)
            
    # we now have three lists.  find the best package(s) of each
    multi = self._bestPackageFromList(multiLib, req=req) # 根据不同架构找到 best package
    single = self._bestPackageFromList(singleLib, req=req)
    no = self._bestPackageFromList(noarch, req=req)

    ...

    return returnlist
```

继续追踪 `_bestPackageFromList` 的实现，可以看到

Github: https://github.com/rpm-software-management/yum/blob/master/yum/__init__.py#L4409

```python
def _bestPackageFromList(self, pkglist, req=None):
    """take list of package objects and return the best package object.
        If the list is empty, return None. 
        
        Note: this is not aware of multilib so make sure you're only
        passing it packages of a single arch group.
        :param pkglist: the list of packages to return the best
            packages from
        :param req: the requirement from the user
        :return: a list of the best packages from *pkglist*
    """
    ...
    bestlist = self._compare_providers(pkglist, reqpo=None, req=req)
    return bestlist[0][0]
```

终于找到最关键的部分： `_compare_providers` ，这是一个巨大的函数，300行，根据注释可以看到主要用户给 pkg 打分：

Github: https://github.com/rpm-software-management/yum/blob/master/yum/depsolve.py#L1465
```Python
def _compare_providers(self, pkgs, reqpo, req=None):
    """take the list of pkgs and score them based on the requesting package
        return a dictionary of po=score"""
    self.verbose_logger.log(logginglevels.DEBUG_4,
            _("Running compare_providers() for %s") %(str(pkgs)))
```

接下来是具体的打分流程，先根据 repo id 的字母序进行过滤，如果多个 repo 均提供了同一版本的 PKG，那么会根据 repo 字母序进行选取：

```python
    # Do a NameArch filtering, based on repo. __cmp__
    unique_nevra_pkgs = {}
    for pkg in pkgs:
        if (pkg.pkgtup in unique_nevra_pkgs and
            unique_nevra_pkgs[pkg.pkgtup].repo <= pkg.repo):
            continue
        unique_nevra_pkgs[pkg.pkgtup] = pkg
    pkgs = unique_nevra_pkgs.values()
```
其中 pkg.repo 的实现如下：

```python
class Repository:
    """this is an actual repository object"""       

    def __init__(self, repoid):
        self.id = repoid
        self.quick_enable_disable = {}
        self.disable()
        self._xml2sqlite_local = False

    def __cmp__(self, other):
        """ Sort base class repos. by alphanumeric on their id, also
            see __cmp__ in YumRepository(). """
        if self.id > other.id:
            return 1
        elif self.id < other.id:
            return -1
        else:
            return 0
```

初始化 pkgresults ，其中 value 是对应的分数，第一步打分是检查目标 pkg 是否已经存在于当前主机上，会通过查询 rpmdb 来获取信息，如果已经存在了，那么这种情况是升级情况，需要与当前主机上 newest 的 pkg 进行比较，如果当前主机上最新的包版本小于 pkg，则 +5 分，如果等于则 +1000 分，如果小于则 -1024 分。如果当前主机上没有，则跳过。

```python
        pkgresults = {}
        penalize = set()

        for pkg in pkgs:
            pkgresults[pkg] = 0 # 初始化各个 pkg 的分数为 0 
        
        # hand this off to our plugins
        self.plugins.run("compare_providers", providers_dict=pkgresults, 
                                      reqpo=reqpo)
        
        for pkg in pkgresults.keys():
            rpmdbpkgs = self.rpmdb.searchNevra(name=pkg.name)
            if rpmdbpkgs:
                #  We only want to count things as "installed" if they are
                # older than what we are comparing, because this then an update
                # so we give preference. If they are newer then obsoletes/etc.
                # could play a part ... this probably needs a better fix.
                newest = sorted(rpmdbpkgs)[-1]
                if newest.verLT(pkg):
                    # give pkgs which are updates just a SLIGHT edge
                    # we should also make sure that any pkg
                    # we are giving an edge to is not obsoleted by
                    # something else in the transaction. :(
                    # there are many ways I hate this - this is but one
                    pkgresults[pkg] += 5
                elif newest.verEQ(pkg):
                    #  We get here from bestPackagesFromList(), give a giant
                    # bump to stuff that is already installed.
                    pkgresults[pkg] += 1000
                elif newest.verGT(pkg):
                    # if the version we're looking at is older than what we have installed
                    # score it down like we would an obsoleted pkg
                    pkgresults[pkg] -= 1024
            else:
                # just b/c they're not installed pkgs doesn't mean they should
                # be ignored entirely. Just not preferred
                pass
```

O(n^2)遍历 pkgs，先获取 Yum repo 中 newest version，然后保存下来，进行比对，如果当前 pkg 不等于 newest version，则 -1024 分。当前 repo 中匹配的 pkgs 列表一共 14 个， 遍历结束后每个 pkg 的分数应该是 13 * (-1024) = -13312。如果 pkg 被 nextpkg 所废除，那么 pkg 分数继续 -1024。如果传递了 arch 相关参数，那么会根据 arch 进行比较，如果哪个 pkg 提供了当前 arch 的包，那么会 +5 分。

```python
        lpos = {}
        for po in pkgs:
            for nextpo in pkgs:
                if po == nextpo:
                    continue

                #  If this package isn't the latest version of said package,
                # treat it like it's obsoleted. The problem here is X-1
                # accidentally provides FOO, so you release X-2 without the
                # provide, but X-1 is still picked over a real provider.
                if po.name not in lpos:
                    lpos[po.name] = self.pkgSack.returnNewestByName(po.name)[:1]
                if not lpos[po.name] or not po.verEQ(lpos[po.name][0]):
                    pkgresults[po] -= 1024

                obsoleted = False
                if po.obsoletedBy([nextpo]):
                    obsoleted = True
                    pkgresults[po] -= 1024
                                
                    self.verbose_logger.log(logginglevels.DEBUG_4,
                        _("%s obsoletes %s") % (nextpo, po))

                if reqpo:
                    arches = (reqpo.arch, self.arch.bestarch)
                else:
                    arches = (self.arch.bestarch,)
                
                for thisarch in arches:
                    res = _compare_arch_distance(po, nextpo, thisarch)
                    if not res:
                        continue
                    self.verbose_logger.log(logginglevels.DEBUG_4,                   
                       _('archdist compared %s to %s on %s\n  Winner: %s' % (po, nextpo, thisarch, res)))

                    if res == po:
                        pkgresults[po] += 5

            # End of O(N*N): for nextpo in pkgs:
```

接下来会根据 pkg 是否存在 source rpm，是否是弱引用，是否是直接引用，是否存在冲突等进行分数的增减。


```python
            # End of O(N*N): for nextpo in pkgs:

            # Respect the repository priority for each provider, the default is 80
            pkgresults[po] += (100 - po.repo.compare_providers_priority) * 10
            self.verbose_logger.log(logginglevels.DEBUG_4,
                _('compare_providers_priority for %s is %s' % (po, po.repo.compare_providers_priority)))

            if _common_sourcerpm(po, reqpo):
                self.verbose_logger.log(logginglevels.DEBUG_4,
                    _('common sourcerpm %s and %s' % (po, reqpo)))
                pkgresults[po] += 20
            if _weak_req(po, reqpo):
                self.verbose_logger.log(logginglevels.DEBUG_4,
                    _('weak req %s and %s' % (po, reqpo)))
                pkgresults[po] += 666
            if _info_req(po, reqpo):
                self.verbose_logger.log(logginglevels.DEBUG_4,
                    _('informational req %s and %s' % (po, reqpo)))
                pkgresults[po] += 333
            if _conflict_req(po, reqpo):
                self.verbose_logger.log(logginglevels.DEBUG_4,
                    _('conflict req %s and %s' % (po, reqpo)))
                penalize.add(po)
            if self.isPackageInstalled(po.base_package_name):
                self.verbose_logger.log(logginglevels.DEBUG_4,
                    _('base package %s is installed for %s' % (po.base_package_name, po)))
                pkgresults[po] += 5 # Same as before - - but off of base package name
            if reqpo:
                cpl = _common_prefix_len(po.name, reqpo.name)
                if cpl > 2:
                    self.verbose_logger.log(logginglevels.DEBUG_4,
                        _('common prefix of %s between %s and %s' % (cpl, po, reqpo)))
                
                    pkgresults[po] += cpl*2
```

当基本分数进行打分完成后， 还存在多个 best pkg，那么会根据当前 OS 安装 pkg 所需依赖数量进行判定，依赖数量越少，则分数越高，最终依赖数量少的 pkg 分数 +1。此时部分 pkg 分数从 -13112 变为 -13111。

```python
        #  If we have more than one "best", see what would happen if we picked
        # each package ... ie. what things do they require that _aren't_ already
        # installed/to-be-installed. In theory this can screw up due to:
        #   pkgA => requires pkgX
        #   pkgB => requires pkgY, requires pkgZ
        # ...but pkgX requires 666 other things. Going recursive is
        # "non-trivial" though, python != prolog. This seems to do "better"
        # from simple testing though.
        bestnum = max(pkgresults.values()) # 将当前 pkg 分数最大的置为 bestnum
        rec_depsolve = {}
        for po in pkgs:
            if pkgresults[po] != bestnum: # 如果当前 pkg 分数不等于最高分，跳过
                continue
            rec_depsolve[po] = 0
        if len(rec_depsolve) > 1: # 如果仍有多个 pkg，则进行依赖判定
            for po in rec_depsolve:
                fake_txmbr = TransactionMember(po)

                #  Note that this is just requirements, so you could also have
                # 4 requires for a single package. This might be fixable, if
                # needed, but given the above it's probably better to leave it
                # like this.
                reqs = self._checkInstall(fake_txmbr) # 检查安装 pkg 所需依赖
                rec_depsolve[po] = len(reqs) # 将依赖数量置为当前 pkg 的分数

            bestnum = min(rec_depsolve.values()) # 找到依赖数量最少的分数作为 bestnum 
            self.verbose_logger.log(logginglevels.DEBUG_4,
                                    _('requires minimal: %d') % bestnum)
            for po in rec_depsolve:
                if rec_depsolve[po] == bestnum: 
                    self.verbose_logger.log(logginglevels.DEBUG_4,
                            _(' Winner: %s') % po)
                    pkgresults[po] += 1 # 将依赖数量结果填充会 pkgresults 中，依赖数量最少的分数 +1
                else:
                    num = rec_depsolve[po]
                    self.verbose_logger.log(logginglevels.DEBUG_4,
                            _(' Loser(with %d): %s') % (num, po))
```

将当前分数最高的置为 bestnum，遍历 pkgs，如果当前 pkg 分数等于 bestnum，则将其分数 +1000，并将其分数 +(pkg.name)*-1 。如果 -13111 + 1000 +(-3) = -12114。

```python
        #  We don't want to decide to use a "shortest first", if something else
        # has told us to pick something else. But we want to pick between
        # multiple "best" packages. So we spike all the best packages (so
        # only those can win) and then bump them down by package name length.
        bestnum = max(pkgresults.values())
        for po in pkgs:
            if pkgresults[po] != bestnum:
                continue
            pkgresults[po] += 1000
            pkgresults[po] += (len(po.name)*-1)

        # Bump down any packages that we identified as "last-resort" in such a
        # way that they all score below the worst overall score whilst keeping
        # their relative differences.
        shift = max(pkgresults.values()) - min(pkgresults.values()) + 1
        for po in penalize:
            pkgresults[po] -= shift

        bestorder = sorted(pkgresults.items(),
                           key=lambda x: (x[1], x[0]), reverse=True)
        self.verbose_logger.log(logginglevels.DEBUG_4,
                _('Best Order: %s' % str(bestorder)))

        return bestorder
```

最终根据 pkg 分数进行重新排序，返回第一个结果。

## 总结

发现这个问题最初是猜测是 Yum Repository 配置问题，阅读代码之后判定是 RPM 在某个版本依赖发生了改变，增加了某些依赖项，导致了 Yum 打分认为其分数较低，从而无法通过 yumdownloader 下载最新的 RPM。与相关同事确认，rc8 版本开始增加了部分依赖，调查结束。

