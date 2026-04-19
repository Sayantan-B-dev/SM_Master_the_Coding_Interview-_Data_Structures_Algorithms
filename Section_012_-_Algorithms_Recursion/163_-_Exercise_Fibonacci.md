# Fibonacci Sequence: Iterative and Recursive Computation

## 1. Introduction

The Fibonacci sequence is a classic integer series frequently used to illustrate fundamental programming concepts, particularly recursion and dynamic programming. Named after the Italian mathematician Leonardo of Pisa (Fibonacci), the sequence appears in various natural phenomena, algorithmic analysis, and mathematical models.

Each number in the Fibonacci sequence is the sum of the two preceding numbers. The sequence commonly begins with `0` and `1`, though some definitions start with `1` and `1`. The mathematical recurrence relation is defined as:

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)  for n ≥ 2
```

**First Few Terms:**

| Index (n) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
|-----------|---|---|---|---|---|---|---|---|---|----|
| F(n)      | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13| 21 |

## 2. Problem Statement

Given a non-negative integer `n`, write a function that returns the Fibonacci number at index `n`. For example:

- Input: `2` → Output: `1`
- Input: `8` → Output: `21`

Two primary implementation strategies are examined:

- **Iterative Approach**: Utilizes a loop to compute subsequent terms sequentially.
- **Recursive Approach**: Directly translates the mathematical recurrence into a function that calls itself.

## 3. Iterative Implementation

The iterative method builds the Fibonacci sequence from the base cases upward, storing only the two most recent values at any time. This approach avoids the overhead of recursive function calls and has optimal space efficiency.

### 3.1 Algorithm Description

1. Handle edge cases where `n` is `0` or `1`, returning `0` or `1` respectively.
2. Initialize two variables to hold the values of `F(0)` and `F(1)`.
3. Iterate from `2` up to `n`.
4. In each iteration, compute the next Fibonacci number as the sum of the two preceding numbers.
5. Update the two variables to shift forward.
6. After the loop completes, return the most recently computed value.

### 3.2 JavaScript Code

```javascript
/**
 * Computes the nth Fibonacci number iteratively.
 * @param {number} n - The index (non-negative integer) in the Fibonacci sequence.
 * @returns {number} The Fibonacci number at index n.
 */
function fibonacciIterative(n) {
    // Base cases
    if (n === 0) return 0;
    if (n === 1) return 1;

    // Initialize first two Fibonacci numbers
    let prevPrev = 0; // F(0)
    let prev = 1;     // F(1)
    let current;

    // Iteratively compute F(2) through F(n)
    for (let i = 2; i <= n; i++) {
        current = prevPrev + prev; // F(i) = F(i-2) + F(i-1)
        prevPrev = prev;           // Shift: F(i-2) becomes previous F(i-1)
        prev = current;            // Shift: F(i-1) becomes current F(i)
    }

    return current;
}

// Example usage
console.log(fibonacciIterative(2));  // Output: 1
console.log(fibonacciIterative(8));  // Output: 21
console.log(fibonacciIterative(10)); // Output: 55
```

### 3.3 Complexity Analysis

- **Time Complexity**: **O(n)** — The loop executes `n-1` times, each iteration performing constant-time operations.
- **Space Complexity**: **O(1)** — Only a fixed number of variables are maintained regardless of input size.

## 4. Recursive Implementation

The recursive solution expresses the Fibonacci function directly in terms of its own definition. While conceptually elegant, naive recursion exhibits significant performance drawbacks due to redundant calculations.

### 4.1 Algorithm Description

- **Base Cases**: Return `n` when `n` is `0` or `1`.
- **Recursive Case**: Return `fibonacciRecursive(n-1) + fibonacciRecursive(n-2)`.

### 4.2 JavaScript Code

```javascript
/**
 * Computes the nth Fibonacci number using naive recursion.
 * @param {number} n - The index (non-negative integer) in the Fibonacci sequence.
 * @returns {number} The Fibonacci number at index n.
 */
function fibonacciRecursive(n) {
    // Base cases
    if (n === 0) return 0;
    if (n === 1) return 1;

    // Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Example usage
console.log(fibonacciRecursive(2));  // Output: 1
console.log(fibonacciRecursive(8));  // Output: 21
```

### 4.3 Execution Flow and Recursion Tree

The recursive computation for `n = 5` generates the following call tree, illustrating the overlapping subproblems:

```
                            fibonacciRecursive(5)
                           /                    \
              fibonacciRecursive(4)       fibonacciRecursive(3)
             /            \                 /            \
fibonacciRecursive(3) fibonacciRecursive(2) fibonacciRecursive(2) fibonacciRecursive(1)
     /        \           /        \           /        \
fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
 /    \
fib(1) fib(0)
```

Many subproblems (e.g., `fib(2)`, `fib(3)`) are recomputed multiple times, leading to exponential growth in function calls.

### 4.4 Complexity Analysis

- **Time Complexity**: **O(2ⁿ)** — Each call spawns two additional calls, resulting in exponential growth. The exact number of calls is proportional to the Fibonacci number itself.
- **Space Complexity**: **O(n)** — The maximum depth of the call stack is `n`.

## 5. Comparison of Approaches

| Aspect                | Iterative                     | Recursive (Naive)               |
|-----------------------|-------------------------------|---------------------------------|
| **Time Complexity**   | O(n)                          | O(2ⁿ) (exponential)             |
| **Space Complexity**  | O(1)                          | O(n) (call stack)               |
| **Ease of Implementation** | Straightforward loop logic | Direct translation of definition |
| **Scalability**       | Efficient for large `n`       | Impractical for `n > 40`        |
| **Code Readability**  | Explicit state management     | Highly expressive and concise   |

## 6. Optimized Recursion with Memoization

The inefficiency of naive recursion can be mitigated using **memoization**, a dynamic programming technique that caches previously computed results. This reduces time complexity to O(n) while preserving the recursive structure.

```javascript
/**
 * Computes Fibonacci with memoization for efficient recursion.
 * @param {number} n - The index in Fibonacci sequence.
 * @param {Object} cache - Memoization cache (optional, initialized empty).
 * @returns {number} The Fibonacci number at index n.
 */
function fibonacciMemoized(n, cache = {}) {
    if (n in cache) {
        return cache[n];
    }
    if (n === 0) return 0;
    if (n === 1) return 1;
    
    cache[n] = fibonacciMemoized(n - 1, cache) + fibonacciMemoized(n - 2, cache);
    return cache[n];
}
```

- **Time Complexity**: O(n) — Each `F(k)` is computed once.
- **Space Complexity**: O(n) — Cache stores up to `n` entries plus call stack depth.

## 7. Summary

The Fibonacci sequence provides a compelling case study in algorithmic design trade-offs. The iterative approach delivers optimal performance with minimal memory usage, making it the preferred choice for production environments. The naive recursive implementation, while conceptually appealing, suffers from exponential time complexity and is unsuitable for large inputs. Memoization offers a balanced alternative, retaining the elegance of recursion while achieving linear time efficiency. Understanding these variations deepens one's grasp of recursion, iteration, and performance optimization in software development.