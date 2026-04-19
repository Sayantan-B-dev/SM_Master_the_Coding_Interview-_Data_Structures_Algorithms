# Array-Based Implementation of a Stack in JavaScript

## 1. Introduction

The **Stack** data structure can be implemented using various underlying storage mechanisms. While a linked list provides dynamic memory allocation with consistent O(1) operations, an **array** offers a simpler and more concise implementation. JavaScript arrays natively support the `push()` and `pop()` methods, which map directly to the standard stack operations. This document presents an array-based stack implementation, highlighting the minimal code required and the trade-offs associated with this approach.

## 2. Advantages of Array-Based Implementation

- **Simplicity**: Leverages built-in JavaScript array methods, eliminating the need for custom node management.
- **Readability**: The code is concise and self-explanatory.
- **Rapid Development**: Requires significantly fewer lines of code compared to a linked list implementation.

## 3. Core Stack Operations Using Arrays

Since JavaScript arrays already provide `push()` and `pop()` methods, the stack implementation reduces to a thin wrapper that enforces the intended LIFO behavior.

| Operation | Array Equivalent | Description |
|-----------|------------------|-------------|
| `push(value)` | `array.push(value)` | Adds an element to the end of the array (top of stack). |
| `pop()` | `array.pop()` | Removes and returns the last element from the array. |
| `peek()` | `array[array.length - 1]` | Returns the last element without removing it. |
| `isEmpty()` | `array.length === 0` | Checks if the stack contains any elements. |

## 4. Implementation

The following `ArrayStack` class encapsulates an internal array and exposes the standard stack interface.

```javascript
/**
 * Stack implementation using a JavaScript array.
 * Provides LIFO behavior with minimal code.
 */
class ArrayStack {
    constructor() {
        this.items = []; // Internal array to store stack elements
    }

    /**
     * Adds an element to the top of the stack.
     * @param {*} value - The element to be pushed.
     * @returns {ArrayStack} The updated stack instance (for chaining).
     */
    push(value) {
        this.items.push(value);
        return this;
    }

    /**
     * Removes and returns the top element from the stack.
     * @returns {*} The removed element, or null if the stack is empty.
     */
    pop() {
        if (this.isEmpty()) {
            return null;
        }
        return this.items.pop();
    }

    /**
     * Returns the top element without removing it.
     * @returns {*} The top element, or null if the stack is empty.
     */
    peek() {
        if (this.isEmpty()) {
            return null;
        }
        return this.items[this.items.length - 1];
    }

    /**
     * Checks whether the stack is empty.
     * @returns {boolean} true if empty, false otherwise.
     */
    isEmpty() {
        return this.items.length === 0;
    }

    /**
     * Returns the number of elements currently in the stack.
     * @returns {number} The size of the stack.
     */
    size() {
        return this.items.length;
    }
}
```

## 5. Example Usage

The array-based stack is used identically to its linked list counterpart.

```javascript
const history = new ArrayStack();

// Visiting web pages
history.push("google.com");
history.push("udemy.com");
history.push("youtube.com");

console.log(history.peek()); // "youtube.com"
console.log(history.size()); // 3

// Navigating back
console.log(history.pop()); // "youtube.com"
console.log(history.pop()); // "udemy.com"
console.log(history.peek()); // "google.com"
console.log(history.isEmpty()); // false

console.log(history.pop()); // "google.com"
console.log(history.isEmpty()); // true
console.log(history.pop()); // null
```

## 6. Time Complexity Analysis

| Operation | Time Complexity | Explanation |
|-----------|-----------------|-------------|
| `push()` | O(1) amortized | Appending to the end of a dynamic array is amortized constant time. Occasional resizing may cause O(n). |
| `pop()` | O(1) | Removing the last element does not require shifting other elements. |
| `peek()` | O(1) | Direct indexed access to the last element. |
| `isEmpty()` | O(1) | Checking the `length` property is constant time. |

## 7. Comparison: Array vs. Linked List Stack

| Aspect | Array-Based Stack | Linked List-Based Stack |
|--------|-------------------|-------------------------|
| Code Complexity | Very simple | Moderate (requires Node class) |
| Memory Overhead | None for references | Extra memory for `next` pointers |
| Dynamic Sizing | Automatic (array resizing) | Inherent (nodes allocated individually) |
| Resizing Cost | Occasional O(n) during reallocation | None |
| Cache Locality | Excellent (contiguous memory) | Poor (scattered nodes) |

## 8. Limitations of Array-Based Implementation

While the array-based stack is simple and efficient for most use cases, it does have a few limitations:

- **Resizing Overhead**: When the internal array reaches capacity, the JavaScript engine must allocate a larger block of memory and copy existing elements. This operation is O(n) but occurs infrequently.
- **Memory Pre-allocation**: Dynamic arrays may allocate more memory than strictly necessary to accommodate future growth, leading to slight memory inefficiency.
- **No Fine-Grained Control**: Developers cannot directly control memory layout or pointer manipulation.

Despite these limitations, the array-based stack is perfectly suitable for the vast majority of applications and is the idiomatic way to implement a stack in JavaScript.

## 9. Summary

Implementing a stack using a JavaScript array is remarkably straightforward due to the language's built-in `push()` and `pop()` methods. The `ArrayStack` class provides a clean, minimal interface while maintaining the expected LIFO behavior. This implementation is ideal for rapid prototyping, educational purposes, and production scenarios where the stack size remains within reasonable bounds. For applications with extreme performance requirements or unbounded growth, a linked list or circular buffer implementation may be considered, but the array-based stack remains the simplest and most practical choice for most JavaScript developers.