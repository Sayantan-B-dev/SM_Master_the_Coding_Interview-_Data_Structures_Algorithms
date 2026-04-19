# Non-Comparison Sorting Algorithms: Counting Sort and Radix Sort

## 1. Introduction

All sorting algorithms examined thus far—Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort—are **comparison-based**. They determine the relative order of elements solely by comparing pairs of elements. A fundamental result in theoretical computer science establishes a lower bound of **Ω(n log n)** for the average-case time complexity of any comparison-based sorting algorithm. Consequently, no comparison sort can achieve better than **O(n log n)** asymptotic performance.

However, this lower bound is predicated on the use of comparisons as the exclusive means of ordering. When additional information about the data is available—specifically, when the keys are integers confined to a known, restricted range—algorithms that **do not rely on comparisons** can circumvent this barrier and achieve **linear time complexity**. Such algorithms are termed **non-comparison sorts**.

This document introduces two prominent non-comparison sorting algorithms: **Counting Sort** and **Radix Sort**. These algorithms exploit the digital representation of integers to sort data without ever comparing two elements against each other. While exceptionally fast under the right conditions, their applicability is limited to specific data types and ranges.

## 2. The Limitations of Comparison-Based Sorting

A decision-tree model demonstrates that any comparison-based sorting algorithm must, in the worst case, perform at least **log₂(n!)** comparisons. By Stirling's approximation, **log₂(n!) ∈ Θ(n log n)**. This mathematical result proves that no comparison sort can achieve sub‑linearithmic average-case complexity.

The algorithms that achieve **O(n log n)**—Merge Sort, Heap Sort, and Quick Sort (on average)—are therefore **asymptotically optimal** within the comparison model. To surpass this bound, one must abandon the comparison model entirely.

## 3. Non-Comparison Sorting: Principles and Prerequisites

Non-comparison sorting algorithms leverage **intrinsic properties** of the data to determine the sorted order without pairwise comparisons. Typically, this involves:

- **Key Type:** The elements to be sorted must be **integers** (or data that can be mapped to integers).
- **Key Range:** The range of possible key values must be **known in advance** and **sufficiently small** relative to the number of elements.

When these prerequisites are met, non-comparison algorithms can sort in **linear time**—**O(n)** or **O(n + k)**, where **k** is the range of input values. The most common non-comparison sorts are **Counting Sort**, **Radix Sort**, and **Bucket Sort**.

### 3.1 Comparison of Applicability

| Algorithm Family     | Applicable Data Types                          | Time Complexity (Average) | Space Complexity |
|----------------------|------------------------------------------------|---------------------------|------------------|
| Comparison Sorts     | Any type with a defined total order            | Ω(n log n)                | Varies           |
| Non-Comparison Sorts | Integers (or mappable) with restricted range   | O(n + k) or O(d·(n+b))    | O(n + k)         |

## 4. Counting Sort

### 4.1 Algorithm Description

Counting Sort operates by determining, for each input element **x**, the number of elements that are **less than x**. This count directly yields the final sorted position of **x**. The algorithm assumes that the input consists of non‑negative integers within a known range **[0, k]**.

**Steps:**

1. Determine the maximum value **k** in the input array.
2. Create an auxiliary **count array** of size **k + 1**, initialized to zero.
3. Traverse the input array and, for each element **x**, increment `count[x]`.
4. Modify the count array such that each element at index **i** stores the cumulative sum of counts up to **i**. After this step, `count[i]` represents the number of elements less than or equal to **i**.
5. Traverse the input array in **reverse order** (to ensure stability) and place each element into its correct position in an output array using the cumulative count. Decrement the count after each placement.

### 4.2 JavaScript Implementation

```javascript
/**
 * Sorts an array of non‑negative integers using Counting Sort.
 * Assumes input values are in the range [0, maxValue].
 *
 * @param {number[]} arr - The array to be sorted.
 * @param {number} maxValue - The maximum value present in the array (optional; computed if omitted).
 * @returns {number[]} A new sorted array.
 */
function countingSort(arr, maxValue = null) {
    if (arr.length === 0) return [];

    // Determine the maximum value if not provided
    const max = maxValue !== null ? maxValue : Math.max(...arr);

    // Step 1: Create and populate count array
    const count = new Array(max + 1).fill(0);
    for (let num of arr) {
        count[num]++;
    }

    // Step 2: Compute cumulative counts (running sum)
    for (let i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    // Step 3: Build output array (stable, by iterating backwards)
    const output = new Array(arr.length);
    for (let i = arr.length - 1; i >= 0; i--) {
        const num = arr[i];
        output[count[num] - 1] = num;
        count[num]--;
    }

    return output;
}

// Example usage
const numbers = [4, 2, 2, 8, 3, 3, 1, 0];
console.log('Counting Sort:', countingSort(numbers));
// Expected output: [0, 1, 2, 2, 3, 3, 4, 8]
```

### 4.3 Complexity Analysis

- **Time Complexity:** **O(n + k)**, where **n** is the number of elements and **k** is the range of input values. When **k = O(n)**, the complexity becomes **O(n)**—linear time.
- **Space Complexity:** **O(n + k)** due to the output array and the count array.

### 4.4 Limitations

- **Integer Keys Only:** Counting Sort requires keys to be non‑negative integers. Arbitrary objects cannot be sorted directly.
- **Range Dependency:** Performance degrades significantly if **k** is much larger than **n** (e.g., sorting 100 elements with values up to 10⁶).
- **Stability:** The reverse traversal ensures stability, but the algorithm is not in‑place.

## 5. Radix Sort

### 5.1 Algorithm Description

Radix Sort addresses the range limitation of Counting Sort by processing integer keys **digit by digit**. Instead of sorting by the entire key at once, Radix Sort repeatedly applies a stable sort (typically Counting Sort) to each digit position, starting from the least significant digit (LSD) or the most significant digit (MSD). The LSD‑first approach is the most common.

**Steps (LSD Radix Sort):**

1. Determine the maximum number in the array to know the number of digits.
2. For each digit position (units, tens, hundreds, etc.):
   - Use a stable sort (e.g., Counting Sort) to sort the array based on the digit at the current position.
3. After processing all digit positions, the array is fully sorted.

Because Counting Sort is stable, the relative order established in previous passes is preserved, ensuring that numbers are correctly ordered by the most significant digits after all passes.

### 5.2 JavaScript Implementation (LSD Radix Sort using Counting Sort)

```javascript
/**
 * Returns the digit at a given place value for a number.
 * @param {number} num - The number.
 * @param {number} place - The place value (1 for units, 10 for tens, etc.).
 * @returns {number} The digit (0-9).
 */
function getDigit(num, place) {
    return Math.floor(Math.abs(num) / place) % 10;
}

/**
 * Counts the number of digits in the largest number in the array.
 * @param {number[]} arr - The array.
 * @returns {number} The maximum digit count.
 */
function digitCount(num) {
    if (num === 0) return 1;
    return Math.floor(Math.log10(Math.abs(num))) + 1;
}

function mostDigits(arr) {
    let maxDigits = 0;
    for (let num of arr) {
        maxDigits = Math.max(maxDigits, digitCount(num));
    }
    return maxDigits;
}

/**
 * Sorts an array of non‑negative integers using LSD Radix Sort.
 *
 * @param {number[]} arr - The array to be sorted.
 * @returns {number[]} A new sorted array.
 */
function radixSort(arr) {
    if (arr.length === 0) return [];

    const maxDigitCount = mostDigits(arr);

    for (let k = 0; k < maxDigitCount; k++) {
        // Create 10 buckets (0-9) for each digit
        const buckets = Array.from({ length: 10 }, () => []);

        // Distribute numbers into buckets based on the k‑th digit
        const place = Math.pow(10, k);
        for (let num of arr) {
            const digit = getDigit(num, place);
            buckets[digit].push(num);
        }

        // Flatten buckets back into the array (stable order)
        arr = [].concat(...buckets);
    }

    return arr;
}

// Example usage
const numbers = [170, 45, 75, 90, 802, 24, 2, 66];
console.log('Radix Sort:', radixSort(numbers));
// Expected output: [2, 24, 45, 66, 75, 90, 170, 802]
```

### 5.3 Complexity Analysis

- **Time Complexity:** **O(d · (n + b))**, where **d** is the number of digits in the maximum element, **n** is the number of elements, and **b** is the base (10 for decimal). If **d** is constant and **b** is constant, the complexity is **O(n)**—linear time.
- **Space Complexity:** **O(n + b)**, due to the buckets used during each counting pass.

### 5.4 Limitations

- **Integer Keys Required:** Like Counting Sort, Radix Sort is designed for integer keys (or data that can be represented as fixed‑length strings/bytes).
- **Overhead for Small Data:** For small arrays, the overhead of multiple passes may outweigh the theoretical linear advantage.
- **Negative Numbers:** Special handling is required for negative integers (e.g., separate negative and positive arrays or using two's complement representation).

## 6. Comparison of Non-Comparison and Comparison Sorts

| Criterion               | Comparison Sorts (Merge, Quick, Heap) | Non‑Comparison Sorts (Counting, Radix) |
|-------------------------|---------------------------------------|----------------------------------------|
| **Data Type**           | Any comparable type                   | Integers (or mappable) with bounded range |
| **Average Time**        | O(n log n)                            | O(n) or O(n + k)                       |
| **Worst‑Case Time**     | O(n log n) or O(n²) (Quick)           | O(n + k) or O(d·(n+b))                 |
| **Space Complexity**    | O(1) to O(n)                          | O(n + k) or O(n + b)                   |
| **Stability**           | Varies (Merge: stable, Quick: unstable)| Counting: stable; Radix: stable        |
| **In‑Place**            | Quick and Heap are in‑place           | Typically not in‑place                 |

## 7. When to Use Non-Comparison Sorts

Non‑comparison sorting algorithms are **not general‑purpose replacements** for comparison sorts. They should be considered only when the following conditions are met:

- The data consists of **integers** or can be mapped to integers (e.g., characters via ASCII codes).
- The **range of possible values is limited** and known in advance.
- **Stability** is required (both Counting Sort and Radix Sort are stable).
- **Linear time performance** is critical and the dataset size is large enough to amortize the constant‑factor overhead.

**Example Scenarios:**

- Sorting exam scores (0–100) for thousands of students.
- Sorting zip codes or area codes in a mailing list.
- Sorting ages or other demographic data with a fixed range.
- Sorting fixed‑length strings in lexicographic order using Radix Sort.

## 8. Conclusion

Comparison-based sorting algorithms are constrained by a theoretical lower bound of **Ω(n log n)**. Non‑comparison algorithms such as Counting Sort and Radix Sort transcend this limitation by exploiting the structure of integer keys within a bounded domain. They can achieve **linear time complexity**—**O(n)**—under favorable conditions. However, their applicability is restricted to specific data types and ranges; they are not universally superior to comparison sorts like Quick Sort or Merge Sort.

Understanding these specialized algorithms enriches one's algorithmic toolkit and provides insight into the tradeoffs between generality and efficiency. In practice, comparison-based sorts remain the default choice for general‑purpose sorting, while non‑comparison sorts are reserved for domains where their prerequisites are satisfied and performance is paramount.