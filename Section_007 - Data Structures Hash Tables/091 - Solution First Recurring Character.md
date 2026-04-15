# First Recurring Character Problem: Algorithmic Approaches and Analysis

## 1. Problem Statement

Given an array of elements, the objective is to identify and return the **first recurring character** (or element) encountered during a sequential traversal of the array. If no element appears more than once, the function should return `undefined`.

**Example Input and Expected Output:**

| Input Array | First Recurring Character |
| :--- | :--- |
| `[2, 5, 1, 2, 3, 5, 1, 2, 4]` | `2` (appears at index 0 and index 3) |
| `[2, 1, 1, 2, 3, 5, 1, 2, 4]` | `1` (appears at index 1 and index 2) |
| `[2, 3, 4, 5]` | `undefined` |

This problem serves as an excellent illustration of how the selection of an appropriate data structure can dramatically influence algorithmic efficiency.

## 2. Naive Approach: Nested Iteration

### 2.1 Algorithm Description

The most intuitive solution involves a brute-force comparison using two nested loops. The outer loop selects an element at index `i`, and the inner loop scans the elements to the right of `i` (from index `i+1` onward) to find a match. The first match encountered during this process is returned.

### 2.2 Implementation in JavaScript

```javascript
/**
 * Finds the first recurring character using a nested loop approach.
 * @param {Array} input - The array to be examined.
 * @returns {*} - The first recurring element, or undefined if none exists.
 */
function firstRecurringCharacterV1(input) {
    // Outer loop: selects the element to compare
    for (let i = 0; i < input.length; i++) {
        // Inner loop: scans elements to the right of the current outer element
        for (let j = i + 1; j < input.length; j++) {
            // If a match is found, return the element immediately
            if (input[i] === input[j]) {
                return input[i];
            }
        }
    }
    // If no recurring character is found after full traversal
    return undefined;
}

// Example usage
console.log(firstRecurringCharacterV1([2, 5, 1, 2, 3, 5, 1, 2, 4])); // Output: 2
console.log(firstRecurringCharacterV1([2, 1, 1, 2, 3, 5, 1, 2, 4])); // Output: 1
console.log(firstRecurringCharacterV1([2, 3, 4, 5]));                // Output: undefined
```

### 2.3 Complexity Analysis

- **Time Complexity:** O(n²)
  - For each element selected by the outer loop, the inner loop iterates over the remaining elements. In the worst case (no recurring character), the total number of comparisons is approximately n(n-1)/2.
  - Even though the inner loop starts at `i+1` (reducing the number of comparisons by roughly half), the asymptotic complexity remains quadratic.

- **Space Complexity:** O(1)
  - The algorithm operates in-place and does not allocate additional data structures that scale with the input size.

## 3. Optimized Approach: Hash Table Utilization

### 3.1 Algorithm Description

The quadratic time complexity of the naive approach can be reduced to linear time by employing a hash table (implemented as a JavaScript object or `Map`). The algorithm performs a single pass over the input array while maintaining a record of previously encountered elements.

**Procedure:**

1. Initialize an empty hash table (`map`).
2. Iterate through each element of the input array sequentially.
3. For each element:
   - Check if the element already exists as a key in the hash table.
   - If it exists, the element is the first recurring character; return it immediately.
   - If it does not exist, add the element as a key to the hash table with an arbitrary value (e.g., its index or `true`).
4. If the loop completes without finding a recurrence, return `undefined`.

### 3.2 Implementation in JavaScript

```javascript
/**
 * Finds the first recurring character using a hash table for O(n) time complexity.
 * @param {Array} input - The array to be examined.
 * @returns {*} - The first recurring element, or undefined if none exists.
 */
function firstRecurringCharacterV2(input) {
    // Initialize an empty object to serve as the hash table
    const map = {};

    // Single pass through the array
    for (let i = 0; i < input.length; i++) {
        const currentItem = input[i];

        // Check if the current item already exists as a key in the hash table
        // Note: Strict inequality check against undefined avoids JavaScript falsy pitfalls (e.g., value 0)
        if (map[currentItem] !== undefined) {
            return currentItem; // Recurrence detected
        }

        // Store the item in the hash table with a placeholder value (e.g., its index)
        map[currentItem] = i;
    }

    // No recurring character found
    return undefined;
}

// Example usage
console.log(firstRecurringCharacterV2([2, 5, 1, 2, 3, 5, 1, 2, 4])); // Output: 2
console.log(firstRecurringCharacterV2([2, 1, 1, 2, 3, 5, 1, 2, 4])); // Output: 1
console.log(firstRecurringCharacterV2([2, 3, 4, 5]));                // Output: undefined
```

**Critical Implementation Note:**
In JavaScript, the condition `if (map[currentItem])` is insufficient because the stored value may be `0` (the index), which evaluates to `false` in a boolean context. Therefore, an explicit check `map[currentItem] !== undefined` is required to correctly identify whether a key exists.

### 3.3 Complexity Analysis

- **Time Complexity:** O(n)
  - The algorithm traverses the input array exactly once. Hash table insertion and lookup operations are O(1) on average. Thus, the overall time is linear with respect to the number of elements.

- **Space Complexity:** O(n)
  - In the worst-case scenario where no recurrence exists, the hash table stores every unique element from the input array. The memory usage scales linearly with the input size.

## 4. Comparative Analysis of Approaches

| Metric | Naive Approach (Nested Loops) | Optimized Approach (Hash Table) |
| :--- | :--- | :--- |
| **Time Complexity** | O(n²) | O(n) |
| **Space Complexity** | O(1) | O(n) |
| **Code Complexity** | Simple, no additional structures | Requires hash table initialization and management |
| **Suitability** | Small input sizes only | Preferred for larger datasets |

**Trade-off Summary:**
The hash table approach trades increased memory consumption for a substantial reduction in execution time. This trade-off is widely accepted in modern software engineering, as memory is often more abundant than CPU time.

## 5. Nuance: Definition of "First" Recurring Character

An important subtlety emerges when the input array contains multiple recurring characters. The interpretation of "first" can vary, leading to different correct answers depending on the problem's exact specification.

### 5.1 Scenario Illustration

Consider the input array: `[2, 5, 5, 2, 3, 5, 1, 2, 4]`

- **Naive Approach Output:** `2`
- **Optimized Hash Table Approach Output:** `5`

**Explanation of Discrepancy:**

- **Naive Approach (Nested Loops):** The outer loop fixes the first element (`2`) and then scans forward. It finds another `2` at index 3 before the inner loop for the second element (`5`) even begins checking for a matching `5` at index 2. Thus, `2` is identified first according to this scanning order.

- **Hash Table Approach:** The algorithm proceeds sequentially from left to right, adding elements to the hash table. It encounters `2` (stores), `5` (stores), and then a second `5`. At the moment the second `5` is encountered, a recurrence is detected immediately, and `5` is returned. This identifies the element whose **second occurrence appears earliest** in the array.

### 5.2 Formal Definitions

| Interpretation | Description | Algorithm that Satisfies |
| :--- | :--- | :--- |
| **Earliest Second Occurrence** | The element whose duplicate appears at the smallest index during a left-to-right scan. | Hash Table Approach |
| **Smallest Distance Between First and Second Occurrence** | The element with the minimal gap between its first and second appearance. | Nested Loop Approach (with specific scanning order) |

**Recommendation for Interviews:**
When presented with the "first recurring character" problem, it is essential to clarify with the interviewer which definition is intended. The hash table approach generally aligns with the more common interpretation of finding the character that repeats **first in the sequence of traversal**.

### 5.3 Adapting the Hash Table Approach for the Alternative Definition

To modify the hash table solution to return `2` instead of `5` for the input `[2, 5, 5, 2, ...]` (i.e., to find the character with the minimal span between occurrences), a different strategy is required. One possible method involves:

1. Storing the index of the first occurrence of each element in a hash table during a first pass.
2. Performing a second pass to identify the element with the minimum difference `(currentIndex - firstOccurrenceIndex)`.

**Implementation Skeleton:**

```javascript
function firstRecurringCharacterMinSpan(input) {
    const firstOccurrence = {};
    let minSpan = Infinity;
    let result = undefined;

    for (let i = 0; i < input.length; i++) {
        const item = input[i];
        if (firstOccurrence[item] !== undefined) {
            const span = i - firstOccurrence[item];
            if (span < minSpan) {
                minSpan = span;
                result = item;
            }
        } else {
            firstOccurrence[item] = i;
        }
    }
    return result;
}
```

This variation maintains O(n) time complexity while satisfying the alternative interpretation.

## 6. Conclusion

The "First Recurring Character" problem exemplifies the profound impact of data structure selection on algorithmic efficiency. The transition from a nested loop (O(n²)) to a hash table-based solution (O(n)) demonstrates how theoretical knowledge of time complexity and hash table operations can be directly applied to optimize real-world code.

Key takeaways include:

- **Hash tables provide O(1) average-time lookups**, making them ideal for problems requiring membership testing or frequency counting.
- **Space-time trade-offs** are a fundamental consideration in algorithm design.
- **Precise problem specification** is crucial, as ambiguous definitions can lead to multiple valid solutions.

Proficiency in recognizing scenarios where hash tables can replace nested iterations is a hallmark of effective algorithmic problem-solving and is frequently tested in technical interviews.