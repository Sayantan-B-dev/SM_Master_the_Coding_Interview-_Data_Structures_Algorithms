# Factorial Computation: Implementation and Analysis

## 1. Introduction

The factorial of a non-negative integer `n`, denoted as `n!`, is defined as the product of all positive integers from `1` to `n`. By convention, `0! = 1`. Computing the factorial serves as a classic exercise to demonstrate both iterative and recursive algorithmic strategies. This document presents the implementation details of both approaches, along with a comparative analysis of their time complexity.

## 2. Iterative Implementation

The iterative method uses a loop construct to accumulate the product of consecutive integers. A common optimization involves recognizing that `1! = 1` and `2! = 2`, allowing the loop to begin from `2` and bypass trivial cases.

### 2.1 Algorithm Steps

1. Handle edge cases where `n` equals `1` or `2` directly.
2. Initialize a variable `answer` to `1`.
3. Iterate from `i = 2` to `n` (inclusive).
4. Multiply `answer` by `i` in each iteration.
5. Return the final value of `answer`.

### 2.2 JavaScript Code

```javascript
/**
 * Computes factorial iteratively.
 * @param {number} number - A non-negative integer.
 * @returns {number} The factorial of the input number.
 */
function findFactorialIterative(number) {
    // Handle base cases to avoid unnecessary looping
    if (number === 0 || number === 1) {
        return 1;
    }
    if (number === 2) {
        return 2;
    }
    
    let answer = 1;
    
    // Start loop from 2 because multiplying by 1 has no effect
    for (let i = 2; i <= number; i++) {
        answer = answer * i;
    }
    
    return answer;
}

// Example usage
console.log(findFactorialIterative(5)); // Output: 120
console.log(findFactorialIterative(2)); // Output: 2
```

### 2.3 Explanation of Loop Initialization

Starting the loop counter at `2` is a minor optimization. Since multiplying by `1` does not change the product, iterations for `i = 0` and `i = 1` are redundant. The conditional checks at the function entry handle `0`, `1`, and `2` explicitly, ensuring correct results without entering the loop for these values.

## 3. Recursive Implementation

The recursive solution mirrors the mathematical recurrence relation: `n! = n × (n-1)!` for `n > 1`, with a base case that terminates the recursion.

### 3.1 Base Case and Recursive Case

- **Base Case**: When `number` equals `2` (or optionally `0` or `1`), return `2` (or `1`). This condition stops further recursive calls.
- **Recursive Case**: For `number > 2`, return `number * findFactorialRecursive(number - 1)`.

### 3.2 JavaScript Code

```javascript
/**
 * Computes factorial recursively.
 * @param {number} number - A non-negative integer.
 * @returns {number} The factorial of the input number.
 */
function findFactorialRecursive(number) {
    // Base case: terminate recursion at 2 (or lower)
    if (number === 2) {
        return 2;
    }
    // Additional base cases for completeness
    if (number === 0 || number === 1) {
        return 1;
    }
    
    // Recursive case: n! = n * (n-1)!
    return number * findFactorialRecursive(number - 1);
}

// Example usage
console.log(findFactorialRecursive(5)); // Output: 120
```

### 3.3 Execution Flow

For an input of `5`, the recursive calls proceed as follows:

```
findFactorialRecursive(5)
    → 5 * findFactorialRecursive(4)
        → 4 * findFactorialRecursive(3)
            → 3 * findFactorialRecursive(2)
                → returns 2 (base case)
            → 3 * 2 = 6
        → 4 * 6 = 24
    → 5 * 24 = 120
```

```mermaid
graph TD
    A[factorial(5)] --> B[5 * factorial(4)]
    B --> C[4 * factorial(3)]
    C --> D[3 * factorial(2)]
    D --> E[return 2]
    E --> F[3 * 2 = 6]
    F --> G[4 * 6 = 24]
    G --> H[5 * 24 = 120]
    H --> I[Return 120]
```

## 4. Time Complexity Analysis

Both the iterative and recursive implementations exhibit linear time complexity relative to the input size.

### 4.1 Iterative Complexity

The `for` loop executes exactly `(number - 1)` times (when starting from `2`). Ignoring constant factors and lower-order terms, the number of operations scales linearly with `n`.

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(1)** (constant auxiliary space)

### 4.2 Recursive Complexity

The recursive function calls itself `(number - 1)` times until the base case is reached. Each call performs a constant amount of work (a multiplication and a subtraction).

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(n)** due to the call stack growth proportional to `n`

### 4.3 Big O Justification

According to Big O rules, constant multipliers and lower-order additions are disregarded. Although the loop in the iterative version starts at `2`, the number of iterations remains proportional to `n`, yielding O(n). Similarly, the recursive depth equals `n`, resulting in O(n) time complexity.

## 5. Summary

The factorial function provides a clear illustration of both iterative and recursive problem-solving paradigms. The iterative approach uses a simple loop with minimal memory overhead, while the recursive approach offers a direct translation of the mathematical definition. Both methods operate in O(n) time, making them suitable for moderate input sizes. Understanding these implementations reinforces fundamental concepts in algorithm design and complexity analysis.