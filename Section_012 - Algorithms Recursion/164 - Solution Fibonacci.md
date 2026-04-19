# Fibonacci Sequence: Implementation Strategies and Complexity Analysis

## 1. Introduction

The Fibonacci sequence is a fundamental integer series defined by a recurrence relation wherein each term is the sum of the two preceding terms. This sequence finds applications in mathematics, computer science, and nature. In algorithmic studies, computing Fibonacci numbers serves as a canonical example to illustrate recursion, iteration, and the associated performance trade-offs.

## 2. Mathematical Definition

The Fibonacci sequence is formally defined as follows:

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)   for n ≥ 2
```

The initial terms of the sequence are:

| n   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
|-----|---|---|---|---|---|---|---|---|---|----|
| F(n)| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13| 21 |

## 3. Problem Statement

Given a non-negative integer `n`, design a function that returns the `n`-th Fibonacci number, `F(n)`. Two distinct approaches are examined:

- **Recursive Implementation**: A direct translation of the mathematical recurrence.
- **Iterative Implementation**: A sequential computation using a loop construct.

## 4. Recursive Implementation

The recursive solution mirrors the definition precisely. It expresses the problem in terms of smaller subproblems until a base case is reached.

### 4.1 Algorithm Description

- **Base Cases**: 
  - If `n === 0`, return `0`.
  - If `n === 1`, return `1`.
- **Recursive Case**: 
  - Return `fibonacciRecursive(n-1) + fibonacciRecursive(n-2)`.

### 4.2 JavaScript Code

```javascript
/**
 * Computes the nth Fibonacci number using naive recursion.
 * @param {number} n - Index in the Fibonacci sequence (non-negative integer).
 * @returns {number} The Fibonacci number at index n.
 */
function fibonacciRecursive(n) {
    // Base cases: F(0) = 0, F(1) = 1
    if (n < 2) {
        return n;
    }
    // Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Example usage
console.log(fibonacciRecursive(3)); // Output: 2
console.log(fibonacciRecursive(8)); // Output: 21
```

### 4.3 Recursion Tree and Redundant Computation

For `n = 7`, the recursive calls form a binary tree structure:

```mermaid
graph TD
    A[fib(7)] --> B[fib(6)]
    A --> C[fib(5)]
    B --> D[fib(5)]
    B --> E[fib(4)]
    C --> F[fib(4)]
    C --> G[fib(3)]
    D --> H[fib(4)]
    D --> I[fib(3)]
```

The tree expands exponentially, and many subproblems (e.g., `fib(5)`, `fib(4)`, `fib(3)`) are recomputed multiple times. This redundancy leads to significant performance degradation as `n` increases.

### 4.4 Complexity Analysis

- **Time Complexity**: **O(2ⁿ)** — Each call generates two recursive calls, resulting in exponential growth.
- **Space Complexity**: **O(n)** — Maximum depth of the call stack equals `n`.

Due to exponential time, naive recursion becomes impractical for even moderately large values (e.g., `n > 40`).

## 5. Iterative Implementation

The iterative approach computes Fibonacci numbers sequentially, storing only the two most recent values to minimize memory usage.

### 5.1 Algorithm Description

1. Initialize an array `result` with the first two Fibonacci numbers: `[0, 1]`.
2. If `n` is `0` or `1`, return `result[n]`.
3. Iterate from `i = 2` to `n` (inclusive).
4. Compute `next = result[i-2] + result[i-1]` and append to the array.
5. Return the last element of the array.

### 5.2 JavaScript Code

```javascript
/**
 * Computes the nth Fibonacci number iteratively.
 * @param {number} n - Index in the Fibonacci sequence (non-negative integer).
 * @returns {number} The Fibonacci number at index n.
 */
function fibonacciIterative(n) {
    // Initialize array with base cases
    const result = [0, 1];
    
    // Build sequence up to index n
    for (let i = 2; i <= n; i++) {
        result.push(result[i - 2] + result[i - 1]);
    }
    
    // Return the nth element
    return result[n];
}

// Example usage
console.log(fibonacciIterative(8));  // Output: 21
console.log(fibonacciIterative(43)); // Output: 433494437 (computed instantly)
```

### 5.3 Complexity Analysis

- **Time Complexity**: **O(n)** — A single loop iterates approximately `n-1` times.
- **Space Complexity**: **O(n)** — The array stores all computed Fibonacci numbers up to `n`. This can be optimized to O(1) by using two variables instead of an array.

### 5.4 Space-Optimized Iterative Version

```javascript
function fibonacciIterativeOptimized(n) {
    if (n < 2) return n;
    
    let prevPrev = 0; // F(0)
    let prev = 1;     // F(1)
    let current;
    
    for (let i = 2; i <= n; i++) {
        current = prevPrev + prev;
        prevPrev = prev;
        prev = current;
    }
    return current;
}
```

- **Space Complexity**: **O(1)** — Only three variables are maintained.

## 6. Comparative Analysis

| Metric                | Recursive (Naive)              | Iterative (Array)              | Iterative (Optimized)          |
|-----------------------|--------------------------------|--------------------------------|--------------------------------|
| Time Complexity       | O(2ⁿ)                          | O(n)                           | O(n)                           |
| Space Complexity      | O(n) (call stack)              | O(n) (array)                   | O(1)                           |
| Readability           | Direct mathematical mapping    | Explicit loop logic            | Clear, memory-efficient        |
| Scalability           | Impractical for `n > 40`       | Suitable for large `n`         | Excellent for large `n`        |
| Risk of Stack Overflow| High for moderate `n`          | None                           | None                           |

## 7. Performance Observation

The exponential time complexity of naive recursion becomes evident with empirical testing. For `n = 43`, the recursive function may take several seconds to complete in a browser environment, whereas the iterative version returns the result almost instantaneously.

```javascript
// Timing comparison (conceptual)
console.time('Recursive');
fibonacciRecursive(43);
console.timeEnd('Recursive'); // Output: Recursive: ~5000ms (varies by system)

console.time('Iterative');
fibonacciIterative(43);
console.timeEnd('Iterative'); // Output: Iterative: < 1ms
```

## 8. Improving Recursive Performance

The inefficiency of naive recursion can be mitigated using **memoization**, a dynamic programming technique that caches computed results. This optimization reduces time complexity to O(n) while preserving the recursive structure.

```javascript
function fibonacciMemoized(n, cache = {}) {
    if (n in cache) return cache[n];
    if (n < 2) return n;
    
    cache[n] = fibonacciMemoized(n - 1, cache) + fibonacciMemoized(n - 2, cache);
    return cache[n];
}
```

## 9. Summary

The Fibonacci sequence exemplifies the trade-offs inherent in algorithmic design. The naive recursive solution offers elegant simplicity but suffers from exponential time complexity due to redundant calculations. The iterative approach provides linear time performance and constant space efficiency, making it the preferred choice for production code. Understanding these differences underscores the importance of selecting appropriate algorithmic strategies based on problem constraints and performance requirements. Furthermore, techniques such as memoization bridge the gap between recursive expressiveness and iterative efficiency.