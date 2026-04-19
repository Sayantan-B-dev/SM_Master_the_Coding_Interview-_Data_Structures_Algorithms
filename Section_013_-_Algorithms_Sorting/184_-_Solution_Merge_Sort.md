# Merge Sort: Solution Analysis and Implementation Details

## 1. Introduction

This document presents the solution for the Merge Sort implementation exercise, providing a detailed line-by-line analysis of the algorithm's mechanics. Merge Sort is a canonical divide-and-conquer sorting algorithm that achieves **O(n log n)** time complexity in all cases, offering a substantial performance improvement over elementary quadratic sorting methods. While the recursive implementation may appear complex, a systematic examination of the code reveals the elegant interplay between the division and merging phases.

## 2. Algorithm Decomposition

Merge Sort consists of two principal functions:

- **`mergeSort(array)`**: Recursively divides the input array into progressively smaller subarrays until the base case of a single element is reached.
- **`merge(left, right)`**: Combines two sorted subarrays into a single sorted array by comparing their front elements.

### 2.1 The Division Phase (`mergeSort`)

The `mergeSort` function is responsible for recursively partitioning the array. Its operation can be understood through the following steps:

1. **Base Case:** If the array length is less than or equal to `1`, the array is trivially sorted and returned as is.
2. **Finding the Midpoint:** The index `mid = Math.floor(array.length / 2)` is computed to split the array into approximately equal halves.
3. **Creating Subarrays:** The `slice()` method extracts the left half (`array.slice(0, mid)`) and the right half (`array.slice(mid)`).
4. **Recursive Sorting:** `mergeSort` is called on both `left` and `right` subarrays.
5. **Combining:** The sorted subarrays are merged using the `merge` function, and the result is returned.

### 2.2 The Merging Phase (`merge`)

The `merge` function accepts two sorted arrays and produces a single sorted array. The procedure is as follows:

1. Initialize an empty `result` array and two pointers `i` (for `left`) and `j` (for `right`), both starting at `0`.
2. Compare `left[i]` and `right[j]`. Append the smaller element to `result` and advance the corresponding pointer.
3. Continue until one of the arrays is fully traversed.
4. Append any remaining elements from the non-exhausted array to `result`.
5. Return the merged `result` array.

## 3. JavaScript Implementation with Logging for Visualization

The following implementation includes `console.log` statements that illustrate the division and merging process step by step. Executing this code aids in understanding the recursive flow.

```javascript
/**
 * Merges two sorted arrays into a single sorted array.
 * @param {number[]} left - The left sorted subarray.
 * @param {number[]} right - The right sorted subarray.
 * @returns {number[]} A new sorted array containing all elements from left and right.
 */
function merge(left, right) {
    const result = [];
    let leftIndex = 0;
    let rightIndex = 0;

    // Log the current merge operation
    console.log(`Merging: [${left}] and [${right}]`);

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] <= right[rightIndex]) {
            result.push(left[leftIndex]);
            leftIndex++;
        } else {
            result.push(right[rightIndex]);
            rightIndex++;
        }
    }

    // Append any remaining elements from the left array
    while (leftIndex < left.length) {
        result.push(left[leftIndex]);
        leftIndex++;
    }

    // Append any remaining elements from the right array
    while (rightIndex < right.length) {
        result.push(right[rightIndex]);
        rightIndex++;
    }

    console.log(`Result: [${result}]`);
    return result;
}

/**
 * Sorts an array using the Merge Sort algorithm.
 * @param {number[]} array - The array to be sorted.
 * @returns {number[]} A new sorted array.
 */
function mergeSort(array) {
    // Log the current subarray being processed
    console.log(`Splitting: [${array}]`);

    if (array.length <= 1) {
        console.log(`Base case reached: [${array}]`);
        return array;
    }

    const mid = Math.floor(array.length / 2);
    const left = array.slice(0, mid);
    const right = array.slice(mid);

    // Recursively sort left and right halves
    const sortedLeft = mergeSort(left);
    const sortedRight = mergeSort(right);

    // Merge the sorted halves
    return merge(sortedLeft, sortedRight);
}

// Example execution
const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
console.log('Initial array:', numbers);
const sorted = mergeSort(numbers);
console.log('Final sorted array:', sorted);
```

### 3.1 Expected Console Output (Excerpt)

Executing the above code produces a trace that mirrors the recursive division and merging process:

```
Initial array: [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
Splitting: [99,44,6,2,1,5,63,87,283,4,0]
Splitting: [99,44,6,2,1]
Splitting: [99,44]
Splitting: [99]
Base case reached: [99]
Splitting: [44]
Base case reached: [44]
Merging: [99] and [44]
Result: [44,99]
Splitting: [6,2,1]
Splitting: [6]
Base case reached: [6]
Splitting: [2,1]
Splitting: [2]
Base case reached: [2]
Splitting: [1]
Base case reached: [1]
Merging: [2] and [1]
Result: [1,2]
Merging: [6] and [1,2]
Result: [1,2,6]
Merging: [44,99] and [1,2,6]
Result: [1,2,6,44,99]
...
Final sorted array: [0,1,2,4,5,6,44,63,87,99,283]
```

The trace clearly shows:
- The initial array being split repeatedly until single-element subarrays are obtained.
- The merge operation combining pairs of sorted subarrays and outputting the merged result.
- The progressive construction of the final sorted array.

## 4. Step-by-Step Execution Trace

To further elucidate the recursive behavior, the following table enumerates the sequence of operations for a simplified input array `[99, 44, 6, 2]`.

| Step | Function Call          | Action                                                                 | Current Subarray |
|------|------------------------|------------------------------------------------------------------------|------------------|
| 1    | `mergeSort([99,44,6,2])` | Split into `[99,44]` and `[6,2]`                                       | `[99,44,6,2]`   |
| 2    | `mergeSort([99,44])`     | Split into `[99]` and `[44]`                                           | `[99,44]`       |
| 3    | `mergeSort([99])`        | Base case: return `[99]`                                               | `[99]`          |
| 4    | `mergeSort([44])`        | Base case: return `[44]`                                               | `[44]`          |
| 5    | `merge([99], [44])`      | Merge: `[44,99]` returned                                              | `[99,44]`       |
| 6    | `mergeSort([6,2])`       | Split into `[6]` and `[2]`                                             | `[6,2]`         |
| 7    | `mergeSort([6])`         | Base case: return `[6]`                                                | `[6]`           |
| 8    | `mergeSort([2])`         | Base case: return `[2]`                                                | `[2]`           |
| 9    | `merge([6], [2])`        | Merge: `[2,6]` returned                                                | `[6,2]`         |
| 10   | `merge([44,99], [2,6])`  | Merge: compare 44 and 2 → 2; compare 44 and 6 → 6; then 44, 99 → `[2,6,44,99]` | `[99,44,6,2]`   |

The final sorted array `[2,6,44,99]` is constructed.

## 5. Complexity Analysis Revisited

The implementation demonstrates the theoretical complexity characteristics of Merge Sort.

### 5.1 Time Complexity

- **Division:** The array is halved at each recursive step, creating a recursion tree of height **log₂ n**.
- **Merging:** At each level of the recursion tree, every element is examined exactly once during the merge operations, contributing **O(n)** work per level.
- **Total:** **O(n log n)** for best, average, and worst cases.

### 5.2 Space Complexity

The auxiliary space complexity is **O(n)** because:
- Each recursive call creates new subarrays using `slice()`, allocating memory proportional to the size of the subarray.
- The `merge` function allocates a `result` array of size equal to the combined length of the two subarrays.
- At the deepest level of recursion, the total auxiliary memory across all active merge operations is proportional to **n**.

### 5.3 Comparison Table

| Algorithm      | Time (Best) | Time (Average) | Time (Worst) | Space       | Stable |
|----------------|-------------|----------------|--------------|-------------|--------|
| Bubble Sort    | O(n)        | O(n²)          | O(n²)        | O(1)        | Yes    |
| Selection Sort | O(n²)       | O(n²)          | O(n²)        | O(1)        | No     |
| Insertion Sort | O(n)        | O(n²)          | O(n²)        | O(1)        | Yes    |
| **Merge Sort** | O(n log n)  | O(n log n)     | O(n log n)   | O(n)        | Yes    |

## 6. Practical Considerations

### 6.1 When to Use Merge Sort

- **Large Datasets:** The O(n log n) complexity ensures scalability.
- **Stable Sorting Required:** Merge Sort preserves the relative order of equal elements.
- **External Sorting:** Merge Sort's divide-and-conquer nature is well-suited for sorting data that exceeds available memory (e.g., external merge sort on disk).
- **Linked Lists:** Merge Sort can sort linked lists with O(1) extra space by adjusting pointers.

### 6.2 When to Consider Alternatives

- **Memory-Constrained Environments:** The O(n) auxiliary space may be prohibitive. In such cases, in-place algorithms like Quick Sort or Heap Sort are preferable.
- **Small Arrays:** For very small arrays (n < 50), Insertion Sort's lower constant factor often outperforms Merge Sort.

## 7. Conclusion

The Merge Sort solution presented herein illustrates the power and elegance of the divide-and-conquer paradigm. By recursively partitioning the array and merging sorted subarrays, the algorithm achieves optimal asymptotic complexity for comparison-based sorting. While the implementation may be intricate, understanding its mechanics provides deep insight into recursion, algorithmic efficiency, and the tradeoffs between time and space complexity. Mastery of Merge Sort is a significant milestone in the study of algorithms and serves as a foundation for tackling more advanced sorting and searching problems.