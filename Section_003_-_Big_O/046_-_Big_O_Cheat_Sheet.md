# Big O Notation: Comprehensive Reference and Cheat Sheet

## Abstract

This document serves as a consolidated reference guide for Big O asymptotic analysis, summarizing the principal complexity classes, the fundamental rules for simplification, and the primary factors contributing to time and space complexity in algorithmic evaluation. The content is structured to facilitate rapid review for examination preparation, technical interviews, and long-term professional reference. The material aligns with standard computer science curricula and provides a succinct yet comprehensive overview of the topic.

---

## 1. Principal Big O Complexity Classes

The following table enumerates the standard Big O notations encountered in algorithmic analysis, arranged in order of increasing growth rate. Each entry includes a brief description and a characteristic code pattern or algorithmic scenario.

| Notation | Name | Description | Typical Pattern / Context |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constant Time | Execution time remains fixed irrespective of input size. | No loops; direct array index access; hash table lookup (average case). |
| **O(log N)** | Logarithmic Time | Execution time increases logarithmically with input size. | Binary search on sorted data; operations on balanced binary search trees. |
| **O(n)** | Linear Time | Execution time grows proportionally to input size. | Single `for` or `while` loops iterating over all `n` elements. |
| **O(n log n)** | Linearithmic Time | Execution time is a product of linear and logarithmic factors. | Efficient sorting algorithms (Merge Sort, Quick Sort average case, Heap Sort). |
| **O(n²)** | Quadratic Time | Execution time grows proportionally to the square of input size. | Nested loops where each element is compared to every other element; bubble sort. |
| **O(2ⁿ)** | Exponential Time | Execution time doubles with each additional input element. | Recursive algorithms that solve subproblems of size `N-1` (e.g., naive Fibonacci). |
| **O(n!)** | Factorial Time | Execution time grows factorially; intractable for non-trivial `n`. | Permutation generation; brute-force traveling salesman problem. |

### 1.1 Important Clarifications

- **Iterating through half a collection:** An algorithm that traverses exactly half of the input elements (e.g., `n/2` iterations) is still classified as **O(n)**. The constant factor `1/2` is discarded per simplification Rule 2.
- **Two separate input collections:** When an algorithm processes two distinct arrays or collections independently, the sizes are denoted by separate variables.
    - **Sequential processing:** Complexity is **O(a + b)**.
    - **Nested processing:** Complexity is **O(a * b)**.

---

## 2. Fundamental Rules for Big O Simplification

The following four rules constitute the standard methodology for deriving simplified, canonical Big O expressions. Adherence to these rules ensures consistency and clarity in complexity analysis.

### Rule 1: Always Consider the Worst Case
Big O notation describes the **upper bound** on the algorithm's runtime. Analysis must be based on the input configuration that results in the maximum number of operations. Optimizations such as early loop termination (`break`) improve average performance but do not alter the worst-case asymptotic bound.

### Rule 2: Remove Constants
Constant additive terms and constant multiplicative coefficients are discarded. As input size `n` approaches infinity, the impact of constants on the growth rate becomes negligible.
- **Example:** `O(2n + 100)` simplifies to **O(n)**.
- **Example:** `O(n/2)` simplifies to **O(n)**.

### Rule 3: Different Inputs Require Different Variables
When a function accepts multiple independent input parameters, the size of each distinct input must be represented by a separate variable in the Big O expression. Collapsing distinct inputs into a single `n` is erroneous.
- **Sequential Steps (Addition):** `O(a + b)`
- **Nested Steps (Multiplication):** `O(a * b)`

> **Mnemonic:** Use **addition (+)** for steps that occur sequentially (same indentation level). Use **multiplication (*)** for steps that are nested (deeper indentation level).

### Rule 4: Drop Non-Dominant Terms
When a complexity expression comprises multiple terms with different growth rates, retain only the term with the **highest order of growth**. Lower-order terms become statistically insignificant as `n` scales.
- **Example:** `O(n + n²)` simplifies to **O(n²)**.
- **Example:** `O(x² + 3x + 1000 + x/2)` simplifies to **O(x²)**.

---

## 3. Factors Contributing to Time Complexity

Time complexity quantifies the number of elementary operations executed by an algorithm as a function of input size. The following constructs and operations contribute to the overall time cost.

| Factor | Description |
| :--- | :--- |
| **Operations** | Arithmetic calculations (`+`, `-`, `*`, `/`), variable assignments, and increment/decrement operations. |
| **Comparisons** | Logical evaluations (`<`, `>`, `==`, `===`, `<=`, `>=`). |
| **Looping** | Iterative constructs (`for`, `while`, `do-while`). The number of iterations directly influences complexity. |
| **Function Calls** | Invocation of external functions or recursive calls. The cost of the called function must be factored into the analysis. |

---

## 4. Factors Contributing to Space Complexity

Space complexity quantifies the amount of auxiliary memory (beyond the input data) required by an algorithm. The following elements consume memory and contribute to the space complexity assessment.

| Factor | Description |
| :--- | :--- |
| **Variables** | Primitive data types, object references, and temporary storage declared within the function. |
| **Data Structures** | Additional arrays, lists, sets, maps, or trees created during algorithm execution. |
| **Function Call Allocations** | Memory allocated on the call stack for recursive function calls or nested function invocations. Each stack frame consumes memory. |

---

## 5. Contextual Notes on Unfamiliar Notations

The complexities **O(log N)**, **O(n log n)**, **O(2ⁿ)**, and **O(n!)** are introduced in this reference but are examined in detail within subsequent sections of the course that address specific data structures and algorithms.

- **O(log N):** Typically associated with **searching algorithms** on ordered data structures (e.g., Binary Search).
- **O(n log n):** Commonly encountered in **sorting algorithms** (e.g., Merge Sort, Quick Sort).
- **O(2ⁿ):** Characteristic of certain **recursive algorithms** that solve problems by branching into multiple subproblems (e.g., recursive calculation of Fibonacci numbers).
- **O(n!):** Arises in algorithms that generate all **permutations** of a set.

The foundational complexities—**O(1)**, **O(n)**, and **O(n²)**—have been thoroughly examined in preceding sections. The remaining notations will be contextualized and applied as the course progresses into specialized topics.

---

## 6. Conclusion

This cheat sheet encapsulates the essential knowledge required for performing Big O analysis in both academic and professional settings. Mastery of the seven principal complexity classes, the four simplification rules, and the sources of time and space complexity equips the software engineer with the analytical tools necessary to design scalable, efficient algorithms. The reference is intended for repeated consultation and serves as a cornerstone for the more advanced topics in data structures and algorithmic strategy that follow.