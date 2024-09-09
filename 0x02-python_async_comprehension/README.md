
### 0x02. Python - Async Comprehension


---

## Resources
### Read or Watch:
- **PEP 530** – Asynchronous Comprehensions
- **What’s New in Python**: Asynchronous Comprehensions / Generators
- **Type-hints for generators**

---

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

---

---

## Tasks


### 0. Async Generator
Write a coroutine called `async_generator` that loops 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10.

### 1. Async Comprehensions
Write a coroutine called `async_comprehension` that collects 10 random numbers from the `async_generator` using an async comprehension, then returns the list of numbers.

### 2. Run time for four parallel comprehensions
Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. Measure and return the total runtime.
