---
title: 《100 Go Mistakes and How to Avoid Them》摘要
date: 2022-12-24 09:00:00
tags:
- Book
description: 断断续续看了好久的书。
---


### 1. Go: Simple to learn but hard to master

* Go is a modern programming language that enables developer productivity, which is crucial for most companies today. 
* Go is simple to learn but not easy to master. This is why we need to deepen our knowledge to make the most effective use of the language. 
* Learning via mistakes and concrete examples is a powerful way to be proficient in a language. This book will accelerate our path to proficiency by exploring 100 common mistakes. 

### 2. Code and project organization

* Avoiding shadowed variables can help prevent mistakes like referencing the wrong variable or confusing readers. 
* Avoiding nested levels and keeping the happy path aligned on the left makes building a mental code model easier. 
* When initializing variables, remember that init functions have limited error handling and make state handling and testing more complex. In most cases, initializations should be handled as specific functions. 
* Forcing the use of getters and setters isn’t idiomatic in Go. Being pragmatic and finding the right balance between efficiency and blindly following certain idioms should be the way to go. 
* Abstractions should be discovered, not created. To prevent unnecessary complexity, create an interface when you need it and not when you foresee needing it, or if you can at least prove the abstraction to be a valid one. 
* Keeping interfaces on the client side avoids unnecessary abstractions. 
* To prevent being restricted in terms of flexibility, a function shouldn’t return interfaces but concrete implementations in most cases. Conversely, a function should accept interfaces whenever possible. 
* Only use any if you need to accept or return any possible type, such as json. Marshal. Otherwise, any doesn’t provide meaningful information and can lead to compile-time issues by allowing a caller to call methods with any data type.
* Relying on generics and type parameters can prevent writing boilerplate code to factor out elements or behaviors. However, do not use type parameters prematurely, but only when you see a concrete need for them. Otherwise, they introduce unnecessary abstractions and complexity. 
* Using type embedding can also help avoid boilerplate code; however, ensure that doing so doesn’t lead to visibility issues where some fields should have remained hidden. 
* To handle options conveniently and in an API-friendly manner, use the functional options pattern. 
* Following a layout such as project-layout can be a good way to start structuring Go projects, especially if you are looking for existing conventions to standardize a new project. 
* Naming is a critical piece of application design. Creating packages such as common, util, and shared doesn’t bring much value for the reader. Refactor such packages into meaningful and specific package names. 
* To avoid naming collisions between variables and packages, leading to confusion or perhaps even bugs, use unique names for each one. If this isn’t feasible, use an import alias to change the qualifier to differentiate the package name from the variable name, or think of a better name. 
* To help clients and maintainers understand your code’s purpose, document exported elements. 
* To improve code quality and consistency, use linters and formatters.


### 3. Data types

* When reading existing code, bear in mind that integer literals starting with 0 are octal numbers. Also, to improve readability, make octal integers explicit by prefixing them with 0o.
* Because integer overflows and underflows are handled silently in Go, you can implement your own functions to catch them.
* Making floating-point comparisons within a given delta can ensure that your code is portable.
* When performing addition or subtraction, group the operations with a similar order of magnitude to favor accuracy. Also, perform multiplication and division before addition and subtraction.
* Understanding the difference between slice length and capacity should be part of a Go developer’s core knowledge. The slice length is the number of available elements in the slice, whereas the slice capacity is the number of elements in the backing array.
* When creating a slice, initialize it with a given length or capacity if its length is already known. This reduces the number of allocations and improves performance. The same logic goes for maps, and you need to initialize their size.
* Using copy or the full slice expression is a way to prevent append from creating conflicts if two different functions use slices backed by the same array. However, only a slice copy prevents memory leaks if you want to shrink a large slice.
* To copy one slice to another using the copy built-in function, remember that the number of copied elements corresponds to the minimum between the two slice’s lengths.
* Working with a slice of pointers or structs with pointer fields, you can avoid memory leaks by marking as nil the elements excluded by a slicing operation.
* To prevent common confusions such as when using the encoding/json or the reflect package, you need to understand the difference between nil and empty slices. Both are zero-length, zero-capacity slices, but only a nil slice doesn’t require allocation.
* To check if a slice doesn’t contain any element, check its length. This check works regardless of whether the slice is nil or empty. The same goes for maps.
* To design unambiguous APIs, you shouldn’t distinguish between nil and empty slices.


### 4. Control structures

* The value element in a range loop is a copy. Therefore, to mutate a struct, for example, access it via its index or via a classic for loop (unless the element or the field you want to modify is a pointer).
* Understanding that the expression passed to the range operator is evaluated only once before the beginning of the loop can help you avoid common mistakes such as inefficient assignment in channel or slice iteration.
* Using a local variable or accessing an element using an index, you can prevent mistakes while copying pointers inside a loop.
* To ensure predictable outputs when using maps, remember that a map data structure  
  – Doesn’t order the data by keys  
  – Doesn’t preserve the insertion order  
  – Doesn’t have a deterministic iteration order  
  – Doesn’t guarantee that an element added during an iteration will be produced during this iteration  
* Using break or continue with a label enforces breaking a specific statement. This can be helpful with switch or select statements inside loops.
* Extracting loop logic inside a function leads to executing a defer statement at the end of each iteration.

### 5. Strings

* Understanding that a rune corresponds to the concept of a Unicode code point and that it can be composed of multiple bytes should be part of the Go developer’s core knowledge to work accurately with strings.
* Iterating on a string with the range operator iterates on the runes with the index corresponding to the starting index of the rune’s byte sequence. To access a specific rune index (such as the third rune), convert the string into a []rune.
* strings.TrimRight/strings.TrimLeft removes all the trailing/leading runes contained in a given set, whereas strings.TrimSuffix/strings.TrimPrefix returns a string without a provided suffix/prefix.
* Concatenating a list of strings should be done with strings.Builder to prevent allocating a new string during each iteration.
* Remembering that the bytes package offers the same operations as the strings package can help avoid extra byte/string conversions.
* Using copies instead of substrings can prevent memory leaks, as the string returned by a substring operation will be backed by the same byte array.


### 6. Functions and methods

* The decision whether to use a value or a pointer receiver should be made based on factors such as the type, whether it has to be mutated, whether it contains a field that can’t be copied, and how large the object is. When in doubt, use a pointer receiver.
* Using named result parameters can be an efficient way to improve the readability of a function/method, especially if multiple result parameters have the same type. In some cases, this approach can also be convenient because named result parameters are initialized to their zero value. But be cautious about potential side effects.
* When returning an interface, be cautious about returning not a nil pointer but an explicit nil value. Otherwise, unintended consequences may result because the caller will receive a non-nil value.
* Designing functions to receive io.Reader types instead of filenames improves the reusability of a function and makes testing easier.
* Passing a pointer to a defer function and wrapping a call inside a closure are two possible solutions to overcome the immediate evaluation of arguments and receivers.


### 7. Error management

* Using panic is an option to deal with errors in Go. However, it should only be used sparingly in unrecoverable conditions: for example, to signal a programmer error or when you fail to load a mandatory dependency.
* Wrapping an error allows you to mark an error and/or provide additional context. However, error wrapping creates potential coupling as it makes the source error available for the caller. If you want to prevent that, don’t use error wrapping.
* If you use Go 1.13 error wrapping with the %w directive and fmt.Errorf, comparing an error against a type or a value has to be done using errors.As or errors.Is, respectively. Otherwise, if the returned error you want to check is wrapped, it will fail the checks.
* To convey an expected error, use error sentinels (error values). An unexpected error should be a specific error type.
* In most situations, an error should be handled only once. Logging an error is handling an error. Therefore, you have to choose between logging or returning an error. In many cases, error wrapping is the solution as it allows you to provide additional context to an error and return the source error.
* Ignoring an error, whether during a function call or in a defer function, should be done explicitly using the blank identifier. Otherwise, future readers may be confused about whether it was intentional or a miss.
* In many cases, you shouldn’t ignore an error returned by a defer function. Either handle it directly or propagate it to the caller, depending on the context. If you want to ignore it, use the blank identifier.


### 8. Concurrency: Foundations

* Understanding the fundamental differences between concurrency and parallelism is a cornerstone of the Go developer’s knowledge. Concurrency is about structure, whereas parallelism is about execution.
* To be a proficient developer, you must acknowledge that concurrency isn’t always faster. Solutions involving parallelization of minimal workloads may not necessarily be faster than a sequential implementation. Benchmarking sequential versus concurrent solutions should be the way to validate assumptions.
* Being aware of goroutine interactions can also be helpful when deciding between channels and mutexes. In general, parallel goroutines require synchronization and hence mutexes. Conversely, concurrent goroutines generally require coordination and orchestration and hence channels.
* Being proficient in concurrency also means understanding that data races and race conditions are different concepts. Data races occur when multiple goroutines simultaneously access the same memory location and at least one of them is writing. Meanwhile, being data-race-free doesn’t necessarily mean deterministic execution. When a behavior depends on the sequence or the timing of events that can’t be controlled, this is a race condition.
* Understanding the Go memory model and the underlying guarantees in terms of ordering and synchronization is essential to prevent possible data races and/ or race conditions.
* When creating a certain number of goroutines, consider the workload type. Creating CPU-bound goroutines means bounding this number close to the GOMAXPROCS variable (based by default on the number of CPU cores on the host). Creating I/O-bound goroutines depends on other factors, such as the external system.
* Go contexts are also one of the cornerstones of concurrency in Go. A context allows you to carry a deadline, a cancellation signal, and/or a list of keys-values.


### 9. Concurrency: Practice

* Understanding the conditions when a context can be canceled should matter when propagating it: for example, an HTTP handler canceling the context when the response has been sent.
* Avoiding leaks means being mindful that whenever a goroutine is started, you should have a plan to stop it eventually.
* To avoid bugs with goroutines and loop variables, create local variables or call functions instead of closures.
* Understanding that select with multiple channels chooses the case randomly if multiple options are possible prevents making wrong assumptions that can lead to subtle concurrency bugs.
* Send notifications using a chan struct{} type.
* Using nil channels should be part of your concurrency toolset because it allows you to remove cases from select statements, for example.
* Carefully decide on the right channel type to use, given a problem. Only unbuffered channels provide strong synchronization guarantees.
* You should have a good reason to specify a channel size other than one for buffered channels.
* Being aware that string formatting may lead to calling existing functions means watching out for possible deadlocks and other data races.
* Calling append isn’t always data-race-free; hence, it shouldn’t be used concurrently on a shared slice.
* Remembering that slices and maps are pointers can prevent common data races.
* To accurately use sync.WaitGroup, call the Add method before spinning up goroutines.
* You can send repeated notifications to multiple goroutines with sync.Cond.
* You can synchronize a group of goroutines and handle errors and contexts with the errgroup package.
* sync types shouldn’t be copied.


### 10. The standard library

* Remain cautious with functions accepting a time.Duration. Even though passing an integer is allowed, strive to use the time API to prevent any possible confusion.
* Avoiding calls to time.After in repeated functions (such as loops or HTTP handlers) can avoid peak memory consumption. The resources created by time.After are released only when the timer expires.
* Be careful about using embedded fields in Go structs. Doing so may lead to sneaky bugs like an embedded time.Time field implementing the json .Marshaler interface, hence overriding the default marshaling behavior.
* When comparing two time.Time structs, recall that time.Time contains both a wall clock and a monotonic clock, and the comparison using the == operator is done on both clocks.
* To avoid wrong assumptions when you provide a map while unmarshaling JSON data, remember that numerics are converted to float64 by default.
* Call the Ping or PingContext method if you need to test your configuration and make sure a database is reachable.
* Configure the database connection parameters for production-grade applications.
* Using SQL prepared statements makes queries more efficient and more secure.
* Deal with nullable columns in tables using pointers or sql.NullXXX types.
* Call the Err method of *sql.Rows after row iterations to ensure that you haven’t missed an error while preparing the next row.
* Eventually close all structs implementing io.Closer to avoid possible leaks.
* To avoid unexpected behaviors in HTTP handler implementations, make sure you don’t miss the return statement if you want a handler to stop after http.Error.
* For production-grade applications, don’t use the default HTTP client and server implementations. These implementations are missing timeouts and behaviors that should be mandatory in production.

### 11. Testing

* Categorizing tests using build flags, environment variables, or short mode makes the testing process more efficient. You can create test categories using build flags or environment variables (for example, unit versus integration tests) and differentiate short- from long-running tests to decide which kinds of tests to execute.
* Enabling the -race flag is highly recommended when writing concurrent applications. Doing so allows you to catch potential data races that can lead to software bugs.
* Using the -parallel flag is an efficient way to speed up tests, especially longrunning ones.
* Use the -shuffle flag to help ensure that a test suite doesn’t rely on wrong assumptions that could hide bugs.
* Table-driven tests are an efficient way to group a set of similar tests to prevent code duplication and make future updates easier to handle.
* Avoid sleeps using synchronization to make a test less flaky and more robust. If synchronization isn’t possible, consider a retry approach.
* Understanding how to deal with functions using the time API is another way to make a test less flaky. You can use standard techniques such as handling the time as part of a hidden dependency or asking clients to provide it.
* The httptest package is helpful for dealing with HTTP applications. It provides a set of utilities to test both clients and servers.
* The iotest package helps write io.Reader and test that an application is tolerant to errors.
* Regarding benchmarks: – Use time methods to preserve the accuracy of a benchmark. – Increasing benchtime or using tools such as benchstat can be helpful when dealing with micro-benchmarks. – Be careful with the results of a micro-benchmark if the system that ends up running the application is different from the one running the micro-benchmark. – Make sure the function under test leads to a side effect, to prevent compiler optimizations from fooling you about the benchmark results. – To prevent the observer effect, force a benchmark to re-create the data used by a CPU-bound function.
* Use code coverage with the -coverprofile flag to quickly see which part of the code needs more attention.
* Place unit tests in a different package to enforce writing tests that focus on an exposed behavior, not internals.
* Handling errors using the *testing.T variable instead of the classic if err != nil makes code shorter and easier to read.
* You can use setup and teardown functions to configure a complex environment, such as in the case of integration tests.


### 12. Optimizations

* Understanding how to use CPU caches is important for optimizing CPU-bound applications because the L1 cache is about 50 to 100 times faster than the main memory.
* Being conscious of the cache line concept is critical to understanding how to organize data in data-intensive applications. A CPU doesn’t fetch memory word by word; instead, it usually copies a memory block to a 64-byte cache line. To get the most out of each individual cache line, enforce spatial locality.
* Making code predictable for the CPU can also be an efficient way to optimize certain functions. For example, a unit or constant stride is predictable for the CPU, but a non-unit stride (for example, a linked list) isn’t predictable.
* To avoid a critical stride, hence utilizing only a tiny portion of the cache, be aware that caches are partitioned.
* Knowing that lower levels of CPU caches aren’t shared across all the cores helps avoid performance-degrading patterns such as false sharing while writing concurrency code. Sharing memory is an illusion.
* Use instruction-level parallelism (ILP) to optimize specific parts of your code to allow a CPU to execute as many parallel instructions as possible. Identifying data hazards is one of the main steps.
* You can avoid common mistakes by remembering that in Go, basic types are aligned with their own size. For example, keep in mind that reorganizing the fields of a struct by size in descending order can lead to more compact structs (less memory allocation and potentially a better spatial locality).
* Understanding the fundamental differences between heap and stack should also be part of your core knowledge when optimizing a Go application. Stack allocations are almost free, whereas heap allocations are slower and rely on the GC to clean the memory.
* Reducing allocations is also an essential aspect of optimizing a Go application. This can be done in different ways, such as designing the API carefully to prevent sharing up, understanding the common Go compiler optimizations, and using sync.Pool.
* Use the fast-path inlining technique to efficiently reduce the amortized time to call a function.
* Rely on profiling and the execution tracer to understand how an application performs and the parts to optimize.
* Understanding how to tune the GC can lead to multiple benefits such as handling sudden load increases more efficiently.
* To help avoid CPU throttling when deployed in Docker and Kubernetes, keep in mind that Go isn’t CFS-aware.