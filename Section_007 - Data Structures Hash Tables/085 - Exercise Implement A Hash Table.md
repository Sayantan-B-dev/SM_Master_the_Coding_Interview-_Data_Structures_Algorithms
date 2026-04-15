# Implementation of a Custom Hash Table in JavaScript

## 1. Objective and Scope

The purpose of this exercise is to construct a functional hash table data structure from fundamental principles using the JavaScript programming language. Although JavaScript provides native object and `Map` implementations that serve as built-in hash tables, implementing a custom version elucidates the underlying mechanics of hashing, bucket storage, and key-value association.

This implementation will include:

- A **constructor** to initialize the storage capacity.
- A **hash function** to generate deterministic numeric indices from string keys.
- A **`set(key, value)`** method to insert or update entries.
- A **`get(key)`** method to retrieve stored values.

## 2. Class Structure and Constructor

The hash table is encapsulated within a class. The constructor accepts a `size` parameter that defines the total number of available memory slots (buckets). This size corresponds to the fixed length of the underlying array used for data storage.

```javascript
class HashTable {
    constructor(size) {
        // Define the total number of memory shelves (buckets)
        this.size = size;
        
        // Initialize the storage array. Each index will eventually hold a bucket.
        // Initially, all entries are set to undefined.
        this.data = new Array(size);
    }
    
    // Additional methods will be defined here...
}
```

**Key Points:**

- `this.size`: Represents the fixed capacity of the hash table. A well-chosen size influences collision probability.
- `this.data`: An array that serves as the primary storage container. Each element at a valid index will hold a **bucket**, which is itself a structure (typically an array or linked list) containing the key-value pairs that hash to that index.

## 3. The Hash Function

### 3.1 Purpose and Requirements

A hash function is a deterministic algorithm that maps an input key (of arbitrary length) to an integer within the range `[0, size - 1]`. For this implementation, a minimal hash function is provided to demonstrate the core concept without introducing unnecessary complexity.

### 3.2 Provided Hash Function Implementation

The following hash function operates on string keys. It iterates over each character, accumulating a numeric value, and then applies the modulo operator to ensure the result falls within the bounds of the storage array.

```javascript
_hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
        // Combine the character code of each letter into a cumulative hash value
        hash = (hash + key.charCodeAt(i) * i) % this.size;
    }
    return hash;
}
```

**Explanation of Operation:**

- **Initialization:** A variable `hash` is initialized to `0`.
- **Iteration:** The function loops through each character of the input `key` string.
- **Accumulation:** For each character at index `i`, the expression `key.charCodeAt(i) * i` multiplies the Unicode value of the character by its position. This reduces the likelihood of collisions for anagrams (e.g., "grapes" vs. "grapse").
- **Modulo Constraint:** The `% this.size` operation ensures that the resulting integer is always a valid index within the array bounds `[0, size - 1]`.

**Deterministic Behavior Example:**

```javascript
const ht = new HashTable(50);
console.log(ht._hash("grapes"));  // Output: 23 (consistent across calls)
console.log(ht._hash("grapess")); // Output: A different value within 0-49
console.log(ht._hash("apples"));  // Output: Another distinct index
```

## 4. Internal Data Organization: Buckets

Unlike a simple array where each index holds a single value, a hash table index (bucket) must accommodate potential collisions. In this implementation, each bucket is represented as a **sub-array** (or list) that stores one or more key-value pairs.

**ASCII Representation of the Data Structure:**

```
Index:   [0]    [1]    [2]    ...    [23]                 ...    [49]
          |      |      |             |                           |
          null   null   null          +---------------------------+
                                       |
                                       v
                              [ ["grapes", 10000] ]
                              
                              (After collision at index 23)
                                       |
                                       v
                              [ ["grapes", 10000], ["apples", 5000] ]
```

- When a key-value pair is inserted, the hash function computes an index (e.g., `23`).
- The bucket at `this.data[23]` is examined:
  - If it is empty (`undefined` or `null`), a new bucket array is created containing a single tuple `[key, value]`.
  - If a bucket already exists, the method checks for an existing entry with the same key. If found, the value is updated; otherwise, a new tuple is appended to the bucket array.

## 5. Method Specifications

### 5.1 The `set(key, value)` Method

**Purpose:** Inserts a new key-value pair into the hash table or updates the value if the key already exists.

**Algorithmic Steps:**

1. Compute the hash index using `_hash(key)`.
2. Access the bucket at `this.data[index]`.
3. If the bucket is empty, initialize it as a new array containing a single tuple `[key, value]`.
4. If the bucket is not empty:
   - Iterate through the existing tuples.
   - If a tuple with the matching `key` is found, update its `value` and exit.
   - If no match is found after iteration, append a new tuple `[key, value]` to the bucket.

**Implementation Skeleton (To be completed):**

```javascript
set(key, value) {
    const address = this._hash(key);
    
    // If bucket does not exist, create it
    if (!this.data[address]) {
        this.data[address] = [];
    }
    
    // Check for existing key within the bucket
    for (let i = 0; i < this.data[address].length; i++) {
        if (this.data[address][i][0] === key) {
            this.data[address][i][1] = value;
            return;
        }
    }
    
    // Key not found; append new entry
    this.data[address].push([key, value]);
}
```

### 5.2 The `get(key)` Method

**Purpose:** Retrieves the value associated with a given key. Returns `undefined` if the key does not exist.

**Algorithmic Steps:**

1. Compute the hash index using `_hash(key)`.
2. Access the bucket at `this.data[index]`.
3. If the bucket is empty, return `undefined`.
4. If the bucket exists:
   - Iterate through the tuples within the bucket.
   - If a tuple with the matching `key` is found, return the associated `value`.
5. If the loop completes without a match, return `undefined`.

**Implementation Skeleton (To be completed):**

```javascript
get(key) {
    const address = this._hash(key);
    const currentBucket = this.data[address];
    
    if (currentBucket) {
        for (let i = 0; i < currentBucket.length; i++) {
            if (currentBucket[i][0] === key) {
                return currentBucket[i][1];
            }
        }
    }
    
    return undefined;
}
```

## 6. Expected Behavior and Testing

Upon successful implementation, the custom hash table should exhibit the following behavior:

```javascript
const myHashTable = new HashTable(50);

// Insertion
myHashTable.set("grapes", 10000);
myHashTable.set("apples", 5000);

// Retrieval
console.log(myHashTable.get("grapes")); // Output: 10000
console.log(myHashTable.get("apples")); // Output: 5000
console.log(myHashTable.get("oranges")); // Output: undefined

// Update
myHashTable.set("grapes", 15000);
console.log(myHashTable.get("grapes")); // Output: 15000
```

## 7. Considerations and Limitations

The provided implementation, while illustrative, contains intentional simplifications:

- **Hash Function Quality:** The `_hash` function is rudimentary and may produce frequent collisions for certain key patterns. Production-grade hash functions employ more sophisticated algorithms to achieve uniform distribution.
- **Collision Handling:** Separate chaining using arrays is implemented. In high-collision scenarios, retrieval time may degrade to O(n) within a bucket.
- **Dynamic Resizing:** The current implementation uses a fixed `size`. A complete hash table would incorporate a load factor threshold and a resize mechanism to rehash entries when the table becomes too dense.

## 8. Summary

- A custom hash table can be constructed using an array of **buckets**, where each bucket stores key-value pairs that hash to the same index.
- The **hash function** converts a string key into a numeric index within the bounds of the storage array.
- The **`set`** method handles both insertion and update by checking for key existence within the bucket.
- The **`get`** method searches the bucket at the computed index and returns the corresponding value or `undefined`.
- This exercise reinforces understanding of hash table internals, including index generation, collision management, and the constant-time average-case access property.