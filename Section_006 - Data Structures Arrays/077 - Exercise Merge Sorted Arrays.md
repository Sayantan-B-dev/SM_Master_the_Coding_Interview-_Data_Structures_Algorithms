# Merging Two Sorted Arrays

## 1. Problem Statement

Given two arrays that are already sorted in ascending order, the task is to produce a single array containing all elements from both input arrays, also sorted in ascending order.

**Example:**

```
Input:  array1 = [0, 3, 4, 31]
        array2 = [4, 6, 30]

Output: [0, 3, 4, 4, 6, 30, 31]
```

This problem tests the candidate's ability to traverse multiple data structures simultaneously using pointer techniques and to handle edge cases efficiently.

---

## 2. Conceptual Approach

The core idea is to leverage the fact that both input arrays are pre-sorted. Instead of concatenating and then sorting—which would yield O(n log n) time complexity—a linear-time merge can be performed by comparing the current smallest elements from each array and appending the smaller one to the result.

This is analogous to the **merge** step of the Merge Sort algorithm.

### 2.1 Algorithm Overview

1. Initialise an empty array to hold the merged result.
2. Initialise two pointers, `i` and `j`, both starting at `0`, to track the current index in `array1` and `array2` respectively.
3. While both pointers are within the bounds of their respective arrays:
   - Compare `array1[i]` and `array2[j]`.
   - Append the smaller element to the result array.
   - Increment the pointer of the array from which the element was taken.
4. After the main loop, one of the arrays may still contain unprocessed elements. Append all remaining elements from that array to the result (these elements are already sorted and greater than or equal to all merged elements).

### 2.2 Visual Illustration

```
array1: [0, 3, 4, 31]   (pointer i = 0)
array2: [4, 6, 30]      (pointer j = 0)
result: []

Step 1: Compare 0 and 4 → append 0, i=1
Step 2: Compare 3 and 4 → append 3, i=2
Step 3: Compare 4 and 4 → append 4 (from array1), i=3
Step 4: Compare 31 and 4 → append 4 (from array2), j=1
Step 5: Compare 31 and 6 → append 6, j=2
Step 6: Compare 31 and 30 → append 30, j=3 (array2 exhausted)
Step 7: Append remaining [31] from array1

Final result: [0, 3, 4, 4, 6, 30, 31]
```

---

## 3. Implementation in JavaScript

### 3.1 Standard Iterative Solution

```javascript
/**
 * Merges two sorted arrays into a single sorted array.
 * @param {number[]} arr1 - First sorted array.
 * @param {number[]} arr2 - Second sorted array.
 * @returns {number[]} Merged sorted array.
 */
function mergeSortedArrays(arr1, arr2) {
    // Input validation: handle edge cases
    if (arr1.length === 0) return arr2;
    if (arr2.length === 0) return arr1;

    const mergedArray = [];
    let i = 0; // Pointer for arr1
    let j = 0; // Pointer for arr2

    // Traverse both arrays until one is exhausted
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] <= arr2[j]) {
            mergedArray.push(arr1[i]);
            i++;
        } else {
            mergedArray.push(arr2[j]);
            j++;
        }
    }

    // Append any remaining elements from arr1
    while (i < arr1.length) {
        mergedArray.push(arr1[i]);
        i++;
    }

    // Append any remaining elements from arr2
    while (j < arr2.length) {
        mergedArray.push(arr2[j]);
        j++;
    }

    return mergedArray;
}

// Example usage
const array1 = [0, 3, 4, 31];
const array2 = [4, 6, 30];
console.log(mergeSortedArrays(array1, array2)); // [0, 3, 4, 4, 6, 30, 31]
```

### 3.2 Optimised Concise Implementation

Using array spread and a single while loop with conditional checks.

```javascript
function mergeSortedArraysConcise(arr1, arr2) {
    const merged = [];
    let i = 0, j = 0;

    while (i < arr1.length || j < arr2.length) {
        // If arr2 exhausted OR (arr1 has element AND arr1 element <= arr2 element)
        if (j >= arr2.length || (i < arr1.length && arr1[i] <= arr2[j])) {
            merged.push(arr1[i]);
            i++;
        } else {
            merged.push(arr2[j]);
            j++;
        }
    }

    return merged;
}
```

---

## 4. Complexity Analysis

| Metric           | Value        | Explanation                                                                                 |
|------------------|--------------|---------------------------------------------------------------------------------------------|
| **Time Complexity** | O(n + m)     | Each element from both arrays is visited exactly once. Here `n` = length of first array, `m` = length of second array. |
| **Space Complexity** | O(n + m)     | A new array of size `n + m` is created to hold the merged result. This is inherent to the problem. |

**In-place merging** is not possible without modifying one of the input arrays (which may be undesirable) unless the arrays are specially designed (e.g., one array has sufficient buffer space at the end).

---

## 5. Edge Cases and Considerations

| Scenario                           | Expected Behaviour                                                       |
|------------------------------------|--------------------------------------------------------------------------|
| One array is empty                 | Return the non-empty array as-is.                                        |
| Both arrays are empty              | Return an empty array.                                                   |
| Arrays contain duplicate values    | All duplicates are preserved in sorted order (e.g., two `4`s in example).|
| Arrays of vastly different lengths | The shorter array is exhausted first; remaining elements of the longer array are appended. |
| Negative numbers or mixed data     | Works correctly assuming standard numeric comparison.                     |

---

## 6. Alternative Approaches

### 6.1 Concatenation Followed by Sorting

A trivial but inefficient solution:

```javascript
function mergeSortedArraysNaive(arr1, arr2) {
    return arr1.concat(arr2).sort((a, b) => a - b);
}
```

**Time Complexity:** O((n+m) log(n+m)) due to sorting.
**Space Complexity:** O(n+m) for the concatenated array.

This approach fails to exploit the pre-sorted property of the inputs and is generally not acceptable in an interview setting.

### 6.2 Using Built-in Merge in Other Languages

Languages like Python offer `heapq.merge()` or `sorted(arr1 + arr2)`; however, demonstrating the manual pointer-based algorithm is preferred during technical evaluations.

---

## 7. Summary

- Merging two sorted arrays is a fundamental operation that can be accomplished in **linear time** using a two-pointer technique.
- The algorithm resembles the merge phase of Merge Sort and is an excellent demonstration of efficient array traversal.
- Key aspects include handling remaining elements after the main comparison loop and addressing edge cases like empty inputs.
- The solution achieves O(n + m) time complexity and O(n + m) space complexity, which is optimal for this problem.