# Exercise: Insertion Sort Implementation

## 1. Introduction

This document presents a structured exercise for implementing the Insertion Sort algorithm based on the concepts introduced in the preceding discussion. Insertion Sort is an elementary comparison-based sorting algorithm that constructs the final sorted array incrementally, inserting each new element into its correct position within the already sorted prefix. This exercise aims to reinforce understanding of the algorithm through hands-on implementation in JavaScript.

## 2. Exercise Objectives

Upon completing this exercise, the learner will be able to:

- Implement the Insertion Sort algorithm from first principles in JavaScript.
- Apply the logic of shifting elements to create space for insertion.
- Recognize the algorithm's adaptive behavior and its efficiency on nearly sorted data.
- Verify the correctness of the implementation using diverse test cases.
- Analyze the time and space complexity of the Insertion Sort algorithm under various input conditions.

## 3. Problem Statement

Write a function named `insertionSort` that accepts an array of numbers as its argument and returns the array sorted in ascending order. The function must sort the array **in place**, modifying the original array rather than creating a new one.

### 3.1 Function Signature

```javascript
/**
 * Sorts an array of numbers in ascending order using the Insertion Sort algorithm.
 * @param {number[]} arr - The array to be sorted.
 * @returns {number[]} The sorted array (sorted in place).
 */
function insertionSort(arr) {
    // Implementation goes here
}
```

### 3.2 Requirements

- **Algorithm:** The implementation must adhere to the Insertion Sort logic: maintain a sorted prefix, extract the next element, shift larger elements rightward, and insert the extracted element into the correct position.
- **In-Place Sorting:** The input array must be modified directly; no auxiliary array should be created.
- **Return Value:** The function should return the reference to the sorted array for convenience.

## 4. Implementation Steps

Follow these steps to construct the `insertionSort` function.

### 4.1 Determine Array Length

Obtain the length of the input array and store it in a constant variable for efficient access.

### 4.2 Outer Loop for Unsorted Elements

Construct a `for` loop that iterates from `i = 1` to `n - 1`. The element at index `i` is the `key` to be inserted into the sorted prefix spanning indices `0` through `i - 1`.

### 4.3 Store the Current Element

Assign `array[i]` to a variable `key`. This value will be placed into its correct position after shifting.

### 4.4 Initialize Inner Loop Pointer

Set `j = i - 1`, representing the last index of the sorted prefix.

### 4.5 Shift Larger Elements Rightward

Create a `while` loop that continues as long as `j >= 0` and `array[j] > key`. Within the loop, assign `array[j + 1] = array[j]` and decrement `j`. This operation shifts elements that are greater than `key` one position to the right, creating a vacancy for insertion.

### 4.6 Insert the Key

After the `while` loop terminates, place `key` into the vacancy at index `j + 1`.

### 4.7 Return the Array

After the outer loop completes, return the reference to the original (now sorted) array.

## 5. Solution Code

The following JavaScript code implements the Insertion Sort algorithm as specified. Critical sections are annotated with explanatory comments.

```javascript
/**
 * Sorts an array of numbers in ascending order using the Insertion Sort algorithm.
 * The function modifies the input array in place.
 *
 * @param {number[]} array - The array to be sorted.
 * @returns {number[]} The sorted array (reference to the original array).
 */
function insertionSort(array) {
    const n = array.length;

    // Start from the second element (index 1); the first element is trivially sorted
    for (let i = 1; i < n; i++) {
        let key = array[i];   // Element to be inserted into the sorted prefix
        let j = i - 1;        // Last index of the sorted prefix

        // Shift elements of the sorted prefix that are greater than key to the right
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j--;
        }

        // Place the key in its correct position
        array[j + 1] = key;
    }

    return array;
}

// Example usage and verification
const numbers = [64, 25, 12, 22, 11];
console.log('Original array:', numbers);
insertionSort(numbers);
console.log('Sorted array:  ', numbers);
```

**Expected Output:**
```
Original array: [64, 25, 12, 22, 11]
Sorted array:   [11, 12, 22, 25, 64]
```

### 5.1 Explanation of Key Code Segments

- **`const n = array.length;`**  
  Caches the array length to avoid repeated property lookups.

- **Outer Loop (`i` from `1` to `n - 1`):**  
  Iterates through the unsorted portion, extracting each element as `key` for insertion.

- **`let key = array[i];`**  
  Stores the current element. This value will be inserted into the correct position within the sorted prefix.

- **`let j = i - 1;`**  
  Initializes `j` to the last index of the sorted subarray.

- **`while (j >= 0 && array[j] > key)`**  
  Shifts elements that are greater than `key` one position to the right. The loop terminates when either the beginning of the array is reached or an element less than or equal to `key` is encountered.

- **`array[j + 1] = key;`**  
  Inserts `key` into the vacancy created by the shifting process.

## 6. Complexity Analysis

The time complexity of Insertion Sort is highly sensitive to the initial ordering of the input data.

### 6.1 Time Complexity

- **Best Case (Already Sorted):**  
  The inner `while` loop condition `array[j] > key` evaluates to false for every element. Thus, only `n - 1` comparisons are performed, and no shifts occur. The time complexity is **O(n)**.

- **Average Case (Random Order):**  
  On average, each new element is compared with approximately half of the already sorted elements. The total number of comparisons is roughly `1 + 2 + ... + (n - 1) = n(n - 1) / 4`, which is **O(n²)**.

- **Worst Case (Reverse Sorted):**  
  Each new element is smaller than all elements in the sorted portion, necessitating the maximum number of comparisons and shifts. The total comparisons are `1 + 2 + ... + (n - 1) = n(n - 1) / 2`, yielding **O(n²)** time complexity.

### 6.2 Space Complexity

Insertion Sort operates **in place**, requiring only a constant amount of additional memory for the `key` variable and loop counters. Consequently, the auxiliary space complexity is **O(1)**.

### 6.3 Summary Table

| Case          | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| Best          | O(n)            | O(1)             |
| Average       | O(n²)           | O(1)             |
| Worst         | O(n²)           | O(1)             |

## 7. Flowchart

A simplified flowchart depicting the Insertion Sort algorithm is provided below.

```mermaid
graph TD
    A[Start] --> B[Set i = 1]
    B --> C{i < n ?}
    C -->|No| D[Array sorted]
    D --> E[End]
    C -->|Yes| F[key = array[i], j = i - 1]
    F --> G{j >= 0 and array[j] > key ?}
    G -->|Yes| H[array[j+1] = array[j]]
    H --> I[j = j - 1]
    I --> G
    G -->|No| J[array[j+1] = key]
    J --> K[i = i + 1]
    K --> C
```

## 8. Verification and Testing

To ensure the correctness of the implementation, test the function with various input scenarios.

```javascript
// Test case 1: Unsorted random numbers
const test1 = [64, 34, 25, 12, 22, 11, 90];
insertionSort(test1);
console.log('Test 1:', test1); // Expected: [11, 12, 22, 25, 34, 64, 90]

// Test case 2: Array with duplicate values
const test2 = [4, 2, 4, 1, 3, 2];
insertionSort(test2);
console.log('Test 2:', test2); // Expected: [1, 2, 2, 3, 4, 4]

// Test case 3: Already sorted array
const test3 = [1, 2, 3, 4, 5];
insertionSort(test3);
console.log('Test 3:', test3); // Expected: [1, 2, 3, 4, 5]

// Test case 4: Reverse sorted array
const test4 = [5, 4, 3, 2, 1];
insertionSort(test4);
console.log('Test 4:', test4); // Expected: [1, 2, 3, 4, 5]

// Test case 5: Single-element array
const test5 = [42];
insertionSort(test5);
console.log('Test 5:', test5); // Expected: [42]

// Test case 6: Empty array
const test6 = [];
insertionSort(test6);
console.log('Test 6:', test6); // Expected: []
```

## 9. Additional Resources

The following resources provide further context and supplementary material for this exercise:

- **Replit Exercise:** The original interactive coding environment for this exercise can be accessed at the following URL (if available):  
  [https://repl.it/@aneagoie/insertionSort-exercise](https://repl.it/@aneagoie/insertionSort-exercise)

  *Note: If the link is inaccessible, the code provided in this document may be executed in any JavaScript environment, such as a browser's developer console or a local Node.js installation.*

- **Algorithm Visualization:** To reinforce understanding, observe the behavior of Insertion Sort using an online sorting visualization tool. The Insertion Sort dance video (AlgoRythmics) provides a kinesthetic representation of the algorithm that can aid in building an intuitive mental model.

## 10. Conclusion

Implementing Insertion Sort from scratch reinforces fundamental programming concepts including nested loops, in-place array manipulation, and the strategy of incrementally building a sorted prefix. The algorithm's adaptive nature makes it particularly valuable for small datasets and nearly sorted inputs. Mastery of Insertion Sort provides a solid foundation for understanding more advanced sorting algorithms and enhances overall algorithmic problem-solving skills.