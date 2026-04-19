# Space Complexity Analysis: Practical Examples and Evaluation

## Abstract

This document provides a practical demonstration of space complexity analysis using illustrative JavaScript code examples. Through the examination of two distinct functions, the methodology for determining the asymptotic space consumption of an algorithm is elucidated. The analysis emphasizes the critical distinction between input space (which is not counted) and auxiliary space (the additional memory allocated within the function). The examples illustrate both O(1) constant space and O(n) linear space complexities, reinforcing the principles enumerated in the space complexity cheat sheet.

---

## 1. Introduction

Space complexity, as introduced in the preceding section, quantifies the amount of **auxiliary memory** an algorithm requires relative to its input size `n`. This analysis focuses exclusively on the memory allocated **within the function's control**—variables, data structures, and stack frames—and explicitly excludes the memory occupied by the input data itself.

This document applies the conceptual framework of space complexity to two concrete JavaScript functions. The goal is to develop an intuitive ability to assess the memory footprint of code, a skill essential for optimizing resource-constrained applications and for succeeding in technical evaluations.

---

## 2. Example 1: Constant Space Complexity - O(1)

### 2.1 Function Definition: `boo(n)`

The first example presents a simple iterative function that logs a message a specified number of times. The function does not create any persistent data structures; it only utilizes a loop counter variable.

```javascript
/**
 * Logs the message "Boo!" a specified number of times.
 * @param {number} n - The number of times to log the message.
 */
function boo(n) {
    // Loop iterates 'n' times
    for (let i = 0; i < n; i++) {
        console.log('Boo!');
    }
}

// Example usage
boo(5);
// Output: "Boo!" logged 5 times to the console.
```

### 2.2 Time Complexity Assessment

The `boo` function contains a single `for` loop that iterates `n` times. The number of operations (console logs and loop increments) grows linearly with `n`.

**Time Complexity:** **O(n)** — Linear Time

### 2.3 Space Complexity Analysis

To determine the space complexity, all memory allocations occurring within the function body are identified.

| Allocation | Type | Quantity | Persistence |
| :--- | :--- | :--- | :--- |
| `let i = 0` | Primitive Variable | 1 | Reused per iteration (not re-declared) |
| Input Parameter `n` | Primitive Variable | 1 | Excluded (input space) |

**Analysis:**
- The function does **not** create any new data structures (e.g., arrays, objects).
- The loop counter `i` is a single numeric variable. Its memory allocation is constant and does not scale with `n`.
- The input `n` is passed as an argument; the memory occupied by the input itself is **not** considered auxiliary space.

**Conclusion:** The function allocates a fixed, constant amount of additional memory regardless of the magnitude of `n`.

**Space Complexity:** **O(1)** — Constant Space

---

## 3. Example 2: Linear Space Complexity - O(n)

### 3.1 Function Definition: `arrayOfHiNTimes(n)`

The second example demonstrates a function that generates a new array populated with the string `"hi"`. The size of the created array is directly proportional to the input parameter `n`.

```javascript
/**
 * Creates and returns an array filled with the string "hi" repeated 'n' times.
 * @param {number} n - The desired length of the output array.
 * @returns {string[]} - An array of length 'n' containing the string "hi" at each index.
 */
function arrayOfHiNTimes(n) {
    // Step 1: Allocate a new, empty array in memory.
    let hiArray = [];

    // Step 2: Iterate 'n' times, appending "hi" to the array on each iteration.
    for (let i = 0; i < n; i++) {
        hiArray[i] = 'hi'; // Alternatively: hiArray.push('hi');
    }

    // Step 3: Return the populated array.
    return hiArray;
}

// Example usage
const result = arrayOfHiNTimes(6);
console.log(result);
// Output: ['hi', 'hi', 'hi', 'hi', 'hi', 'hi']
```

### 3.2 Time Complexity Assessment

The function contains a single loop that executes `n` times. The `push` operation or indexed assignment to an array is an O(1) amortized operation. Therefore, the total time taken scales linearly with `n`.

**Time Complexity:** **O(n)** — Linear Time

### 3.3 Space Complexity Analysis

The space complexity is determined by examining the memory allocations performed within the function.

| Allocation | Type | Quantity | Relationship to `n` |
| :--- | :--- | :--- | :--- |
| `let hiArray = []` | Data Structure (Array) | 1 | Initially O(1), grows to O(n) |
| `hiArray` elements | Array Slots | `n` | Each element occupies memory proportional to its data type. |
| `let i = 0` | Primitive Variable | 1 | O(1) constant space |

**Analysis:**
- The function explicitly creates a new data structure: the array `hiArray`.
- The `for` loop populates `hiArray` with exactly `n` elements.
- The total memory consumed by `hiArray` is directly proportional to `n` (plus a constant overhead for the array object itself).
- Applying Rule 4 (Drop Non-Dominant Terms) and Rule 2 (Remove Constants), the constant memory used by the loop counter `i` is negligible compared to the `n`-sized array.

**Conclusion:** The amount of auxiliary memory allocated by the function grows linearly with the input size `n`.

**Space Complexity:** **O(n)** — Linear Space

---

## 4. Comparative Summary and Key Takeaways

The following table summarizes the differences between the two examples, highlighting the distinction between time and space complexity.

| Function | Time Complexity | Space Complexity | Dominant Factor |
| :--- | :--- | :--- | :--- |
| `boo(n)` | O(n) | **O(1)** | Loop execution time scales; memory is fixed. |
| `arrayOfHiNTimes(n)` | O(n) | **O(n)** | New array allocation scales linearly with input. |

### 4.1 Guiding Principles for Space Complexity Evaluation

1.  **Focus on Auxiliary Space:** Exclude the memory occupied by the input arguments. The analysis concerns only what the function **adds**.
2.  **Identify Data Structure Creation:** The instantiation of new arrays, objects, maps, or sets is the primary driver of increased space complexity.
3.  **Account for Recursive Depth:** (Not illustrated here, but noted) Recursive calls consume stack space. A recursion depth of `n` contributes O(n) to space complexity.
4.  **Apply Big O Simplification Rules:** Constant factors and lower-order terms are discarded. An algorithm that creates one array of size `n` and ten primitive variables still has a space complexity of O(n).

### 4.2 The Time-Space Trade-off in Context

The function `arrayOfHiNTimes` serves as a simple illustration of a common trade-off. If the requirement were simply to process or output data without retaining it, a solution with O(1) space might be preferable. However, if the generated array is required for subsequent operations (e.g., as input to another function), the O(n) space cost is an inherent necessity of the problem domain.

The ability to articulate both the time and space characteristics of a function is a hallmark of thorough algorithmic analysis.

---

## 5. Conclusion

Through the analysis of `boo(n)` and `arrayOfHiNTimes(n)`, the practical application of space complexity evaluation has been demonstrated. The `boo` function exemplifies **O(1) constant space**, as its memory footprint does not scale with input size. In contrast, `arrayOfHiNTimes` exhibits **O(n) linear space** due to the allocation of a new array whose size is proportional to `n`.

These examples reinforce the core principle that space complexity is concerned with the **additional memory** allocated during execution. The methodology outlined—identifying variables, data structures, and function call allocations—provides a reliable framework for analyzing any algorithm's memory efficiency. This understanding, coupled with time complexity analysis, empowers the engineer to make informed decisions balancing speed and memory usage.