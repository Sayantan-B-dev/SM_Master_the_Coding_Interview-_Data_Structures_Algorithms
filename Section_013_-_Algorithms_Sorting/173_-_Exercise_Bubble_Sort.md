# Exercise: Bubble Sort Implementation

## 1. Introduction

This document provides a structured exercise for implementing the Bubble Sort algorithm based on the concepts introduced in the preceding theoretical discussion. The objective is to translate the algorithmic understanding into functional code, reinforcing both the mechanics of the algorithm and proficiency in JavaScript programming.

## 2. Exercise Objectives

Upon completion of this exercise, the learner should be able to:

- Implement the Bubble Sort algorithm from first principles in JavaScript.
- Apply the optimization technique of early termination when no swaps occur.
- Verify the correctness of the implementation using test cases.
- Analyze the time and space complexity of the written code.

## 3. Problem Statement

Write a function named `bubbleSort` that accepts an array of numbers as its argument and returns the array sorted in ascending order. The function must sort the array **in place**, meaning that it should modify the original array rather than creating a new sorted copy.

### 3.1 Function Signature

```javascript
/**
 * Sorts an array of numbers in ascending order using the Bubble Sort algorithm.
 * @param {number[]} arr - The array to be sorted.
 * @returns {number[]} The sorted array (sorted in place).
 */
function bubbleSort(arr) {
    // Implementation goes here
}
```

### 3.2 Requirements

- **Algorithm:** The implementation must follow the Bubble Sort logic of repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.
- **Optimization:** The function must include a flag to detect whether any swaps were performed during a pass. If a pass completes without any swaps, the function should terminate early.
- **In-Place Sorting:** The input array must be modified directly; no additional array should be created.
- **Return Value:** The function should return the reference to the sorted array for convenience.

## 4. Implementation Steps

The following steps outline the recommended approach for constructing the Bubble Sort function.

### 4.1 Determine the Length of the Array

Use the `length` property to obtain the number of elements in the array. This value is required to control the iteration bounds.

### 4.2 Outer Loop for Passes

Construct a `for` loop that runs from `i = 0` to `n - 1`. Each iteration of this loop represents a complete pass through the array. The number of required passes is at most `n - 1`.

### 4.3 Inner Loop for Comparisons

Within the outer loop, create a nested `for` loop that iterates from `j = 0` to `n - i - 2`. This range ensures that the inner loop only traverses the unsorted portion of the array. After each pass, the largest element among the unsorted portion is correctly placed at the end, so the effective length of the unsorted segment decreases by one.

### 4.4 Comparison and Swap

Inside the inner loop, compare `arr[j]` with `arr[j + 1]`. If `arr[j] > arr[j + 1]`, swap the two elements using a temporary variable.

### 4.5 Swap Detection Flag

Before the inner loop begins, declare a boolean variable `swapped` and set it to `false`. Whenever a swap occurs, set `swapped` to `true`. After the inner loop completes, check the value of `swapped`. If it remains `false`, break out of the outer loop, as the array is already sorted.

### 4.6 Return the Array

After the outer loop terminates, return the original array reference.

## 5. Solution Code

The following JavaScript code implements the Bubble Sort algorithm according to the specifications outlined above. Critical sections are annotated with explanatory comments.

```javascript
function bubbleSort(arr) {
    const n = arr.length;
    
    // Outer loop: each iteration is one pass through the array
    for (let i = 0; i < n - 1; i++) {
        let swapped = false; // Flag to track whether any swap occurred in this pass
        
        // Inner loop: compare adjacent elements in the unsorted portion
        // The unsorted portion shrinks by 1 after each pass (hence n - i - 1)
        for (let j = 0; j < n - i - 1; j++) {
            // Compare adjacent elements
            if (arr[j] > arr[j + 1]) {
                // Swap elements using a temporary variable
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true; // Mark that a swap occurred
            }
        }
        
        // If no elements were swapped, the array is already sorted
        if (!swapped) {
            break;
        }
    }
    
    return arr;
}

// Test cases
const testArray1 = [64, 34, 25, 12, 22, 11, 90];
console.log('Original:', testArray1);
console.log('Sorted:  ', bubbleSort(testArray1));

const testArray2 = [5, 1, 4, 2, 8];
console.log('Original:', testArray2);
console.log('Sorted:  ', bubbleSort(testArray2));

const testArray3 = [1, 2, 3, 4, 5]; // Already sorted
console.log('Original:', testArray3);
console.log('Sorted:  ', bubbleSort(testArray3));
```

**Expected Output:**
```
Original: [64, 34, 25, 12, 22, 11, 90]
Sorted:   [11, 12, 22, 25, 34, 64, 90]
Original: [5, 1, 4, 2, 8]
Sorted:   [1, 2, 4, 5, 8]
Original: [1, 2, 3, 4, 5]
Sorted:   [1, 2, 3, 4, 5]
```

## 6. Verification and Testing

To ensure the correctness of the implementation, test the function with various input scenarios:

| Test Case Description | Input Array | Expected Output |
|-----------------------|-------------|-----------------|
| Unsorted random numbers | `[64, 34, 25, 12, 22, 11, 90]` | `[11, 12, 22, 25, 34, 64, 90]` |
| Small unsorted array | `[5, 1, 4, 2, 8]` | `[1, 2, 4, 5, 8]` |
| Already sorted array | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` |
| Array with duplicates | `[3, 1, 3, 2, 1]` | `[1, 1, 2, 3, 3]` |
| Single element array | `[42]` | `[42]` |
| Empty array | `[]` | `[]` |

## 7. Complexity Analysis of the Implementation

### 7.1 Time Complexity

- **Worst Case (Reverse Sorted):** The outer loop runs `n-1` times, and the inner loop runs approximately `n-i-1` times per pass. The total number of comparisons is approximately `n(n-1)/2`, resulting in **O(n²)** time complexity.
- **Average Case:** On random data, the number of comparisons is still **O(n²)**.
- **Best Case (Already Sorted):** The `swapped` flag ensures that only one pass of `n-1` comparisons is performed, yielding **O(n)** time complexity.

### 7.2 Space Complexity

The algorithm sorts the array in place and uses only a constant amount of additional memory for the `temp` variable and loop counters. Therefore, the auxiliary space complexity is **O(1)**.

## 8. Additional Resources

The following resources provide further context and supplementary material for this exercise:

- **GitHub Repository:** The companion code repository for the course contains additional examples and exercises.  
  [Master the Coding Interview: Data Structures + Algorithms Code](https://github.com/aneagoie/ztm-master-the-coding-interview-ds-algo)

- **Interactive Visualization:** Refer to the sorting algorithm visualization tool mentioned in the course materials to observe Bubble Sort in action alongside other algorithms under various input conditions.

## 9. Conclusion

Implementing Bubble Sort from scratch consolidates the understanding of nested loops, in-place array manipulation, and algorithmic optimization. Although the algorithm is not suitable for production use with large datasets, the exercise builds foundational skills essential for tackling more advanced sorting algorithms and algorithmic problem-solving in general.