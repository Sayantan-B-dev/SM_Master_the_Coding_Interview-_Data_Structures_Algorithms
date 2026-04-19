# Exercise: Selection Sort Implementation

## 1. Introduction

This document presents a structured exercise for implementing the Selection Sort algorithm based on the concepts introduced in the preceding discussion. Selection Sort is an elementary comparison-based sorting algorithm that partitions the array into sorted and unsorted regions, repeatedly selecting the minimum element from the unsorted portion and placing it at the end of the sorted region. This exercise aims to reinforce understanding of the algorithm through hands-on implementation in JavaScript.

## 2. Exercise Objectives

Upon completing this exercise, the learner will be able to:

- Implement the Selection Sort algorithm from first principles in JavaScript.
- Apply the logic of finding the minimum element in an unsorted subarray.
- Perform in-place swaps to build the sorted portion of the array.
- Verify the correctness of the implementation using diverse test cases.
- Analyze the time and space complexity of the Selection Sort algorithm.

## 3. Problem Statement

Write a function named `selectionSort` that accepts an array of numbers as its argument and returns the array sorted in ascending order. The function must sort the array **in place**, modifying the original array rather than creating a new one.

### 3.1 Function Signature

```javascript
/**
 * Sorts an array of numbers in ascending order using the Selection Sort algorithm.
 * @param {number[]} arr - The array to be sorted.
 * @returns {number[]} The sorted array (sorted in place).
 */
function selectionSort(arr) {
    // Implementation goes here
}
```

### 3.2 Requirements

- **Algorithm:** The implementation must adhere to the Selection Sort logic: repeatedly find the minimum element in the unsorted portion and swap it with the first element of that unsorted portion.
- **In-Place Sorting:** The input array must be modified directly; no auxiliary array should be created.
- **Return Value:** The function should return the reference to the sorted array for convenience.
- **Swaps:** Perform a swap only when the minimum element is not already in the correct position.

## 4. Implementation Steps

Follow these steps to construct the `selectionSort` function.

### 4.1 Determine Array Length

Obtain the length of the input array and store it in a constant variable for efficient access.

### 4.2 Outer Loop for Sorted Boundary

Construct a `for` loop that iterates from `i = 0` to `n - 2`. The variable `i` represents the boundary between the sorted and unsorted portions of the array. After `n - 1` elements have been placed, the last remaining element is automatically in its correct position.

### 4.3 Find the Minimum in the Unsorted Portion

Within the outer loop, assume the first element of the unsorted portion (at index `i`) is the minimum. Initialize a variable `minIndex` to `i`. Then, create an inner `for` loop that scans from `i + 1` to `n - 1`. Compare each element with the current minimum; if a smaller element is found, update `minIndex` accordingly.

### 4.4 Swap if Necessary

After the inner loop completes, if `minIndex` differs from `i`, swap the elements at indices `i` and `minIndex` using a temporary variable. This places the smallest remaining element into its correct sorted position.

### 4.5 Return the Array

After the outer loop finishes, return the reference to the original (now sorted) array.

## 5. Solution Code

The following JavaScript code implements the Selection Sort algorithm as specified. Critical sections are annotated with explanatory comments.

```javascript
/**
 * Sorts an array of numbers in ascending order using the Selection Sort algorithm.
 * The function modifies the input array in place.
 *
 * @param {number[]} arr - The array to be sorted.
 * @returns {number[]} The sorted array (reference to the original array).
 */
function selectionSort(arr) {
    const n = arr.length;

    // Outer loop: i represents the boundary of the sorted portion
    for (let i = 0; i < n - 1; i++) {
        // Assume the first element of the unsorted portion is the minimum
        let minIndex = i;

        // Inner loop: scan the unsorted portion to find the true minimum
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j; // Update index of the minimum element
            }
        }

        // Swap only if a new minimum was found
        if (minIndex !== i) {
            let temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    return arr;
}

// Example usage and verification
const numbers = [64, 25, 12, 22, 11];
console.log('Original array:', numbers);
selectionSort(numbers);
console.log('Sorted array:  ', numbers);
```

**Expected Output:**
```
Original array: [64, 25, 12, 22, 11]
Sorted array:   [11, 12, 22, 25, 64]
```

### 5.1 Explanation of Key Code Segments

- **`const n = arr.length;`**  
  Caches the array length to avoid repeated property lookups.

- **Outer Loop Condition `i < n - 1`**  
  The loop runs `n - 1` times because after placing `n - 1` elements, the final element is naturally sorted.

- **`let minIndex = i;`**  
  Initializes the index of the minimum element to the start of the unsorted subarray.

- **Inner Loop (`j` from `i + 1` to `n - 1`)**  
  Scans the remaining elements to find the smallest value. When a smaller element is encountered, `minIndex` is updated.

- **Conditional Swap**  
  The swap is performed only if `minIndex !== i`, avoiding unnecessary operations when the minimum is already in place.

- **Return Statement**  
  Returns the reference to the sorted array, enabling method chaining if desired.

## 6. Complexity Analysis

### 6.1 Time Complexity

Selection Sort performs the same number of comparisons regardless of the initial ordering of the input data.

- **Number of Comparisons:** The inner loop executes `(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2` times. This yields a time complexity of **O(n²)** for the best, average, and worst cases.
- **Number of Swaps:** At most one swap occurs per outer loop iteration, resulting in a maximum of `n - 1` swaps. This linear number of swaps is a distinguishing feature of Selection Sort.

### 6.2 Space Complexity

Selection Sort operates **in place**, requiring only a constant amount of additional memory for loop counters, the `minIndex` variable, and a temporary variable during swapping. Consequently, the auxiliary space complexity is **O(1)**.

### 6.3 Summary Table

| Case          | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| Best          | O(n²)           | O(1)             |
| Average       | O(n²)           | O(1)             |
| Worst         | O(n²)           | O(1)             |

## 7. Verification and Testing

To ensure the correctness of the implementation, test the function with various input scenarios.

```javascript
// Test case 1: Unsorted random numbers
const test1 = [64, 34, 25, 12, 22, 11, 90];
selectionSort(test1);
console.log('Test 1:', test1); // Expected: [11, 12, 22, 25, 34, 64, 90]

// Test case 2: Array with duplicate values
const test2 = [4, 2, 4, 1, 3, 2];
selectionSort(test2);
console.log('Test 2:', test2); // Expected: [1, 2, 2, 3, 4, 4]

// Test case 3: Already sorted array
const test3 = [1, 2, 3, 4, 5];
selectionSort(test3);
console.log('Test 3:', test3); // Expected: [1, 2, 3, 4, 5]

// Test case 4: Reverse sorted array
const test4 = [5, 4, 3, 2, 1];
selectionSort(test4);
console.log('Test 4:', test4); // Expected: [1, 2, 3, 4, 5]

// Test case 5: Single-element array
const test5 = [42];
selectionSort(test5);
console.log('Test 5:', test5); // Expected: [42]

// Test case 6: Empty array
const test6 = [];
selectionSort(test6);
console.log('Test 6:', test6); // Expected: []
```

## 8. Additional Resources

The following resources provide further context and supplementary material for this exercise:

- **Replit Exercise:** The original interactive coding environment for this exercise can be accessed at the following URL (if available):  
  [https://repl.it/@aneagoie/selectionSort-exercise](https://repl.it/@aneagoie/selectionSort-exercise)

  *Note: If the link is inaccessible, the code provided in this document may be executed in any JavaScript environment, such as a browser's developer console or a local Node.js installation.*

- **Course GitHub Repository:** Additional examples and related exercises are available in the course repository:  
  [Master the Coding Interview: Data Structures + Algorithms Code](https://github.com/aneagoie/ztm-master-the-coding-interview-ds-algo)

- **Algorithm Visualization:** To reinforce understanding, observe the behavior of Selection Sort using an online sorting visualization tool. Watching the algorithm progressively build the sorted portion from the left helps solidify the concept.

## 9. Conclusion

Implementing Selection Sort from scratch reinforces fundamental programming concepts including nested loops, in-place array manipulation, and the strategy of building a sorted subarray. Although the algorithm's quadratic time complexity limits its practical utility for large datasets, its minimal swap count and straightforward logic make it a valuable pedagogical tool. Mastery of Selection Sort provides a solid foundation for understanding more advanced sorting algorithms and enhances overall algorithmic problem-solving skills.