# Selection Sort: Solution and Analysis

## 1. Introduction

This document presents the solution for the Selection Sort algorithm implementation exercise. Selection Sort is an elementary comparison-based sorting algorithm characterized by its in-place operation and minimal number of swaps. The algorithm iteratively identifies the smallest element in the unsorted portion of the array and places it at the beginning of the sorted sequence. While its quadratic time complexity limits its practical application to small datasets, the algorithm serves as an instructive example of fundamental sorting principles.

## 2. Algorithmic Approach

Selection Sort operates by maintaining a conceptual division between a sorted subarray at the left end and an unsorted subarray occupying the remainder. During each iteration, the algorithm scans the unsorted portion to locate the minimum element and swaps it with the leftmost element of that unsorted portion, thereby expanding the sorted boundary by one position.

### 2.1 Step-by-Step Logic

1. Initialize the boundary index `i` to `0`, marking the start of the unsorted subarray.
2. Set `minIndex = i` as the provisional index of the minimum element.
3. Traverse the unsorted subarray from index `i + 1` to the end of the array.
4. For each element, if its value is less than the value at `minIndex`, update `minIndex` to the current index.
5. After scanning the entire unsorted portion, swap the element at index `i` with the element at `minIndex` if they differ.
6. Increment `i` by `1` and repeat steps 2 through 5 until `i` reaches `n - 1`.

### 2.2 Visual Illustration

Consider the array `[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]`. The following sequence demonstrates the first two passes:

**Initial Array:**
```
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
```

**Pass 1:**
- Minimum element in the entire array is `0` at index `10`.
- Swap with element at index `0`.
```
[0, 44, 6, 2, 1, 5, 63, 87, 283, 4, 99]
```

**Pass 2:**
- Minimum element in unsorted portion (indices `1` to `10`) is `1` at index `4`.
- Swap with element at index `1`.
```
[0, 1, 6, 2, 44, 5, 63, 87, 283, 4, 99]
```

The process continues until the array is fully ordered.

## 3. JavaScript Implementation

The following code provides a complete implementation of the Selection Sort algorithm in JavaScript. The function modifies the input array in place and returns the reference to the sorted array.

```javascript
/**
 * Sorts an array of numbers in ascending order using the Selection Sort algorithm.
 * The function modifies the input array in place.
 *
 * @param {number[]} array - The array to be sorted.
 * @returns {number[]} The sorted array (reference to the original array).
 */
function selectionSort(array) {
    const n = array.length;

    // Outer loop: i marks the boundary between sorted and unsorted portions
    for (let i = 0; i < n - 1; i++) {
        // Assume the first element of the unsorted portion is the minimum
        let minIndex = i;

        // Inner loop: scan the unsorted portion to find the true minimum
        for (let j = i + 1; j < n; j++) {
            // If a smaller element is found, update minIndex
            if (array[j] < array[minIndex]) {
                minIndex = j;
            }
        }

        // Swap the found minimum element with the element at the boundary
        // Perform swap only if a new minimum was identified
        if (minIndex !== i) {
            let temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }

    return array;
}

// Example usage
const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
console.log('Original array:', numbers);
selectionSort(numbers);
console.log('Sorted array:  ', numbers);
```

**Expected Output:**
```
Original array: [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
Sorted array:   [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
```

### 3.1 Code Explanation

- **`const n = array.length;`**  
  Caches the length of the array to avoid repeated property access.

- **Outer Loop (`i` from `0` to `n - 2`):**  
  Controls the boundary of the sorted portion. After placing `n - 1` elements, the final element is automatically in its correct position.

- **`let minIndex = i;`**  
  Initializes the index of the minimum element to the start of the unsorted subarray.

- **Inner Loop (`j` from `i + 1` to `n - 1`):**  
  Scans the unsorted portion. Whenever a smaller element is encountered, `minIndex` is updated.

- **Conditional Swap:**  
  The swap is executed only if `minIndex` differs from `i`, avoiding unnecessary operations when the minimum is already correctly positioned.

## 4. Complexity Analysis

Selection Sort exhibits consistent performance characteristics regardless of the initial ordering of the input data.

### 4.1 Time Complexity

The algorithm performs exactly `(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2` comparisons in all cases. Consequently, the time complexity is **O(n²)** for the best, average, and worst cases.

### 4.2 Space Complexity

Selection Sort is an in-place algorithm. It requires only a constant amount of additional memory for loop counters, the `minIndex` variable, and a temporary variable during swapping. Therefore, the auxiliary space complexity is **O(1)**.

### 4.3 Summary Table

| Case          | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| Best          | O(n²)           | O(1)             |
| Average       | O(n²)           | O(1)             |
| Worst         | O(n²)           | O(1)             |

## 5. Comparison with Bubble Sort

Although both Selection Sort and Bubble Sort are elementary algorithms with **O(n²)** time complexity, they differ in several key aspects.

| Feature                | Selection Sort                    | Bubble Sort                       |
|------------------------|-----------------------------------|-----------------------------------|
| Number of Comparisons  | Always n(n-1)/2                   | Variable; can be O(n) in best case|
| Number of Swaps         | At most n-1                       | Up to n(n-1)/2 in worst case      |
| Stability              | Unstable                          | Stable                            |
| Adaptivity             | Non-adaptive                      | Adaptive (with optimization)       |

Selection Sort performs significantly fewer swaps than Bubble Sort, which may be advantageous in environments where write operations are costly.

## 6. Implementation in Other Programming Languages

The Selection Sort algorithm is language-agnostic and can be readily implemented in any programming language. Below are illustrative examples in Python and Java for reference.

### 6.1 Python Implementation

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
numbers = [64, 25, 12, 22, 11]
print("Sorted array:", selection_sort(numbers))
```

### 6.2 Java Implementation

```java
public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int[] numbers = {64, 25, 12, 22, 11};
        selectionSort(numbers);
        System.out.println(Arrays.toString(numbers));
    }
}
```

## 7. Additional Resources

For further exploration of the Selection Sort algorithm and its implementations, the following resources are recommended:

- **Online Code Repositories:** Platforms such as GitHub host numerous implementations across various languages. Searching for "selection sort [language]" yields practical examples.
- **Algorithm Visualization Tools:** Interactive websites (e.g., VisuAlgo, Sorting.at) provide animated demonstrations of Selection Sort and other algorithms, aiding in conceptual reinforcement.
- **Documentation and Tutorials:** Official language documentation and educational platforms (e.g., GeeksforGeeks, Programiz) offer detailed explanations and code samples.

## 8. Conclusion

Selection Sort is a fundamental sorting algorithm that, despite its quadratic time complexity, offers a clear illustration of the "select and place" strategy. Its minimal swap count and in-place nature distinguish it from other elementary sorts. The implementation provided in this document, along with the accompanying complexity analysis, equips the learner with both practical coding experience and a deeper understanding of algorithmic tradeoffs. Mastery of Selection Sort serves as a stepping stone toward more advanced sorting techniques that achieve superior asymptotic performance.