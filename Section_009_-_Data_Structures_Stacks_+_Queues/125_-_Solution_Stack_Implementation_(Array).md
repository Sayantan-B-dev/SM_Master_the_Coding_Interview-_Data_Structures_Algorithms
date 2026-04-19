# Array-Based Implementation of a Stack in JavaScript

## 1. Introduction

The stack data structure, characterized by Last-In-First-Out (LIFO) behavior, can be implemented efficiently using the built-in array type available in JavaScript. Arrays in JavaScript natively provide methods such as `push()` and `pop()` that align precisely with stack operations. This document details the conversion of a linked list-based stack implementation to an array-based approach, emphasizing the reduction in code complexity and the inherent advantages of leveraging language-native data structures.

## 2. Modifications to the Constructor

In the linked list implementation, the constructor initializes `top`, `bottom`, and `length` properties. With an array-based approach, these properties are replaced by a single internal array.

### 2.1 Original Constructor (Linked List)

```javascript
constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
}
```

### 2.2 Modified Constructor (Array)

```javascript
constructor() {
    this.array = []; // Internal array to store stack elements
}
```

**Rationale:**
- The `length` property is automatically maintained by the JavaScript array and can be accessed via `this.array.length`.
- The concepts of `top` and `bottom` become implicit: the top of the stack corresponds to the last element of the array, and the bottom corresponds to the first element.

## 3. Implementation of Core Operations

### 3.1 Peek Operation

The `peek()` method returns the element at the top of the stack without removing it. In an array representation, this is the element at the highest index.

```javascript
/**
 * Returns the top element without removal.
 * @returns {*} The top element, or undefined if stack is empty.
 */
peek() {
    return this.array[this.array.length - 1];
}
```

**Explanation:**
- Arrays in JavaScript are zero-indexed. The index of the last element is `length - 1`.
- If the array is empty, accessing `array[-1]` returns `undefined`.

### 3.2 Push Operation

The `push()` method appends a new element to the top of the stack. The built-in `Array.prototype.push()` method performs this operation in amortized constant time.

```javascript
/**
 * Adds an element to the top of the stack.
 * @param {*} value - The element to be pushed.
 * @returns {ArrayStack} The stack instance for method chaining.
 */
push(value) {
    this.array.push(value);
    return this;
}
```

**Explanation:**
- The native `push()` method adds one or more elements to the end of an array and returns the new length.
- Returning `this` enables fluent interface chaining.

### 3.3 Pop Operation

The `pop()` method removes and returns the top element. The built-in `Array.prototype.pop()` method directly fulfills this requirement.

```javascript
/**
 * Removes and returns the top element.
 * @returns {*} The removed element, or undefined if stack is empty.
 */
pop() {
    return this.array.pop();
}
```

**Explanation:**
- The native `pop()` method removes the last element from an array and returns that element.
- If the array is empty, `pop()` returns `undefined`.

### 3.4 isEmpty Operation (Optional)

Although the `length` property can be checked directly, an `isEmpty()` method improves readability and abstraction.

```javascript
/**
 * Checks if the stack is empty.
 * @returns {boolean} true if stack contains no elements, false otherwise.
 */
isEmpty() {
    return this.array.length === 0;
}
```

## 4. Complete Array-Based Stack Implementation

The following code consolidates all methods into the `ArrayStack` class.

```javascript
/**
 * Stack implementation using a native JavaScript array.
 */
class ArrayStack {
    constructor() {
        this.array = [];
    }

    peek() {
        return this.array[this.array.length - 1];
    }

    push(value) {
        this.array.push(value);
        return this;
    }

    pop() {
        return this.array.pop();
    }

    isEmpty() {
        return this.array.length === 0;
    }

    size() {
        return this.array.length;
    }
}
```

## 5. Example Usage and Verification

The following example demonstrates the array-based stack in action, mirroring the behavior of the linked list version.

```javascript
const myStack = new ArrayStack();

// Pushing elements
myStack.push("google");
myStack.push("udemy");
myStack.push("discord");

console.log(myStack.peek()); // Output: "discord"

// Popping elements
console.log(myStack.pop()); // Output: "discord"
console.log(myStack.pop()); // Output: "udemy"
console.log(myStack.peek()); // Output: "google"
console.log(myStack.pop()); // Output: "google"

console.log(myStack.isEmpty()); // Output: true
console.log(myStack.pop());     // Output: undefined
```

## 6. Advantages of Array-Based Implementation

- **Simplicity**: The code is reduced to a minimal set of wrapper methods around native array operations.
- **Readability**: The implementation is self-documenting and easier for new developers to understand.
- **Performance**: JavaScript engines heavily optimize array methods, providing excellent real-world performance.
- **No Node Management Overhead**: Eliminates the need for a separate `Node` class and manual pointer manipulation.

## 7. Time Complexity

| Operation | Time Complexity | Notes |
|-----------|-----------------|-------|
| `push()`  | O(1) amortized  | Array resizing may occasionally cause O(n) copy. |
| `pop()`   | O(1)            | Removal from end does not shift elements. |
| `peek()`  | O(1)            | Direct indexed access. |
| `isEmpty()` | O(1)          | Simple length check. |

## 8. Summary

Converting a stack implementation from a linked list to an array in JavaScript results in a significant reduction in code volume and complexity. By leveraging the language's built-in array methods, developers can create a fully functional stack with minimal effort. This approach is both efficient and idiomatic for JavaScript applications, making it the preferred choice for most use cases where a stack is required.