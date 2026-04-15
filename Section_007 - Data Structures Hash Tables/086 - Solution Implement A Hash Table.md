# Hash Table Implementation: A Practical Approach

## 1. Introduction

Understanding the internal mechanics of hash tables requires constructing a functional implementation. This documentation presents a step-by-step implementation of a hash table in JavaScript, demonstrating key concepts including hashing algorithms, collision resolution through chaining, and core operations.

## 2. Class Structure and Design Considerations

### 2.1 Private Properties Convention

JavaScript, prior to the introduction of private class fields, lacked native support for truly private properties. A widely adopted convention among developers involves prefixing intended private members with an underscore (`_`).

```javascript
class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }
    
    _hash(key) {
        // Private method by convention
    }
}
```

This underscore notation signals to other developers that the method or property should not be accessed externally, despite being technically accessible.

### 2.2 Constructor and Storage Allocation

The constructor initializes the hash table with a predetermined number of storage locations (buckets). The `data` property holds an array representing available memory slots.

```javascript
constructor(size) {
    this.data = new Array(size);
}
```

## 3. The Hash Function Implementation

The hash function transforms an input key into a numeric index within the allocated storage bounds.

### 3.1 Algorithm Description

The implemented hash function performs the following operations:

1. Initialize a hash accumulator to zero
2. Iterate through each character of the key string
3. Obtain the Unicode character code for each character
4. Combine the character code with its position index
5. Apply modulo operation to constrain the result within array bounds

```javascript
_hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
        // charCodeAt() returns UTF-16 code unit (0-65535)
        // Multiplying by index i increases uniqueness
        hash = (hash + key.charCodeAt(i) * i) % this.data.length;
    }
    return hash;
}
```

### 3.2 Execution Example

For the key `"grapes"`, the function processes characters sequentially:

| Iteration (i) | Character | charCodeAt(i) | Calculation |
|---------------|-----------|---------------|-------------|
| 0 | 'g' | 103 | (0 + 103 × 0) % size |
| 1 | 'r' | 114 | (previous + 114 × 1) % size |
| 2 | 'a' | 97 | (previous + 97 × 2) % size |
| 3 | 'p' | 112 | (previous + 112 × 3) % size |
| 4 | 'e' | 101 | (previous + 101 × 4) % size |
| 5 | 's' | 115 | (previous + 115 × 5) % size |

The final result is an integer index between `0` and `size - 1`.

## 4. The Set Method: Inserting Key-Value Pairs

The `set` method stores a key-value pair at the address determined by the hash function.

### 4.1 Implementation with Collision Handling

Collisions occur when different keys produce identical hash values. The implementation resolves collisions through **separate chaining**, where each bucket contains an array of entries.

```javascript
set(key, value) {
    // Step 1: Compute storage address using hash function
    const address = this._hash(key);
    
    // Step 2: Initialize bucket if it does not exist
    if (!this.data[address]) {
        this.data[address] = [];
    }
    
    // Step 3: Push key-value pair as a sub-array
    this.data[address].push([key, value]);
    
    return this.data;
}
```

### 4.2 Collision Resolution Visualization

When multiple keys hash to the same address, entries are appended to the bucket array:

```
Hash Table with size = 2
-------------------------
Address 0: [ ["grapes", 10000], ["apples", 54] ]
Address 1: [ ["oranges", 200] ]
```

## 5. The Get Method: Retrieving Values

The `get` method locates and returns the value associated with a given key.

### 5.1 Implementation Logic

```javascript
get(key) {
    // Step 1: Determine the storage address
    const address = this._hash(key);
    
    // Step 2: Access the bucket at computed address
    const currentBucket = this.data[address];
    
    // Step 3: Verify bucket existence
    if (currentBucket) {
        // Step 4: Linear search within the bucket
        for (let i = 0; i < currentBucket.length; i++) {
            // Each entry is [key, value] pair
            if (currentBucket[i][0] === key) {
                return currentBucket[i][1];
            }
        }
    }
    
    // Step 5: Key not found
    return undefined;
}
```

### 5.2 Retrieval Process Example

For a query `get("grapes")` in a table with collisions:

```
1. _hash("grapes") → returns address 0
2. currentBucket = [ ["grapes", 10000], ["apples", 54] ]
3. Iterate bucket:
   - i=0: currentBucket[0][0] === "grapes" → true
   - Return currentBucket[0][1] = 10000
```

## 6. Time Complexity Analysis

### 6.1 Operation Complexities

| Operation | Average Case | Worst Case | Explanation |
|-----------|--------------|------------|-------------|
| `_hash(key)` | O(1) | O(k) | k = key length; typically negligible |
| `set(key, value)` | O(1) | O(1) | Direct array push operation |
| `get(key)` | O(1) | O(n) | Linear search through bucket entries |

### 6.2 Factors Affecting Performance

The worst-case O(n) retrieval occurs under two adverse conditions:

- **Poor hash function distribution**: Concentrates entries into few buckets
- **High load factor with small table size**: Increases collision probability

In well-designed hash tables, these conditions are mitigated through:

- Effective hash functions with uniform distribution
- Dynamic resizing when load factor exceeds threshold
- Optimal initial capacity selection

### 6.3 Practical Considerations

Despite the theoretical possibility of O(n) degradation, practical hash table implementations maintain near-constant time performance. The linear search within buckets operates on collision lists that remain short under normal operating conditions.

## 7. Complete Implementation Example

```javascript
class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }

    set(key, value) {
        const address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        }
        this.data[address].push([key, value]);
        return this.data;
    }

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
}

// Usage demonstration
const myHashTable = new HashTable(50);
myHashTable.set('grapes', 10000);
myHashTable.set('apples', 54);
console.log(myHashTable.get('grapes')); // Output: 10000
```

## 8. Limitations and Future Enhancements

The current implementation lacks several features present in production-grade hash tables:

- **Keys method**: Returning all stored keys requires traversing the entire data structure
- **Deletion operation**: Removing entries from buckets
- **Dynamic resizing**: Expanding capacity when load factor increases
- **Load factor monitoring**: Tracking utilization ratio

These enhancements are addressed in subsequent implementations to achieve a fully functional hash table data structure.

## 9. Summary

The implemented hash table demonstrates fundamental principles:

- **Hashing**: Transformation of keys to array indices via a deterministic function
- **Collision Resolution**: Separate chaining using arrays within buckets
- **Core Operations**: O(1) average-case insertion and retrieval

Understanding this implementation provides insight into the internal mechanisms of hash-based data structures across programming languages and frameworks.