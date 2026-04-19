# Implementation of Bubble Sort in JavaScript

## 1. Introduction

This document presents a practical implementation of the Bubble Sort algorithm in JavaScript. Building upon the theoretical foundation established in the preceding discussion, the objective is to translate the algorithmic logic into executable code. The implementation adheres to the in-place sorting paradigm and incorporates the optimization of early termination when the array becomes sorted prior to completing all passes.

## 2. Algorithm Recap

Bubble Sort operates by repeatedly traversing the array, comparing adjacent elements, and swapping them if they appear in the incorrect order. With each complete pass, the largest unsorted element migrates to its correct position at the end of the array. This process repeats for the remaining unsorted portion until the entire collection is ordered.

### 2.1 Key Characteristics

- **Comparison-based:** Elements are ordered through pairwise comparisons.
- **In-place:** Sorting occurs within the original array without requiring auxiliary data structures proportional to input size.
- **Stable:** Equal elements retain their relative ordering.
- **Adaptive:** With optimization, the algorithm detects sorted sequences and terminates early.

## 3. Implementation Steps

The following systematic procedure outlines the construction of the `bubbleSort` function.

### 3.1 Determine Array Length

Store the length of the input array in a constant variable to avoid repeated property access.

### 3.2 Outer Loop for Pass Control

Establish a `for` loop that iterates from `i = 0` to `length - 1`. Each iteration corresponds to one complete pass through the array. In the worst case, `length - 1` passes are required to guarantee a fully sorted array.

### 3.3 Inner Loop for Adjacent Comparisons

Within the outer loop, construct a nested `for` loop that iterates from `j = 0` to `length - i - 2`. The upper bound decreases with each outer iteration because the largest elements have already been placed in their final positions at the end of the array.

### 3.4 Conditional Swap

During each inner loop iteration, compare `array[j]` with `array[j + 1]`. If the left element exceeds the right element, perform a swap using a temporary variable.

### 3.5 Optimization with Swap Flag

Introduce a boolean flag `swapped` initialized to `false` at the beginning of each outer loop pass. Set the flag to `true` whenever a swap occurs. If the flag remains `false` after completing the inner loop, the array is fully sorted, and the outer loop can be terminated prematurely.

### 3.6 Return the Sorted Array

After the outer loop concludes, return the reference to the original (now sorted) array.

## 4. Complete JavaScript Implementation

The following code implements the Bubble Sort algorithm as described. Critical lines are annotated with explanatory comments.

```javascript
/**
 * Sorts an array of numbers in ascending order using the Bubble Sort algorithm.
 * The function modifies the input array in place.
 *
 * @param {number[]} array - The array to be sorted.
 * @returns {number[]} The sorted array (reference to the original array).
 */
function bubbleSort(array) {
    // Obtain the length of the array to control loop bounds
    const length = array.length;

    // Outer loop: each iteration represents one complete pass through the array
    for (let i = 0; i < length; i++) {
        // Flag to detect whether any swap occurred during the current pass
        let swapped = false;

        // Inner loop: compare adjacent elements within the unsorted portion
        // The unsorted portion shrinks by one after each outer loop iteration
        for (let j = 0; j < length - i - 1; j++) {
            // If the left element is greater than the right element, swap them
            if (array[j] > array[j + 1]) {
                // Temporary variable to facilitate the swap
                let temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                swapped = true; // A swap occurred, so the array may not be fully sorted
            }
        }

        // If no swaps were performed in this pass, the array is already sorted
        if (!swapped) {
            break;
        }
    }

    // Return the sorted array
    return array;
}

// Example usage and verification
const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
console.log('Original array:', numbers);

bubbleSort(numbers);
console.log('Sorted array:  ', numbers);
```

**Expected Output:**
```
Original array: [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
Sorted array:   [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
```

### 4.1 Explanation of Key Code Segments

- **`const length = array.length;`**  
  Caches the array length to improve readability and avoid repeated property lookups.

- **Outer Loop Condition `i < length`**  
  Ensures sufficient passes to sort the array. In practice, the loop often terminates early due to the `swapped` flag.

- **Inner Loop Condition `j < length - i - 1`**  
  The `- i` term accounts for the fact that after each pass, the largest `i` elements are already in their final sorted positions at the end. The `- 1` prevents accessing an index beyond the array bounds when comparing `j` with `j + 1`.

- **Swap Mechanism**  
  A temporary variable `temp` holds the value of `array[j]` while `array[j]` is overwritten with `array[j + 1]`. Subsequently, `array[j + 1]` receives the value stored in `temp`.

- **Early Termination**  
  The `if (!swapped) break;` statement significantly improves performance on nearly sorted or already sorted inputs, reducing the best-case time complexity to **O(n)**.

## 5. Complexity Analysis

### 5.1 Time Complexity

The time complexity of the implemented Bubble Sort varies based on the initial ordering of the input data.

| Case          | Description                                      | Time Complexity |
|---------------|--------------------------------------------------|-----------------|
| Best          | Array is already sorted. Only one pass occurs.   | O(n)            |
| Average       | Array elements are in random order.              | O(n²)           |
| Worst         | Array is sorted in reverse order.                | O(n²)           |

The nested loops account for the quadratic behavior in the average and worst cases. The number of comparisons is approximately `n(n-1)/2`.

### 5.2 Space Complexity

The algorithm sorts the array **in place**. Apart from the loop counters and the temporary variable used during swapping, no additional memory proportional to the input size is allocated. Consequently, the auxiliary space complexity is **O(1)**.

## 6. Verification with Additional Test Cases

To ensure robustness, the implementation should be tested with diverse input scenarios.

```javascript
// Test case 1: Array with duplicate values
const duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5];
bubbleSort(duplicates);
console.log('Duplicates sorted:', duplicates);
// Expected: [1, 1, 2, 3, 4, 5, 5, 6, 9]

// Test case 2: Single-element array
const single = [42];
bubbleSort(single);
console.log('Single element sorted:', single);
// Expected: [42]

// Test case 3: Empty array
const empty = [];
bubbleSort(empty);
console.log('Empty array sorted:', empty);
// Expected: []
```

## 7. Conclusion

The implementation of Bubble Sort in JavaScript serves as an instructive exercise in algorithmic thinking and fundamental programming constructs such as loops, conditionals, and in-place data manipulation. Although the algorithm's quadratic time complexity limits its applicability to large datasets, the process of coding it reinforces essential concepts that are transferable to the study of more efficient sorting algorithms. The optimization technique employed—early termination upon detecting a sorted state—demonstrates how minor enhancements can yield measurable performance improvements under favorable input conditions.