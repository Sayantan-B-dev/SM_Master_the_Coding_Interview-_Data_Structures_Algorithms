# Bubble Sort: Elementary Sorting Algorithm

## 1. Introduction

Bubble Sort is one of the fundamental sorting algorithms classified under the category of **elementary sorts**. It is characterized by its conceptual simplicity and serves primarily as a pedagogical tool for introducing algorithmic thinking and the analysis of computational complexity. The algorithm derives its name from the manner in which larger elements "bubble up" to their correct positions at the end of the array through successive passes.

Despite its intuitive appeal, Bubble Sort is among the least efficient sorting algorithms in practice. Its quadratic time complexity renders it unsuitable for large datasets. However, understanding its mechanics provides a foundation for appreciating the design and optimization of more advanced sorting techniques.

## 2. Algorithm Description

Bubble Sort operates by repeatedly traversing the list of elements, comparing adjacent pairs, and swapping them if they are in the incorrect order. Each complete pass through the list places the largest unsorted element into its final sorted position at the end of the array. The process is repeated for the remaining unsorted portion until the entire list is ordered.

### 2.1 Step-by-Step Procedure

Given an unsorted array of elements, the algorithm proceeds as follows:

1. Compare the first element with the second element.
2. If the first element is greater than the second, swap their positions.
3. Move to the next pair of adjacent elements (second and third) and repeat the comparison and conditional swap.
4. Continue this process until the end of the array is reached.
5. After the first pass, the largest element is guaranteed to be positioned at the final index.
6. Repeat steps 1 through 5 for the remaining unsorted portion of the array (i.e., excluding the last element after each pass).
7. Terminate when a complete pass occurs without any swaps, indicating that the array is fully sorted.

### 2.2 Visual Representation

The following sequence illustrates the bubbling process on an array `[6, 5, 3, 1, 8, 7, 2, 4]`:

**Pass 1:**
```
[6, 5, 3, 1, 8, 7, 2, 4]  → compare 6 and 5 → swap → [5, 6, 3, 1, 8, 7, 2, 4]
[5, 6, 3, 1, 8, 7, 2, 4]  → compare 6 and 3 → swap → [5, 3, 6, 1, 8, 7, 2, 4]
[5, 3, 6, 1, 8, 7, 2, 4]  → compare 6 and 1 → swap → [5, 3, 1, 6, 8, 7, 2, 4]
[5, 3, 1, 6, 8, 7, 2, 4]  → compare 6 and 8 → no swap
[5, 3, 1, 6, 8, 7, 2, 4]  → compare 8 and 7 → swap → [5, 3, 1, 6, 7, 8, 2, 4]
[5, 3, 1, 6, 7, 8, 2, 4]  → compare 8 and 2 → swap → [5, 3, 1, 6, 7, 2, 8, 4]
[5, 3, 1, 6, 7, 2, 8, 4]  → compare 8 and 4 → swap → [5, 3, 1, 6, 7, 2, 4, 8]
```
After Pass 1, the element `8` is in its final position.

**Pass 2:**
```
[5, 3, 1, 6, 7, 2, 4, 8]  → compare 5 and 3 → swap → [3, 5, 1, 6, 7, 2, 4, 8]
[3, 5, 1, 6, 7, 2, 4, 8]  → compare 5 and 1 → swap → [3, 1, 5, 6, 7, 2, 4, 8]
[3, 1, 5, 6, 7, 2, 4, 8]  → compare 5 and 6 → no swap
[3, 1, 5, 6, 7, 2, 4, 8]  → compare 6 and 7 → no swap
[3, 1, 5, 6, 7, 2, 4, 8]  → compare 7 and 2 → swap → [3, 1, 5, 6, 2, 7, 4, 8]
[3, 1, 5, 6, 2, 7, 4, 8]  → compare 7 and 4 → swap → [3, 1, 5, 6, 2, 4, 7, 8]
```
After Pass 2, elements `7` and `8` are correctly placed.

The algorithm continues until the array is fully ordered.

### 2.3 Flowchart

A simplified flowchart representing the Bubble Sort algorithm is provided below.

```mermaid
graph TD
    A[Start] --> B[Initialize n = array length]
    B --> C[For i from 0 to n-1]
    C --> D[Set swapped = false]
    D --> E[For j from 0 to n-i-2]
    E --> F{arr[j] > arr[j+1] ?}
    F -->|Yes| G[Swap arr[j] and arr[j+1]]
    G --> H[Set swapped = true]
    F -->|No| I[Continue]
    H --> I
    I --> J[End inner loop]
    J --> K{swapped == false ?}
    K -->|Yes| L[Array sorted, exit]
    K -->|No| M[Next i iteration]
    M --> C
    L --> N[End]
```

## 3. Implementation in JavaScript

The following JavaScript code implements the Bubble Sort algorithm with an optimization that terminates early if no swaps occur during a pass, indicating that the array is already sorted.

```javascript
/**
 * Sorts an array using the Bubble Sort algorithm.
 * @param {Array<number>} arr - The array to be sorted.
 * @returns {Array<number>} The sorted array (sorted in place).
 */
function bubbleSort(arr) {
    const n = arr.length;
    
    // Outer loop controls the number of passes
    for (let i = 0; i < n - 1; i++) {
        let swapped = false; // Flag to detect if any swap occurred in this pass
        
        // Inner loop compares adjacent elements
        // The unsorted portion shrinks by 1 each pass
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap elements using a temporary variable
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        
        // If no elements were swapped, the array is already sorted
        if (!swapped) {
            break;
        }
    }
    
    return arr;
}

// Example usage
const numbers = [6, 5, 3, 1, 8, 7, 2, 4];
console.log('Original array:', numbers);
console.log('Sorted array:', bubbleSort(numbers));
```

**Output:**
```
Original array: [6, 5, 3, 1, 8, 7, 2, 4]
Sorted array: [1, 2, 3, 4, 5, 6, 7, 8]
```

### 3.1 Code Explanation

- **Outer Loop (i):** Executes `n-1` passes. Each pass ensures that the largest unsorted element moves to its correct position at the end.
- **Inner Loop (j):** Iterates through the unsorted portion of the array (up to `n-i-1`). Compares `arr[j]` with `arr[j+1]` and swaps if the left element is larger.
- **Optimization Flag (swapped):** If a complete pass occurs without any swaps, the array is already sorted, and the algorithm terminates early, improving best-case performance to **O(n)**.

## 4. Complexity Analysis

### 4.1 Time Complexity

The time complexity of Bubble Sort is analyzed by counting the number of comparisons and swaps performed.

- **Worst Case:** The array is in reverse order. The algorithm must perform the maximum number of comparisons and swaps.

  - Number of comparisons: `(n-1) + (n-2) + ... + 1 = n(n-1)/2`
  - Number of swaps: `n(n-1)/2`

  Therefore, worst-case time complexity is **O(n²)**.

- **Average Case:** Assuming random ordering, the number of comparisons is also approximately `n(n-1)/2`, leading to **O(n²)** average-case time complexity.

- **Best Case:** The array is already sorted. With the optimized version using the `swapped` flag, only one pass of `n-1` comparisons is performed, and no swaps occur. The time complexity becomes **O(n)**.

### 4.2 Space Complexity

Bubble Sort operates **in place**, meaning it requires only a constant amount of additional memory for temporary variables (e.g., `temp` during swapping). Therefore, the auxiliary space complexity is **O(1)**.

### 4.3 Summary Table

| Case          | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| Best          | O(n)            | O(1)             |
| Average       | O(n²)           | O(1)             |
| Worst         | O(n²)           | O(1)             |

## 5. Characteristics and Practical Considerations

### 5.1 Stability

Bubble Sort is a **stable sorting algorithm**. When two elements are equal, no swap occurs, preserving their relative order in the sorted output. This property is significant when sorting complex records by multiple keys.

### 5.2 Adaptability

The algorithm is **adaptive** in its optimized form. If the input is partially or fully sorted, the early termination condition reduces the number of passes, improving performance beyond the worst-case bound.

### 5.3 Suitability

Due to its quadratic time complexity, Bubble Sort is rarely used in production software except in the following niche scenarios:

- **Educational Purposes:** Illustrates fundamental sorting concepts and loop structures.
- **Extremely Small Datasets:** For arrays with a very small number of elements (e.g., n < 10), the constant-factor overhead of more complex algorithms may outweigh their asymptotic advantage.
- **Nearly Sorted Data:** With early termination optimization, Bubble Sort can approach linear time on already ordered or nearly ordered inputs.

## 6. Conclusion

Bubble Sort exemplifies a straightforward approach to sorting through repeated adjacent comparisons and swaps. While its performance limitations render it impractical for large-scale applications, its study imparts essential lessons about algorithm design, complexity analysis, and the significance of optimization techniques. The algorithm serves as a stepping stone toward comprehending more efficient sorting methods such as Merge Sort and Quick Sort, which will be explored in subsequent sections.