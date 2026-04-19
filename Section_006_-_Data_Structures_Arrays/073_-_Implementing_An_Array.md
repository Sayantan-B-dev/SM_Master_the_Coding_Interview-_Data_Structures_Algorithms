# Implementing a Custom Array Class in JavaScript

## 1. Introduction

While modern programming languages provide built-in array implementations, constructing a custom array class from fundamental principles offers valuable insight into the internal mechanics of this essential data structure. This exercise illuminates the operational complexity of array methods and demonstrates how data structures can be built upon simpler constructs.

This document details the implementation of a custom array class named `MyArray` using JavaScript. The class replicates core array behaviours, including element access, appending, removal from the end, and deletion at arbitrary positions with subsequent index shifting.

---

## 2. Class Structure and Constructor

The `MyArray` class encapsulates the data storage and associated length property. The constructor initialises an empty array state.

```javascript
class MyArray {
    constructor() {
        this.length = 0;   // Tracks the number of elements in the array
        this.data = {};    // Object serving as the underlying storage
    }
}
```

**Explanation:**
- **`length`:** An integer property representing the count of elements currently held.
- **`data`:** A plain JavaScript object where keys are string representations of integer indices (e.g., `"0"`, `"1"`), mimicking contiguous memory slots.

---

## 3. Core Operations Implementation

### 3.1 Access Method: `get(index)`

Retrieves the element at a specified index in constant time, O(1).

```javascript
get(index) {
    // Directly return the value stored at the given index key
    return this.data[index];
}
```

**Time Complexity:** O(1) – Accessing an object property by key is a constant-time operation.

### 3.2 Append Method: `push(item)`

Adds an element to the end of the array, updating the length accordingly.

```javascript
push(item) {
    // Assign the item to the current length index, then increment length
    this.data[this.length] = item;
    this.length++;
    return this.length; // Mimics standard JavaScript push behaviour
}
```

**Time Complexity:** O(1) – A single assignment and increment operation.

### 3.3 Remove Last Method: `pop()`

Removes and returns the last element of the array.

```javascript
pop() {
    const lastItem = this.data[this.length - 1]; // Retrieve the last element
    delete this.data[this.length - 1];           // Remove the property
    this.length--;                               // Decrement length
    return lastItem;
}
```

**Time Complexity:** O(1) – Involves property deletion and length decrement.

### 3.4 Delete Method: `delete(index)`

Removes an element at an arbitrary index. This operation necessitates shifting all subsequent elements one position to the left to maintain contiguous indexing, resulting in linear time complexity.

```javascript
delete(index) {
    const item = this.data[index];           // Store reference to deleted item
    this._shiftItems(index);                 // Helper method to re-index elements
    return item;
}
```

**Helper Method: `_shiftItems(index)`**

Implements the shifting logic required after deletion.

```javascript
_shiftItems(index) {
    // Iterate from the deletion index to the second-last element
    for (let i = index; i < this.length - 1; i++) {
        this.data[i] = this.data[i + 1]; // Shift element leftward
    }
    // Remove the now-duplicate last element and decrement length
    delete this.data[this.length - 1];
    this.length--;
}
```

**Time Complexity:** O(n) – The `for` loop iterates over `n - index` elements; in the worst case (deleting the first element), it traverses the entire array.

---

## 4. Usage Example

The following code demonstrates the complete `MyArray` class in action.

```javascript
// Instantiate a new custom array
const customArray = new MyArray();

// Append elements
customArray.push('Hi');
customArray.push('you');
customArray.push('!');
console.log(customArray); 
// Output: MyArray { length: 3, data: { '0': 'Hi', '1': 'you', '2': '!' } }

// Access an element
console.log(customArray.get(1)); // Output: 'you'

// Remove the last element
console.log(customArray.pop());  // Output: '!'
console.log(customArray); 
// Output: MyArray { length: 2, data: { '0': 'Hi', '1': 'you' } }

// Delete an element at index 0
customArray.delete(0);
console.log(customArray);
// Output: MyArray { length: 1, data: { '0': 'you' } }
```

---

## 5. Operational Complexity Summary

The following table correlates the custom methods with their respective time complexities.

| Method       | Description                                    | Time Complexity |
|--------------|------------------------------------------------|-----------------|
| `get(index)` | Access element by index                        | O(1)            |
| `push(item)` | Append element to end                          | O(1)            |
| `pop()`      | Remove and return last element                 | O(1)            |
| `delete(index)` | Remove element at arbitrary position         | O(n)            |

These complexities align with the theoretical behaviour of static arrays discussed in earlier sections. The O(n) nature of deletion stems from the necessity of shifting elements to preserve contiguous indexing.

---

## 6. Design Considerations

### 6.1 Single Responsibility Principle

The `delete` method delegates the shifting logic to a dedicated helper method `_shiftItems`. This separation adheres to the single responsibility principle, improving code maintainability and readability.

### 6.2 Underlying Storage Mechanism

The use of a plain JavaScript object to simulate array storage highlights a key characteristic of JavaScript arrays: they are essentially objects with integer-based keys. In lower-level languages, arrays occupy contiguous memory blocks, whereas JavaScript abstracts this detail.

### 6.3 Language-Agnostic Applicability

Although implemented in JavaScript, the concepts demonstrated—constructor initialisation, index-based storage, and element shifting—are transferable to other programming languages when constructing custom array-like structures.

---

## 7. Summary

- A custom array class can be implemented using a class definition with properties for `length` and a storage `object`.
- Constant-time operations (`get`, `push`, `pop`) are achieved through direct key access and simple property manipulation.
- Linear-time deletion requires iterating over subsequent elements to shift indices, reflecting the O(n) complexity of insertions and deletions in standard arrays.
- Building data structures from scratch reinforces understanding of their internal behaviour and time complexity characteristics.