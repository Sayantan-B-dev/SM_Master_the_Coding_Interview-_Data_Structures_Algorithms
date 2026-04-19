# Hash Table Operations: Implementation of the `keys()` Method and Performance Considerations

## 1. Introduction

In the previous sections, the foundational components of a custom hash table were established, including the constructor, the hash function, and the essential `set()` and `get()` methods. This section addresses the implementation of an additional utility method: `keys()`. The `keys()` method provides a mechanism to retrieve an array containing all unique keys currently stored within the hash table. This operation is frequently required for tasks such as iterating over the stored entries or validating the contents of the data structure.

## 2. Objective of the `keys()` Method

The `keys()` method is designed to traverse the internal storage array of the hash table, collect all keys present in any non-empty bucket, and return them as a standard JavaScript array. The method serves as an iterator for the keys of the hash table, albeit one that must account for the sparse and unordered nature of the underlying storage.

**Expected Behavior Example:**

```javascript
const ht = new HashTable(50);
ht.set("grapes", 10000);
ht.set("apples", 5000);
ht.set("oranges", 2);

console.log(ht.keys()); // Expected Output: ["grapes", "apples", "oranges"] (order may vary)
```

## 3. Implementation of the `keys()` Method

### 3.1 Algorithmic Steps

The `keys()` method follows a straightforward linear probing approach across the entire storage array:

1. **Initialization:** Create an empty array, conventionally named `keysArray`, to accumulate the extracted keys.
2. **Array Traversal:** Iterate through every index of the internal `this.data` array, from index `0` to `this.size - 1`.
3. **Bucket Inspection:** At each index `i`, check if `this.data[i]` contains a valid bucket (i.e., it is not `undefined` or empty).
4. **Key Extraction:** If a bucket exists, retrieve the first element of each tuple stored within that bucket. In the current implementation, each bucket is an array of tuples in the format `[key, value]`. Therefore, `this.data[i][j][0]` accesses the key of the j-th entry.
5. **Collection:** Append each extracted key to the `keysArray`.
6. **Return Value:** After the loop completes, return the populated `keysArray`.

### 3.2 Code Implementation

The following code block presents the complete implementation of the `keys()` method within the `HashTable` class.

```javascript
class HashTable {
    // ... (constructor, _hash, set, get methods as defined previously)

    keys() {
        // Step 1: Initialize an empty array to hold keys
        const keysArray = [];

        // Step 2: Loop through every index of the storage array (all memory shelves)
        for (let i = 0; i < this.data.length; i++) {
            // Step 3: Check if the current bucket contains any data
            if (this.data[i]) {
                // Step 4: The bucket exists. Iterate through its inner array.
                // Each element in the bucket is a tuple [key, value].
                for (let j = 0; j < this.data[i].length; j++) {
                    // Step 5: Extract the key (first element of the tuple) and add to result
                    keysArray.push(this.data[i][j][0]);
                }
            }
        }

        // Step 6: Return the accumulated array of keys
        return keysArray;
    }
}
```

**Code Explanation:**

- The outer `for` loop iterates over the fixed size of the hash table (e.g., 50 iterations).
- The condition `if (this.data[i])` ensures that processing is only attempted on indices where a bucket has been initialized. This avoids unnecessary iteration over empty slots.
- The inner `for` loop traverses the bucket array at index `i`. This inner loop is necessary because collisions may have caused multiple key-value pairs to be stored at the same index (separate chaining).
- The expression `this.data[i][j][0]` uses three levels of indexing:
  - `this.data[i]`: Accesses the bucket array at index `i`.
  - `this.data[i][j]`: Accesses the j-th tuple within that bucket.
  - `this.data[i][j][0]`: Accesses the key string from that tuple.

### 3.3 Execution Trace

Given the following insertions:

```javascript
ht.set("grapes", 10000);
ht.set("apples", 5000);
ht.set("oranges", 2);
```

When `ht.keys()` is invoked, the loop scans indices 0 through 49. At the indices where the hash function placed "grapes", "apples", and "oranges", the respective buckets are encountered, and their keys are extracted and pushed into `keysArray`. The final array is returned containing the three keys.

## 4. Performance Analysis and Drawbacks

### 4.1 Time Complexity: O(n) where n is the Table Size

The `keys()` method, as implemented, exhibits a time complexity of **O(m + k)**, where:
- **m** is the total number of allocated buckets (`this.size`).
- **k** is the total number of stored key-value pairs.

Since the outer loop always iterates over all `m` buckets regardless of how many entries exist, the operation is bounded by the table size. In practice, this can be inefficient for sparsely populated hash tables with large capacities.

### 4.2 Comparison with Array Iteration

| Data Structure | Iteration Over Keys | Complexity |
| :--- | :--- | :--- |
| **Array** | Loop over actual elements (e.g., `for` loop over length) | O(n) where n = number of elements |
| **Hash Table (Custom)** | Loop over all allocated buckets (including empty ones) | O(size) where size = capacity |

**Illustrative Scenario:**
- An array with 3 elements requires 3 iterations to retrieve all items.
- A hash table with 3 elements but a size of 500 requires 500 iterations to retrieve the same number of keys.

This disparity highlights a fundamental performance trade-off: while hash tables excel at point queries (`get`, `set`, `delete`), they are less efficient for operations that require full traversals of the data structure.

### 4.3 Unordered Nature of Keys

An additional characteristic revealed by the `keys()` method is the **lack of guaranteed order** in hash table iteration. The order of keys in the returned array depends entirely on the hash indices where they were stored. Since the hash function distributes keys pseudo-randomly across the bucket array, and the `keys()` method traverses indices sequentially from 0 to `size - 1`, the resulting order is unrelated to the chronological order of insertion.

**Example:**
```javascript
ht.set("zebra", 1);
ht.set("apple", 2);
ht.set("mango", 3);
console.log(ht.keys()); // Possible output: ["apple", "mango", "zebra"] (order not guaranteed)
```

This behavior contrasts with arrays, which maintain strict insertion order. In modern JavaScript, the native `Map` object preserves insertion order, but the classic hash table abstraction does not inherently provide this guarantee.

## 5. Extensions: Implementing a `values()` Method

By applying the same traversal logic, a companion method named `values()` can be readily implemented. The only modification required is to extract the second element of each tuple (`this.data[i][j][1]`) instead of the key.

```javascript
values() {
    const valuesArray = [];
    for (let i = 0; i < this.data.length; i++) {
        if (this.data[i]) {
            for (let j = 0; j < this.data[i].length; j++) {
                valuesArray.push(this.data[i][j][1]);
            }
        }
    }
    return valuesArray;
}
```

## 6. Summary

- The **`keys()` method** provides a means to retrieve all stored keys from a custom hash table by iterating over the entire underlying storage array and collecting keys from non-empty buckets.
- The implementation involves a **nested loop**: an outer loop scanning the fixed-size array and an inner loop traversing collision chains.
- The time complexity of this approach is **O(size)**, which may be inefficient for large, sparsely populated tables compared to arrays where iteration is O(n) with respect to actual elements.
- The **unordered output** of the `keys()` method underscores the fundamental property that classic hash tables do not maintain insertion order.
- Understanding these operational details enables developers to make informed decisions when selecting data structures for specific tasks, balancing the benefits of O(1) average access against the costs of full traversals.