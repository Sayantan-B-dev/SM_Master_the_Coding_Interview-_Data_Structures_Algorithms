# Linear Search

## 1. Introduction to Linear Search

Linear search, also referred to as sequential search, is a fundamental searching algorithm in computer science. It operates by systematically examining each element within a collection, one after another, until either the desired target value is located or the entire collection has been exhausted without success.

This algorithm is among the most intuitive search methods, as it mimics the natural human approach of scanning items in a list sequentially. Despite its conceptual simplicity, linear search remains a valid algorithmic choice under specific conditions, particularly when dealing with unsorted data or small datasets.

---

## 2. Algorithm Description

The linear search algorithm follows a straightforward, iterative procedure:

1. Begin at the first element of the collection
2. Compare the current element with the target value
3. If a match is found, return the position (index) of the element
4. If no match is found, advance to the next element
5. Repeat steps 2 through 4 until either a match is discovered or the end of the collection is reached
6. If the entire collection is traversed without finding the target, return an indication of failure (e.g., -1 or null)

This process ensures that every element is examined at most once during the search operation.

---

## 3. Visual Representation

A sequential scan of a list can be illustrated as follows:

```
Index:   0     1     2     3     4     5
       +-----+-----+-----+-----+-----+-----+
Value: |  6  | 12  |  8  |  4  |  9  | 15  |
       +-----+-----+-----+-----+-----+-----+

Searching for target = 9:

Step 1: Check index 0 (value 6) → Not a match
Step 2: Check index 1 (value 12) → Not a match
Step 3: Check index 2 (value 8) → Not a match
Step 4: Check index 3 (value 4) → Not a match
Step 5: Check index 4 (value 9) → Match found, return index 4
```

The algorithm proceeds sequentially from left to right, requiring five comparisons in this example to locate the target.

---

## 4. Time Complexity Analysis

The performance characteristics of linear search are directly proportional to the size of the input collection.

| Case | Description | Number of Comparisons | Big-O Notation |
|------|-------------|----------------------|----------------|
| **Best Case** | Target is the first element | 1 | O(1) |
| **Worst Case** | Target is the last element or not present | n | O(n) |
| **Average Case** | Target is equally likely to be anywhere | (n+1)/2 | O(n) |

**Explanation:**

- **Best Case:** The algorithm terminates immediately upon finding the target at the initial position. This occurs with probability 1/n for a uniformly distributed search target.

- **Worst Case:** When the target resides at the final position or is entirely absent from the collection, every element must be examined. The algorithm performs n comparisons before concluding.

- **Average Case:** Assuming a successful search where the target exists and all positions are equally probable, the expected number of comparisons is the arithmetic mean of all possible positions: (1 + 2 + ... + n)/n = (n+1)/2, which still grows linearly with n.

---

## 5. Implementation in JavaScript

JavaScript provides several built-in methods that implement linear search under the hood. The following examples demonstrate both native implementations and a manual implementation.

### 5.1 Built-in Linear Search Methods

```javascript
// Sample dataset
const beasts = ['Ant', 'Bison', 'Camel', 'Duck', 'Godzilla', 'Elephant'];

// Method 1: indexOf() - returns first index or -1
const indexGodzilla = beasts.indexOf('Godzilla');
console.log(indexGodzilla); // Output: 4

// Method 2: findIndex() - uses callback function
const findIndexResult = beasts.findIndex(item => item === 'Godzilla');
console.log(findIndexResult); // Output: 4

// Method 3: find() - returns the actual element
const findResult = beasts.find(item => item === 'Godzilla');
console.log(findResult); // Output: 'Godzilla'

// Method 4: includes() - returns boolean existence
const includesResult = beasts.includes('Godzilla');
console.log(includesResult); // Output: true
```

### 5.2 Manual Implementation

A custom linear search function provides explicit control over the search logic:

```javascript
/**
 * Performs a linear search on an array to locate a target value.
 * @param {Array} array - The array to search within.
 * @param {*} target - The value to locate.
 * @returns {number} - The index of the target if found; otherwise -1.
 */
function linearSearch(array, target) {
    // Iterate through each element sequentially
    for (let i = 0; i < array.length; i++) {
        // Compare current element with target
        if (array[i] === target) {
            return i;  // Target found, return its position
        }
    }
    
    // Target not present in the array
    return -1;
}

// Example usage
const numbers = [6, 12, 8, 4, 9, 15];
const position = linearSearch(numbers, 9);
console.log(position); // Output: 4
```

---

## 6. Limitations and Considerations

### 6.1 Performance Constraints

Linear search operates with O(n) time complexity, which becomes prohibitively expensive as dataset sizes grow into millions or billions of elements. Applications such as web search engines, social network friend lookups, and large-scale database queries cannot rely on linear search due to its inefficiency with massive data volumes.

### 6.2 The Significance of Sorted Data

The linear search algorithm makes no assumptions about the ordering of elements within the collection. Consequently, it cannot exploit any inherent structure that might accelerate the search process. If the data were arranged in a sorted order, alternative algorithms could leverage this property to achieve significantly faster search times, often reducing complexity to O(log n).

This observation motivates the study of more sophisticated search algorithms, such as binary search, which are specifically designed to operate on ordered collections and provide exponential improvements in search efficiency.

---

## 7. Summary

Linear search is a foundational algorithm characterized by its simplicity and universal applicability to any list-based data structure. While its O(n) time complexity renders it unsuitable for large-scale or performance-critical applications, it remains a valid choice for small datasets and serves as an essential pedagogical stepping stone toward understanding more advanced searching techniques. The recognition of its limitations directly informs the need for optimized algorithms that exploit sorted data structures to achieve superior performance.