# Selection Sort: Elementary Sorting Algorithm

## 1. Introduction

Selection Sort is an elementary comparison-based sorting algorithm that operates by repeatedly identifying the minimum element from the unsorted portion of the array and placing it at the beginning of the sorted sequence. Like Bubble Sort, it is characterized by conceptual simplicity and serves primarily as a pedagogical instrument for introducing algorithmic design and analysis. Although its quadratic time complexity renders it inefficient for large datasets, Selection Sort offers advantages in scenarios where memory writes are costly, as it performs a minimal number of swaps.

## 2. Algorithm Description

Selection Sort partitions the input array into two logical regions: a **sorted subarray** at the left end and an **unsorted subarray** occupying the remainder. Initially, the sorted subarray is empty. During each iteration, the algorithm scans the unsorted subarray to locate the smallest element, then swaps it with the leftmost element of the unsorted subarray, thereby extending the sorted subarray by one position. This process repeats until the unsorted subarray is exhausted.

### 2.1 Step-by-Step Procedure

Given an unsorted array of `n` elements, the algorithm proceeds as follows:

1. Set the boundary index `i = 0` marking the start of the unsorted subarray.
2. Find the index `minIndex` of the minimum element within the subarray `array[i ... n-1]`.
3. Swap the element at `array[i]` with the element at `array[minIndex]`.
4. Increment `i` by 1 to expand the sorted subarray.
5. Repeat steps 2 through 4 until `i` equals `n - 1`.

### 2.2 Visual Representation

Consider the array `[6, 5, 3, 1, 8, 7, 2, 4]`. The following sequence illustrates the progression of Selection Sort:

**Initial Array:**
```
[6, 5, 3, 1, 8, 7, 2, 4]
```

**Pass 1:** Locate minimum in entire array (value `1` at index 3). Swap with element at index 0.
```
[1, 5, 3, 6, 8, 7, 2, 4]
  ↑              ↑
sorted         unsorted
```

**Pass 2:** Locate minimum in unsorted portion (value `2` at index 6). Swap with element at index 1.
```
[1, 2, 3, 6, 8, 7, 5, 4]
     ↑           ↑
  sorted       unsorted
```

**Pass 3:** Minimum is `3` at index 2. Swap with itself (no change).
```
[1, 2, 3, 6, 8, 7, 5, 4]
        ↑        ↑
     sorted    unsorted
```

**Pass 4:** Minimum is `4` at index 7. Swap with element at index 3.
```
[1, 2, 3, 4, 8, 7, 5, 6]
           ↑     ↑
        sorted unsorted
```

**Pass 5:** Minimum is `5` at index 6. Swap with element at index 4.
```
[1, 2, 3, 4, 5, 7, 8, 6]
              ↑     ↑
           sorted unsorted
```

**Pass 6:** Minimum is `6` at index 7. Swap with element at index 5.
```
[1, 2, 3, 4, 5, 6, 8, 7]
                 ↑  ↑
              sorted unsorted
```

**Pass 7:** Minimum is `7` at index 7. Swap with element at index 6.
```
[1, 2, 3, 4, 5, 6, 7, 8]
                    ↑
                 sorted (complete)
```

The array is now fully sorted.

### 2.3 Flowchart

A simplified flowchart depicting the Selection Sort algorithm is presented below.

```mermaid
graph TD
    A[Start] --> B[Set i = 0]
    B --> C{i < n - 1 ?}
    C -->|No| D[Array sorted]
    D --> E[End]
    C -->|Yes| F[Set minIndex = i]
    F --> G[Set j = i + 1]
    G --> H{j < n ?}
    H -->|Yes| I{array[j] < array[minIndex] ?}
    I -->|Yes| J[minIndex = j]
    I -->|No| K[j = j + 1]
    J --> K
    K --> H
    H -->|No| L[Swap array[i] and array[minIndex]]
    L --> M[i = i + 1]
    M --> C
```

## 3. Implementation in JavaScript

The following JavaScript code implements the Selection Sort algorithm. The function sorts the array in place and returns the reference to the sorted array.

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

    // Outer loop: iterate over each position to place the next minimum element
    for (let i = 0; i < n - 1; i++) {
        // Assume the first element of the unsorted portion is the minimum
        let minIndex = i;

        // Inner loop: scan the remaining unsorted elements to find the true minimum
        for (let j = i + 1; j < n; j++) {
            if (array[j] < array[minIndex]) {
                minIndex = j; // Update the index of the minimum element
            }
        }

        // If a new minimum was found, swap it with the element at index i
        if (minIndex !== i) {
            let temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }

    return array;
}

// Example usage and verification
const numbers = [6, 5, 3, 1, 8, 7, 2, 4];
console.log('Original array:', numbers);

selectionSort(numbers);
console.log('Sorted array:  ', numbers);
```

**Expected Output:**
```
Original array: [6, 5, 3, 1, 8, 7, 2, 4]
Sorted array:   [1, 2, 3, 4, 5, 6, 7, 8]
```

### 3.1 Code Explanation

- **`const n = array.length;`**  
  Caches the length of the array for efficient access.

- **Outer Loop (`i` from `0` to `n - 2`):**  
  Each iteration determines the correct element for position `i`. The loop runs `n - 1` times because after placing `n - 1` elements, the last remaining element is naturally in its correct position.

- **`let minIndex = i;`**  
  Initializes the index of the minimum element to the start of the unsorted subarray.

- **Inner Loop (`j` from `i + 1` to `n - 1`):**  
  Scans the unsorted portion of the array to locate the smallest element. Whenever a smaller element is found, `minIndex` is updated.

- **Swap Condition:**  
  If `minIndex` differs from `i`, the elements at indices `i` and `minIndex` are swapped using a temporary variable. This places the minimum element of the unsorted subarray into its correct sorted position.

- **Return Statement:**  
  The function returns the reference to the original array, now sorted.

## 4. Complexity Analysis

### 4.1 Time Complexity

Selection Sort's time complexity is independent of the initial ordering of the input data.

- **Number of Comparisons:**  
  The inner loop performs `(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2` comparisons, regardless of whether the array is partially or fully sorted. This yields a time complexity of **O(n²)** for all cases (best, average, and worst).

- **Number of Swaps:**  
  At most one swap occurs per outer loop iteration, resulting in a maximum of `n - 1` swaps. This is significantly fewer than Bubble Sort's worst-case swap count.

### 4.2 Space Complexity

Selection Sort operates **in place**, requiring only a constant amount of additional memory for loop counters, the `minIndex` variable, and a temporary variable during swapping. Consequently, the auxiliary space complexity is **O(1)**.

### 4.3 Summary Table

| Case          | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| Best          | O(n²)           | O(1)             |
| Average       | O(n²)           | O(1)             |
| Worst         | O(n²)           | O(1)             |

## 5. Characteristics and Practical Considerations

### 5.1 Stability

Selection Sort is **not stable** by default. When swapping the minimum element with the element at index `i`, the relative order of equal elements may be altered. Consider the array `[2, 2, 1]`. The first pass swaps the `1` with the first `2`, resulting in `[1, 2, 2]`, which preserves the order of the two `2`s. However, in a more complex example such as `[5, 3, 5, 1]`, the first pass swaps `1` with the first `5`, moving it after the second `5`, thus destabilizing the order of the `5`s.

### 5.2 Adaptability

Unlike optimized Bubble Sort, Selection Sort is **non-adaptive**. It always performs the full complement of comparisons, irrespective of whether the input is already sorted. There is no mechanism for early termination.

### 5.3 Suitability

Despite its quadratic time complexity, Selection Sort may be advantageous in specific contexts:

- **Minimizing Write Operations:** When the cost of writing to memory (or swapping elements) is high, Selection Sort's linear number of swaps (`O(n)`) can be beneficial compared to Bubble Sort's quadratic swap count in the worst case.
- **Small Datasets:** For very small arrays (e.g., `n < 20`), the constant factors and simplicity of Selection Sort may result in acceptable performance.
- **Educational Purposes:** Selection Sort provides a clear illustration of the divide-between-sorted-and-unsorted strategy and introduces the concept of finding extrema.

## 6. Comparison with Bubble Sort

The following table contrasts Selection Sort with Bubble Sort to highlight key differences.

| Feature                | Selection Sort                    | Bubble Sort                       |
|------------------------|-----------------------------------|-----------------------------------|
| Comparisons            | Always n(n-1)/2                   | Variable; can be O(n) in best case|
| Swaps                  | At most n-1                       | Up to n(n-1)/2 in worst case      |
| Stability              | Unstable                          | Stable                            |
| Adaptivity             | Non-adaptive                      | Adaptive (with optimization)       |
| In-Place               | Yes                               | Yes                               |
| Space Complexity       | O(1)                              | O(1)                              |

## 7. Verification with Additional Test Cases

To ensure correctness, the implementation should be validated with diverse inputs.

```javascript
// Test case 1: Array with duplicate values
const duplicates = [4, 2, 4, 1, 3, 2];
selectionSort(duplicates);
console.log('Duplicates sorted:', duplicates);
// Expected: [1, 2, 2, 3, 4, 4]

// Test case 2: Already sorted array
const sorted = [1, 2, 3, 4, 5];
selectionSort(sorted);
console.log('Already sorted:', sorted);
// Expected: [1, 2, 3, 4, 5]

// Test case 3: Reverse sorted array
const reverse = [5, 4, 3, 2, 1];
selectionSort(reverse);
console.log('Reverse sorted:', reverse);
// Expected: [1, 2, 3, 4, 5]

// Test case 4: Single-element array
const single = [42];
selectionSort(single);
console.log('Single element:', single);
// Expected: [42]

// Test case 5: Empty array
const empty = [];
selectionSort(empty);
console.log('Empty array:', empty);
// Expected: []
```

## 8. Conclusion

Selection Sort is a foundational sorting algorithm that, despite its quadratic time complexity, imparts valuable lessons regarding algorithm design, in-place manipulation, and complexity analysis. Its minimal swap count renders it suitable for scenarios where write operations are expensive. Understanding Selection Sort prepares the learner for more advanced sorting techniques such as Insertion Sort, Merge Sort, and Quick Sort, which will be explored in subsequent sections. The algorithm's straightforward implementation serves as an effective exercise for reinforcing programming fundamentals and algorithmic thinking.