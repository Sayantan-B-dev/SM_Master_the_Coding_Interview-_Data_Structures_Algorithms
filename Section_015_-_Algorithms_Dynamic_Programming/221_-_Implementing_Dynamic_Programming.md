# Memoized Fibonacci Implementation and Complexity Analysis

## 1. Introduction

The naive recursive implementation of the Fibonacci sequence exhibits exponential time complexity **O(2ⁿ)** due to repeated computation of identical subproblems. This document presents the application of dynamic programming via memoization to transform the algorithm into a linear-time **O(n)** solution. The implementation leverages closure-based caching in JavaScript, and a comparative analysis of computational effort and complexity is provided.

## 2. Implementation of Memoized Fibonacci

### 2.1 Closure-Based Memoization Pattern

To encapsulate the cache and prevent global namespace pollution, a factory function returns a memoized inner function. This pattern, known as a **closure**, ensures the cache persists across recursive calls without external exposure.

```javascript
/**
 * Fibonacci Master - Memoization Factory using Closure.
 * This function creates a memoized Fibonacci calculator.
 *
 * The outer function initializes a private cache object.
 * The returned inner function accesses this cache via closure.
 *
 * @returns {Function} A memoized Fibonacci function.
 */
function fibonacciMaster() {
    // The cache object (hash table) stores previously computed Fibonacci numbers.
    // Keys are the input 'n', values are F(n).
    const cache = {};

    /**
     * Inner recursive function that computes Fibonacci with memoization.
     *
     * @param {number} n - The zero-based index in the Fibonacci sequence.
     * @returns {number} The nth Fibonacci number.
     */
    function fib(n) {
        // Step 1: Check if the result for this 'n' is already in the cache.
        // The 'in' operator checks for property existence in the cache object.
        // This is an O(1) average-time operation.
        if (n in cache) {
            // Cache hit: Immediately return the stored value, avoiding recomputation.
            return cache[n];
        }

        // Step 2: Handle base cases (n = 0 or n = 1).
        // F(0) = 0, F(1) = 1.
        if (n < 2) {
            // Store base case results in the cache for consistency.
            cache[n] = n;
            return n;
        }

        // Step 3: Recursive step for n >= 2.
        // Compute F(n) = F(n-1) + F(n-2).
        // Since fib(n-1) and fib(n-2) are also memoized, each unique n is computed only once.
        const result = fib(n - 1) + fib(n - 2);

        // Step 4: Cache the newly computed result before returning.
        cache[n] = result;

        // Step 5: Return the computed value.
        return result;
    }

    // Return the inner function, closing over the cache.
    return fib;
}

// Instantiate the memoized Fibonacci function.
const fasterFib = fibonacciMaster();

// Example usage:
console.log('DP Fibonacci(10):', fasterFib(10)); // Output: 55
```

### 2.2 Explanation of Key Components

| Component | Purpose |
| :--- | :--- |
| `fibonacciMaster()` | Factory function that creates a closure containing the `cache` object. It returns the `fib` function. |
| `const cache = {}` | Private hash table that stores computed Fibonacci values. Persists across multiple invocations of `fasterFib`. |
| `if (n in cache)` | Cache lookup. Avoids redundant recursion by returning precomputed results. |
| Base case handling | `n < 2` returns `n`. These values are also cached for completeness. |
| Recursive call with caching | `fib(n-1) + fib(n-2)` is computed, and the result is stored in `cache[n]` before returning. |

## 3. Comparative Analysis of Computational Effort

### 3.1 Counting Function Calls

To empirically demonstrate the performance improvement, a counter variable tracks the number of times the recursive function is invoked. The following code integrates the counter into both the naive and memoized implementations.

```javascript
// Global counter for tracking function invocations.
let calculations = 0;

/**
 * Naive recursive Fibonacci with invocation counter.
 */
function fibonacciNaive(n) {
    calculations++; // Increment on every call.
    if (n < 2) {
        return n;
    }
    return fibonacciNaive(n - 1) + fibonacciNaive(n - 2);
}

/**
 * Memoized Fibonacci factory with internal counter.
 */
function fibonacciMasterWithCounter() {
    const cache = {};
    function fib(n) {
        calculations++; // Increment on every call.
        if (n in cache) {
            return cache[n];
        }
        if (n < 2) {
            cache[n] = n;
            return n;
        }
        const result = fib(n - 1) + fib(n - 2);
        cache[n] = result;
        return result;
    }
    return fib;
}

// Example: Compare function calls for n = 10
calculations = 0;
console.log('Naive F(10):', fibonacciNaive(10));
console.log('Naive Calculations:', calculations); // Output: 177

calculations = 0;
const memoFib = fibonacciMasterWithCounter();
console.log('Memoized F(10):', memoFib(10));
console.log('Memoized Calculations:', calculations); // Output: 19
```

### 3.2 Empirical Observations

The table below summarizes the number of function calls for various inputs.

| n | Naive Recursive Calls | Memoized Recursive Calls |
|---|-----------------------|--------------------------|
| 10 | 177 | 19 |
| 20 | 21,891 | 39 |
| 30 | 2,692,537 | 59 |
| 35 | ~29.8 million | 69 |
| 50 | Would crash browser | 99 |
| 100 | Uncomputable | 199 |

**Interpretation:**
- The naive approach exhibits exponential growth: calls ≈ **F(n+2) - 1**.
- The memoized version computes each **F(k)** for **k = 0..n** exactly once, resulting in **2n - 1** calls (or approximately **2n**). For **n=100**, only **199** calls are made.
- The memoized function can compute **F(100)** instantaneously, whereas the naive version would require billions of calls.

## 4. Complexity Analysis

### 4.1 Time Complexity

| Implementation | Time Complexity | Explanation |
| :--- | :--- | :--- |
| **Naive Recursive** | **O(2ⁿ)** | Each call spawns two more calls, creating a binary tree of depth **n**. Number of nodes is exponential. |
| **Memoized (Top-Down DP)** | **O(n)** | Each unique subproblem **F(k)** is solved once. With **n** subproblems, and O(1) cache access, total time is linear. |

### 4.2 Space Complexity

| Implementation | Space Complexity | Explanation |
| :--- | :--- | :--- |
| **Naive Recursive** | **O(n)** | Maximum depth of recursion stack is **n**. No additional data structures. |
| **Memoized (Top-Down DP)** | **O(n)** | Recursion stack depth remains **n**. Additionally, the cache stores **n+1** entries, each O(1). Total space remains linear. |

### 4.3 Trade-off Discussion

Memoization introduces a space overhead due to the cache. However, the space required is linear (**O(n)**), which is a modest cost compared to the exponential time savings. In most practical scenarios, trading a linear increase in memory for a reduction from exponential to linear time is highly advantageous.

## 5. Execution Flow Diagram

The following simplified Mermaid diagram illustrates the control flow of the memoized Fibonacci function for **n=5**.

```mermaid
graph TD
    A[fib(5)] --> B{5 in cache?};
    B -- No --> C[Compute fib(4) + fib(3)];
    C --> D[fib(4)];
    D --> E{4 in cache?};
    E -- No --> F[Compute fib(3) + fib(2)];
    F --> G[fib(3)];
    G --> H{3 in cache?};
    H -- No --> I[Compute fib(2) + fib(1)];
    I --> J[fib(2)];
    J --> K{2 in cache?};
    K -- No --> L[Compute fib(1) + fib(0)];
    L --> M[fib(1) -> 1 cached];
    L --> N[fib(0) -> 0 cached];
    J --> O[Store fib(2)=1 in cache];
    G --> P[fib(1) -> cache hit];
    I --> Q[Store fib(3)=2 in cache];
    F --> R[fib(2) -> cache hit];
    D --> S[Store fib(4)=3 in cache];
    C --> T[fib(3) -> cache hit];
    A --> U[Store fib(5)=5 in cache];
    U --> V[Return 5];
```

**Note:** The diagram highlights cache hits that bypass redundant sub-tree evaluations.

## 6. Practical Considerations

### 6.1 Handling Large Inputs

The memoized function can compute **F(1000)** without performance degradation, though JavaScript's number type may overflow for extremely large values (Fibonacci numbers exceed `Number.MAX_SAFE_INTEGER` beyond **F(79)**). For accurate large-number computation, `BigInt` should be used.

```javascript
function fibonacciMasterBigInt() {
    const cache = {};
    function fib(n) {
        if (n in cache) return cache[n];
        if (n < 2) {
            cache[n] = BigInt(n);
            return cache[n];
        }
        const result = fib(n - 1) + fib(n - 2);
        cache[n] = result;
        return result;
    }
    return fib;
}

const bigFib = fibonacciMasterBigInt();
console.log(bigFib(100).toString()); // Outputs 354224848179261915075
```

### 6.2 Bottom-Up Approach (Tabulation)

While memoization (top-down) is intuitive, the same **O(n)** time complexity can be achieved iteratively with **O(1)** space using tabulation.

```javascript
function fibonacciTabulation(n) {
    if (n < 2) return n;
    let prev = 0, curr = 1;
    for (let i = 2; i <= n; i++) {
        [prev, curr] = [curr, prev + curr];
    }
    return curr;
}
```

This approach eliminates recursion and cache overhead, demonstrating that dynamic programming can be applied in multiple forms.

## 7. Summary

- **Memoization** transforms the exponential-time naive Fibonacci into a linear-time solution.
- The **closure-based memoization pattern** encapsulates the cache, preventing global scope pollution and ensuring persistence.
- Empirical comparison shows a reduction from **177 calls** to **19 calls** for **n=10**, and from billions to **199 calls** for **n=100**.
- **Time complexity** improves from **O(2ⁿ)** to **O(n)**.
- **Space complexity** remains **O(n)** due to recursion stack and cache, representing a favorable trade-off.
- Dynamic programming is a powerful optimization technique that is both accessible and essential for efficient algorithm design.

> **Key Insight:** The core of dynamic programming lies in recognizing overlapping subproblems and caching their solutions. The Fibonacci sequence provides a clear and compelling illustration of this principle, demonstrating that even simple recursive functions can be dramatically improved with memoization.