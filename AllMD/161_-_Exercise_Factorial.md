# Factorial Computation: Iterative and Recursive Approaches

## 1. Introduction

The factorial function is a fundamental mathematical operation frequently used to illustrate algorithmic concepts, particularly recursion. Computing the factorial of a non-negative integer serves as an instructive exercise in comparing iterative and recursive problem-solving strategies. Both approaches yield identical results but differ in implementation structure and underlying execution mechanics.

## 2. Mathematical Definition of Factorial

The factorial of a non-negative integer `n`, denoted as `n!`, is the product of all positive integers less than or equal to `n`. By convention, the factorial of zero is defined as `1`.

**Formal Definition:**

```
n! = 1                  if n = 0
n! = n × (n-1) × ... × 1   if n > 0
```

**Examples:**

- `5! = 5 × 4 × 3 × 2 × 1 = 120`
- `6! = 6 × 5 × 4 × 3 × 2 × 1 = 720`
- `0! = 1`

### 2.1 Recursive Nature of Factorial

The factorial function exhibits a natural recursive structure. Observe that:

```
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1 × 0!
0! = 1
```

Generalizing this pattern yields the recurrence relation:

```
n! = n × (n-1)!   for n > 0
0! = 1            (base case)
```

This self-referential definition makes factorial an ideal candidate for recursive implementation.

## 3. Iterative Approach

The iterative method computes the factorial using a loop construct to accumulate the product. It avoids function call overhead and stack memory consumption associated with recursion.

### 3.1 Algorithm Description

1. Initialize a result variable to `1`.
2. Iterate from `2` up to `n` (inclusive).
3. Multiply the result by the current iteration value.
4. Return the final product.

### 3.2 Implementation in JavaScript

```javascript
/**
 * Computes the factorial of a non-negative integer using iteration.
 * @param {number} n - The non-negative integer input.
 * @returns {number} The factorial of n.
 */
function factorialIterative(n) {
    // Handle negative input (optional, based on requirements)
    if (n < 0) {
        throw new Error('Factorial is not defined for negative numbers');
    }
    
    let result = 1;
    
    // Loop from 2 to n (inclusive); 0! and 1! both yield 1
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    
    return result;
}

// Example usage
console.log(factorialIterative(5)); // Output: 120
console.log(factorialIterative(0)); // Output: 1
```

### 3.3 Complexity Analysis

- **Time Complexity**: O(n) — The loop executes `n-1` multiplications.
- **Space Complexity**: O(1) — Only a constant amount of memory is used.

## 4. Recursive Approach

The recursive solution mirrors the mathematical recurrence relation. The function calls itself with a reduced argument until the base case is encountered.

### 4.1 Identifying Base Case and Recursive Case

Following the three rules of recursion:

| Rule | Application to Factorial |
|------|--------------------------|
| **Base Case** | When `n` equals `0`, return `1`. |
| **Recursive Case** | For `n > 0`, return `n * factorial(n-1)`. |
| **Progress and Return** | Each call reduces `n` by `1`, guaranteeing eventual termination. Both cases return a value. |

### 4.2 Implementation in JavaScript

```javascript
/**
 * Computes the factorial of a non-negative integer using recursion.
 * @param {number} n - The non-negative integer input.
 * @returns {number} The factorial of n.
 */
function factorialRecursive(n) {
    // Input validation
    if (n < 0) {
        throw new Error('Factorial is not defined for negative numbers');
    }
    
    // Base Case: 0! = 1
    if (n === 0) {
        return 1;
    }
    
    // Recursive Case: n! = n * (n-1)!
    return n * factorialRecursive(n - 1);
}

// Example usage
console.log(factorialRecursive(5)); // Output: 120
console.log(factorialRecursive(0)); // Output: 1
```

### 4.3 Execution Flow and Call Stack Behavior

The recursive computation for `factorialRecursive(5)` unfolds as follows:

```mermaid
graph TD
    A[factorial(5)] --> B[5 * factorial(4)]
    B --> C[4 * factorial(3)]
    C --> D[3 * factorial(2)]
    D --> E[2 * factorial(1)]
    E --> F[1 * factorial(0)]
    F --> G[return 1]
    G --> H[1 * 1 = 1]
    H --> I[2 * 1 = 2]
    I --> J[3 * 2 = 6]
    J --> K[4 * 6 = 24]
    K --> L[5 * 24 = 120]
    L --> M[Return 120]
```

Each recursive call pushes a new stack frame. Upon reaching the base case (`n = 0`), frames unwind, and multiplication operations resolve from the innermost call outward.

### 4.4 Complexity Analysis

- **Time Complexity**: O(n) — `n` recursive calls are made, each performing a constant-time multiplication.
- **Space Complexity**: O(n) — The call stack grows linearly with `n` due to the pending multiplications.

## 5. Comparison of Iterative and Recursive Approaches

| Aspect | Iterative | Recursive |
|--------|-----------|-----------|
| **Code Clarity** | Straightforward loop logic | Direct mapping to mathematical definition |
| **Memory Usage** | Constant (O(1)) | Linear stack space (O(n)) |
| **Risk of Stack Overflow** | None | Possible for very large `n` |
| **Performance** | Slightly faster (no function call overhead) | Slightly slower due to call overhead |
| **Conceptual Alignment** | Procedural | Declarative, self-referential |

For factorial specifically, the iterative solution is generally preferred in production code due to its memory efficiency. However, the recursive version serves as an excellent pedagogical tool for understanding recursion fundamentals.

## 6. Summary

The factorial function provides a clear and concise demonstration of both iterative and recursive algorithmic design. The iterative approach leverages a simple loop to accumulate the product, while the recursive approach expresses the solution in terms of a smaller instance of the same problem. Mastery of these two paradigms is essential for tackling a wide range of computational problems, from basic arithmetic operations to complex tree and graph traversals.