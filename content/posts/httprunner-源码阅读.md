---
title: httprunner 源码阅读
date: 2019-09-06 19:50:27
tags:
- Python
---

## 背景

最近工作上每天疲于应付各种事情，周末实在不想继续做工作相关的事情，想起一直想了解的自动化测试框架 [httprunner](https://github.com/httprunner/httprunner)，就阅读下。之前一直有关注作者 [debugtalk](https://debugtalk.com/) 的博客，收获很多。

随着公司的发展，自己也做过很多的工作，其中就包含测试，但是自己当时大部分都是手工测试，虽然会针对其中的部分进行代码编写，但是不成体系。虽然后来就没有继续负责测试工作了，但是对于测试还是很感兴趣，平时开发过程中，最多也就是使用 unittest 或 pytest 来编写单测，这次通过阅读 httprunner 代码来感受下测试框架。

P.S. 在使用及了解 httprunner 之前，最好先了解下 unittest。

## httprunner

>HttpRunner 是一款面向 HTTP(S) 协议的通用测试框架，只需编写维护一份 YAML/JSON 脚本，即可实现自动化测试、性能测试、线上监控、持续集成等多种测试需求。

一句话总结就是 api 自动化测试，其中用到了以下的开源项目：
1. requests
2. locust
3. unittest
4. ...

requests 和 unittest 可以说是 python 开发者用的比较多的两个项目。locust 是一个 api 压力测试，这个我们公司也有用到。

介绍完了项目，我们来跟着官方文档了解运行流程。


## 执行流程

文档中的 [快速上手](https://cn.httprunner.org/quickstart/) 章节与章节名称很配，真心是 **快速上手** ，通过一个又一个的示例来了解具体的功能使用，循序渐进，简直完美。不过又一点不好的地方是 demo 示例的代码不再 httprunner 中，而是在 docs 项目中，使用起来不是很方便，如果有 Dockerfile 来支撑，就更好了。

在 httprunner 项目中，项目的包管理是通过 **poetry** 进行的，比 setuptools 要清晰很多。

首先来看命令，httprunner 随着项目的演进，支持的命令行有 4个，其中 3 个是重复的，1个是压力测试：

```yaml
[tool.poetry.scripts]
hrun = "httprunner.cli:main_hrun"
ate = "httprunner.cli:main_hrun"
httprunner = "httprunner.cli:main_hrun"
locusts = "httprunner.cli:main_locust"
```

我们以 `hrun` 为例，从 argparse 接收到的参数均作为参数传递给 HttpRunner，然后执行实例化 HttpRunner，通过 `HttpRunner.run ` 进行用例的执行：

```python
    runner = HttpRunner(
        failfast=args.failfast,
        save_tests=args.save_tests,
        report_template=args.report_template,
        report_dir=args.report_dir,
        log_level=args.log_level,
        log_file=args.log_file
    )
    try:
        for path in args.testcase_paths:
            runner.run(path, dot_env_path=args.dot_env_path)
    except Exception:
        color_print("!!!!!!!!!! exception stage: {} !!!!!!!!!!".format(runner.exception_stage), "YELLOW")
        raise
```

我们来看下 `runner.run` 做了啥：

```python
    def run(self, path_or_tests, dot_env_path=None, mapping=None):
        if validator.is_testcase_path(path_or_tests):
            return self.run_path(path_or_tests, dot_env_path, mapping)
        elif validator.is_testcases(path_or_tests):
            return self.run_tests(path_or_tests)
        else:
            raise exceptions.ParamsError("Invalid testcase path or testcases: {}".format(path_or_tests))
```

这里只是进行了一层判断，判断传入的参数是一个路径还是具体的用例，因为我们主要是了解整个执行流程，所以我们直接假设传入的是测试用例，来看看 `self.run_tests` ：

```python
    def run_tests(self, tests_mapping):
        """ run testcase/testsuite data
        """
        project_mapping = tests_mapping.get("project_mapping", {})
        if self.save_tests:
            utils.dump_logs(tests_mapping, project_mapping, "loaded")

        # parse tests
        self.exception_stage = "parse tests"
        parsed_testcases = parser.parse_tests(tests_mapping)

        if self.save_tests:
            utils.dump_logs(parsed_testcases, project_mapping, "parsed")

        # add tests to test suite
        self.exception_stage = "add tests to test suite"
        test_suite = self._add_tests(parsed_testcases)

        # run test suite
        self.exception_stage = "run test suite"
        results = self._run_suite(test_suite)

        # aggregate results
        self.exception_stage = "aggregate results"
        self._summary = self._aggregate(results)

        # generate html report
        self.exception_stage = "generate html report"
        report.stringify_summary(self._summary)

        if self.save_tests:
            utils.dump_logs(self._summary, project_mapping, "summary")

        report_path = report.render_html_report(
            self._summary,
            self.report_template,
            self.report_dir
        )

        return report_path
```

先来看下具体的执行函数 `self._run_suite`：

```python
    def _run_suite(self, test_suite):
        tests_results = []

        for testcase in test_suite:
            testcase_name = testcase.config.get("name")
            logger.log_info("Start to run testcase: {}".format(testcase_name))

            result = self.unittest_runner.run(testcase)
            tests_results.append((testcase, result))

        return tests_results
```

真正执行用例执行的是 `self.unittest_runner` ，而 `self.unittest_runner = unittest.TextTestRunner(**kwargs)`，也就是说这里的 `testcase` 其实是 `unittest.suite.TestSuite` 或者 `unittest.case.TestCase`。

这里跟预想中的出现了偏差，我以为这里是自己实现的测试执行及结果比对的方法，没想到调用的是 `unittest`，那么怎么从一个 testcase 变为 `unittest` 可执行对象的，应该就是在 `self._add_tests` 中实现的了：

```python
    def _add_tests(self, testcases):
        """ initialize testcase with Runner() and add to test suite.

        Args:
            testcases (list): testcases list.

        Returns:
            unittest.TestSuite()

        """
```

这个函数略长，这里分开说，从注释中可以知道，最终 unittest 执行的是 `unittest.TestSuite` ，看下具体的逻辑：

```python
        test_suite = unittest.TestSuite() #定义 test_suite 返回值
        for testcase in testcases:
            config = testcase.get("config", {})
            test_runner = runner.Runner(config) # 实例化 Runner，后续主要执行逻辑都在 Runner 中
            TestSequense = type('TestSequense', (unittest.TestCase,), {}) # 通过 type 声明一个 `unittest.TestCase` 的子类

            tests = testcase.get("teststeps", [])
            for index, test_dict in enumerate(tests):
                times = test_dict.get("times", 1)
                try:
                    times = int(times)
                except ValueError:
                    raise exceptions.ParamsError(
                        "times should be digit, given: {}".format(times))

                for times_index in range(times):
                    # suppose one testcase should not have more than 9999 steps,
                    # and one step should not run more than 999 times.
                    test_method_name = 'test_{:04}_{:03}'.format(index, times_index)
                    test_method = _add_test(test_runner, test_dict) 
                    setattr(TestSequense, test_method_name, test_method) # 将上面的 test_method 定义为 TestSequense 属性

            loaded_testcase = self.test_loader.loadTestsFromTestCase(TestSequense) # 利用 TestLoader 来找到符合条件的方法，默认 TestLoader 寻找前缀为 `test` 
            setattr(loaded_testcase, "config", config)
            setattr(loaded_testcase, "teststeps", tests)
            setattr(loaded_testcase, "runner", test_runner)
            test_suite.addTest(loaded_testcase) # 将 `TestLoader.loadTestsFromTestCase` 找到的 testcase 添加到 `test_suite` 中，并最终返回
```

看完上面这里，有一个比较重要的就是 `_add_test` 做了啥：

```python
        def _add_test(test_runner, test_dict):
            """ add test to testcase.
            """
            def test(self):
                try:
                    test_runner.run_test(test_dict)
                except exceptions.MyBaseFailure as ex:
                    self.fail(str(ex))
                finally:
                    self.meta_datas = test_runner.meta_datas
            ...
            return test
```

先忽略其他代码，可以看到 `_add_test` 最终返回的是一个函数，这个函数名称是 `test` ，结合上面的 `self.test_loader.loadTestsFromTestCase` ，可以知道这个函数就是最终执行的方法。


看完这里，回到 `run_tests` 中，在 `self._run_suite` 执行完之后，就进行结果汇总、生成报告了，那么具体的请求是怎么发送出去的，结果又是怎么校验的？猜测是在 `runner.Runner` 中实现的，接着来看。

## 用例请求及校验

在上面提到，最终 `_add_test` 返回的函数中，执行的内容只有一个，就是 `test_runner.run_test` ，那么我们来看看 `run_test` ：

```python
def run_test(self, test_dict):
        """ run single teststep of testcase.
            test_dict may be in 3 types.

        Args:
            test_dict (dict):

                # teststep
                {
                    "name": "teststep description",
                    "variables": [],        # optional
                    "request": {
                        "url": "http://127.0.0.1:5000/api/users/1000",
                        "method": "GET"
                    }
                }

                # nested testcase
                {
                    "config": {...},
                    "teststeps": [
                        {...},
                        {...}
                    ]
                }

                # TODO: function
                {
                    "name": "exec function",
                    "function": "${func()}"
                }

        """
        self.meta_datas = None
        if "teststeps" in test_dict:
            # nested testcase
            test_dict.setdefault("config", {}).setdefault("variables", {})
            test_dict["config"]["variables"].update(
                self.session_context.session_variables_mapping)
            self._run_testcase(test_dict)
        else:
            # api
            try:
                self._run_test(test_dict)
            except Exception:
                # log exception request_type and name for locust stat
                self.exception_request_type = test_dict["request"]["method"]
                self.exception_name = test_dict.get("name")
                raise
            finally:
                self.meta_datas = self.__get_test_data()
```

这里的注释虽然很长，但是很清晰的告诉我们这个函数做了什么，他允许传递的参数是嵌套的，所以这里先做了层判断，我们以最简单的来假设，直接看 `self._run_test` ：

```python
def _run_test(self, test_dict):
        # clear meta data first to ensure independence for each test
        self.__clear_test_data() # 清空测试结果及 session 信息

        # check skip
        self._handle_skip_feature(test_dict) # 根据测试用例关键字执行相应跳过逻辑

        ... # N 多准备工作

        # setup hooks
        setup_hooks = test_dict.get("setup_hooks", [])
        if setup_hooks:
            self.do_hook_actions(setup_hooks, "setup") # 与大部分框架一样，支持 pre hook

        ... # N 多准备工作

        # request
        resp = self.http_client_session.request( # 根据用例发出请求
            method,
            parsed_url,
            name=(group_name or test_name),
            **parsed_test_request
        )
        resp_obj = response.ResponseObject(resp)

        # teardown hooks
        teardown_hooks = test_dict.get("teardown_hooks", []) # 支持 post hook
        if teardown_hooks:
            self.session_context.update_test_variables("response", resp_obj)
            self.do_hook_actions(teardown_hooks, "teardown")

        # extract
        extractors = test_dict.get("extract", {})
        extracted_variables_mapping = resp_obj.extract_response(extractors)
        self.session_context.update_session_variables(extracted_variables_mapping)

        # validate
        validators = test_dict.get("validate") or test_dict.get("validators") or []
        try:
            self.session_context.validate(validators, resp_obj) # 结果校验
        except (exceptions.ParamsError, exceptions.ValidationFailure, exceptions.ExtractFailure):
            err_msg = "{} DETAILED REQUEST & RESPONSE {}\n".format("*" * 32, "*" * 32)
            ...

            raise

        finally:
            self.validation_results = self.session_context.validation_results
```

具体的 http 请求时通过 `self.http_client_session.request` 发送的，通过 `self.session_context.validate` 进行结果校验，来看下具体的校验方式：

```python
        for validator in validators:
            # validator should be LazyFunction object
            if not isinstance(validator, parser.LazyFunction):
                raise exceptions.ValidationFailure(
                    "validator should be parsed first: {}".format(validators))

            # evaluate validator args with context variable mapping.
            validator_args = validator.get_args()
            check_item, expect_item = validator_args
            check_value = self.__eval_validator_check( # 准备参数
                check_item,
                resp_obj
            )
            expect_value = self.__eval_validator_expect(expect_item) # 准备参数
            validator.update_args([check_value, expect_value])

            comparator = validator.func_name
            ...

            try:
                validator.to_value(self.test_variables_mapping) # 执行校验
                validator_dict["check_result"] = "pass"
                validate_msg += "\t==> pass"
                logger.log_debug(validate_msg)
            except (AssertionError, TypeError):
                ...

            self.validation_results.append(validator_dict)
```

前面都是在准备参数，最终执行完 `validator.to_value` 如果没有异常，就直接标记 `check_result` 为 `pass` 了，那么我们需要看看这里的 `to_value` 做了什么，感觉这个方法名称不太好，跟实际做的事情感觉不匹配。

```python
    def to_value(self, variables_mapping=None):
        """ parse lazy data with evaluated variables mapping.
            Notice: variables_mapping should not contain any variable or function.
        """
        variables_mapping = variables_mapping or {}
        args = parse_lazy_data(self._args, variables_mapping)
        kwargs = parse_lazy_data(self._kwargs, variables_mapping)
        self.cache_key = self.__prepare_cache_key(args, kwargs)
        return self._func(*args, **kwargs)
```

看到这里可能会感觉迷糊下，咦，为什么这里执行了 `self._func` ，`self._func` 是什么时候定义的，它做了啥？
我们在编写测试用例的时候 `validate` 通常是`eq`,`gt`,`lt` 等字段，如果把他们直接当作函数执行肯定不行的，那么一定存在一个映射关系将这些关键字转换为对应的函数。

看到这里其实我们漏掉了一个比较重要的步骤，就是 `run_tests` 中的 `parse_tests` 。其实很多时候默认的配置是不足以支撑我们真正逻辑的运行的，往往我们需要根据已有配置来扩充信息，达到满足执行要求的状态，接下来我们来看下测试用例准备工作。


## 用例解析

```python

def parse_tests(tests_mapping):
    
    project_mapping = tests_mapping.get("project_mapping", {})
    testcases = []

    for test_type in tests_mapping:

        if test_type == "testsuites":
            ...

        elif test_type == "testcases":
            for testcase in tests_mapping["testcases"]:
                parsed_testcase = _parse_testcase(testcase, project_mapping)
                testcases.append(parsed_testcase)

        elif test_type == "apis":
            ...

    return testcases
```

这里同样对 `test_type` 进行了判断，如果不是 `testcases` ，则会进行处理，我们还是假设最简单的 `testcases`，可以看到调用了 `_parse_testcase` 方法：

```python
def _parse_testcase(testcase, project_mapping, session_variables_set=None):
    testcase.setdefault("config", {})
    prepared_config = __prepare_config(
        testcase["config"],
        project_mapping,
        session_variables_set
    )
    prepared_testcase_tests = __prepare_testcase_tests(
        testcase["teststeps"],
        prepared_config,
        project_mapping,
        session_variables_set
    )
    return {
        "config": prepared_config,
        "teststeps": prepared_testcase_tests
    }
```

从官方文档可以知道，每个 testcase 中的 config 其实是全局配置，所以这里先解析了 config，然后将其作为参数传递给了 `__prepare_testcase_tests` 用来准备对应的 testcase，最终返回准备好的测试用例及配置，那么跟着看下 `__prepare_testcase_tests`，这个函数很长很长，先忽略其他部分，先来看这段：

```python
        # unify validators' format
        if "validate" in test_dict:
            ref_raw_validators = test_dict.pop("validate", [])
            test_dict["validate"] = [
                validator.uniform_validator(_validator)
                for _validator in ref_raw_validators
            ]
```

如果存在 `validate` ，那么将其转换为 `validator.uniform_validator` 组成的列表，彷佛抓到了什么，我们来看下 `validator.uniform_validator`：

```python
def uniform_validator(validator):
    ...
    # uniform comparator, e.g. lt => less_than, eq => equals
    comparator = get_uniform_comparator(comparator)

    return {
        "check": check_item,
        "expect": expect_value,
        "comparator": comparator
    }
```

最终返回的是一个字典，其中的 `comparator` 是 `get_uniform_comparator` 返回值，继续看：

```python
def get_uniform_comparator(comparator):
    """ convert comparator alias to uniform name
    """
    if comparator in ["eq", "equals", "==", "is"]:
        return "equals"
    elif comparator in ["lt", "less_than"]:
        return "less_than"
    ...
    else:
        return comparator
```

终于找到了校验关键字的映射关键字，那么我们继续回头看 `__prepare_testcase_tests`：

```python
        # convert validators to lazy function
        validators = test_dict.pop("validate", [])
        prepared_validators = []
        for _validator in validators:
            function_meta = {
                "func_name": _validator["comparator"],
                "args": [
                    _validator["check"],
                    _validator["expect"]
                ],
                "kwargs": {}
            }
            prepared_validators.append(
                LazyFunction(
                    function_meta,
                    functions,
                    teststep_variables_set
                )
            )
        test_dict["validate"] = prepared_validators

        # convert variables and functions to lazy object.
        # raises VariableNotFound if undefined variable exists in test_dict
        prepared_test_dict = prepare_lazy_data(
            test_dict,
            functions,
            teststep_variables_set
        )
        prepared_testcase_tests.append(prepared_test_dict)
```

在这里针对刚刚得到的关键字对应函数名称又进行了一次封装，现在的 `test_dict["validate"]` 就是一个 `LazyFunction` 组成的列表了，回想最开始我们为啥要看用例解析这部分的代码，因为我们发现在函数校验那里没找到真正执行的函数，我们来看下 `LazyFunction` 的构造函数：

```python
    def __init__(self, function_meta, functions_mapping=None, check_variables_set=None):
        """ init LazyFunction object with function_meta

        Args:
            function_meta (dict): function name, args and kwargs.
                {
                    "func_name": "func",
                    "args": [1, 2]
                    "kwargs": {"a": 3, "b": 4}
                }

        """
        self.functions_mapping = functions_mapping or {}
        self.check_variables_set = check_variables_set or set()
        self.cache_key = None
        self.__parse(function_meta)
```

重点在最后一个行，`self.__parse(function_meta)`：

```python
    def __parse(self, function_meta):
        """ init func as lazy functon instance

        Args:
            function_meta (dict): function meta including name, args and kwargs
        """
        self._func = get_mapping_function(
            function_meta["func_name"],
            self.functions_mapping
        )
        self.func_name = self._func.__name__
        self._args = prepare_lazy_data(
            function_meta.get("args", []),
            self.functions_mapping,
            self.check_variables_set
        )
        self._kwargs = prepare_lazy_data(
            function_meta.get("kwargs", {}),
            self.functions_mapping,
            self.check_variables_set
        )

        ...
```

在这里找到了我们一直想找的 `self._func` 定义，看函数名是通过 `func_name` 从一个 map 中返回真正的函数，来看看是不是这样：

```python
def get_mapping_function(function_name, functions_mapping):
    
    ...

    try:
        # check if HttpRunner builtin functions
        from httprunner import loader
        built_in_functions = loader.load_builtin_functions()
        return built_in_functions[function_name]
    except KeyError:
        pass
    ...
```


```python
from httprunner import built_in, exceptions, logger, parser, utils, validator
def load_builtin_functions():
    """ load built_in module functions
    """
    return load_module_functions(built_in)
```


```python
def load_module_functions(module):
    module_functions = {}

    for name, item in vars(module).items():
        if validator.is_function(item):
            module_functions[name] = item

    return module_functions
```

一路追下来，具体的实现应该在 `built_in.py` 没跑：

```python
def equals(check_value, expect_value):
    assert check_value == expect_value

def less_than(check_value, expect_value):
    assert check_value < expect_value

...
```

Ok，到这里我们终于了解了用例的解析工作做了什么，同时也解答了我们上面遗留下来的疑问，结果校验执行的是什么。


## 总结

在公司内部同样有着测试框架，是基于 Robot Framework 进行开发的，但是我被 Robot 的代码量劝退了。。。httprunner 项目整体来看代码量不大，很适合作为初步了解自动化测试的框架来阅读。

根据作者自述，项目起源于大疆内部的测试需求，之后转为开源项目，不知道作者现在是否是因为离开了大疆还是其他原因，现在 httprunner 的社区感觉很差，明明是有公司使用的，但是并没有积极参与，作者一个人承担了几乎100% 的代码开发任务，感觉是一个不健康的社区。

希望自己有机会的话也参与进去，不希望这样一个项目 `死` 掉。


## P.S.

其实这篇博客应该是在周五晚上完成的，但是写着写着发现自己对于项目中的整体流程无法理顺，今天又用了大半天的时间重新读了代码，一点一点记录下来。

嗯，写博客的好处之一。