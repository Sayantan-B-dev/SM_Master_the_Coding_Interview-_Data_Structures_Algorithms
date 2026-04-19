# Implementation Analysis of Stacks and Queues: Arrays versus Linked Lists

## 1. Introduction

Stacks and Queues are abstract data types that define a set of behavioral operations without prescribing a specific underlying implementation. In practice, both structures can be constructed using either **arrays** or **linked lists**. While both approaches are functionally viable for stacks, the choice of underlying data structure carries significant performance implications, particularly for queues. This document examines the trade-offs associated with each implementation strategy and provides clear guidance for selecting the appropriate foundation based on operational requirements.

## 2. Stack Implementation Considerations

A stack adheres to the **Last-In-First-Out (LIFO)** principle. Operations are confined to the top of the structure, making both array-based and linked list-based implementations efficient and straightforward.

### 2.1 Array-Based Stack

**Advantages:**

- **Cache Locality**: Array elements reside in contiguous memory locations. This spatial locality allows the CPU cache to pre-fetch adjacent elements, resulting in faster access times during traversal or repeated operations.
- **Memory Efficiency**: Arrays do not require additional storage for pointers or references to subsequent nodes.
- **Simplicity**: Implementation logic is minimal and does not involve managing dynamic node allocations.

**Disadvantages:**

- **Fixed Capacity (Static Arrays)**: A predetermined maximum size may lead to overflow if exceeded.
- **Resizing Overhead (Dynamic Arrays)**: When capacity is reached, the array must be reallocated and elements copied to a new memory block. This operation costs **O(n)** time, though it occurs infrequently, yielding an amortized **O(1)** push cost.

### 2.2 Linked List-Based Stack

**Advantages:**

- **Truly Dynamic Size**: The stack can grow and shrink without pre-allocation, limited only by available heap memory.
- **No Resizing Penalty**: Each element is allocated individually, eliminating the need for bulk memory reallocation.

**Disadvantages:**

- **Memory Overhead**: Each node requires additional memory to store a reference (pointer) to the next node.
- **Scattered Memory Allocation**: Nodes may be dispersed throughout memory, reducing cache efficiency and potentially increasing access latency.

### 2.3 Comparative Summary for Stacks

| Criterion | Array-Based Stack | Linked List-Based Stack |
|-----------|-------------------|-------------------------|
| Push/Pop Complexity | O(1) amortized | O(1) |
| Memory Usage | Contiguous, no pointer overhead | Extra memory per node for references |
| Cache Performance | Excellent | Moderate |
| Dynamic Growth | Requires occasional resizing | Inherently dynamic |

**Conclusion for Stacks:** Both implementations are acceptable. The choice hinges on whether predictable memory usage and cache performance (favoring arrays) or unbounded growth without resizing penalties (favoring linked lists) aligns with application priorities.

## 3. Queue Implementation Considerations

A queue follows the **First-In-First-Out (FIFO)** principle. Elements are inserted at the rear and removed from the front. This access pattern reveals a critical inefficiency when a naive array implementation is employed.

### 3.1 The Problem with Naive Array-Based Queues

Consider a queue containing the elements `[Matt, Joy, Samir, Pavel]` implemented in a standard array:

```
Indices: 0      1      2      3
         Matt   Joy   Samir  Pavel
         ↑                    ↑
       Front                 Rear
```

When `Matt` is dequeued (removed from the front), the element at index 0 becomes vacant. To maintain the queue's logical order and keep the front at index 0, **all remaining elements must shift one position to the left**:

```
After dequeue:
Indices: 0     1      2      3
         Joy   Samir Pavel  (empty)
         ↑           ↑
       Front        Rear
```

This shifting operation requires iterating over every element, resulting in **O(n)** time complexity for each dequeue operation. For applications with frequent insertions and removals, this linear cost is prohibitively expensive.

### 3.2 Efficient Queue Implementations

To achieve **O(1)** time complexity for both enqueue and dequeue operations, two primary alternatives exist:

- **Circular Array (Ring Buffer)**: Uses an array with front and rear pointers that wrap around the end using modulo arithmetic. No shifting occurs; pointers simply advance.
- **Linked List**: Maintains references to both the head (front) and tail (rear) of a singly linked list. Removal from the head and insertion at the tail are constant-time operations.

### 3.3 Linked List-Based Queue

The linked list approach eliminates the shifting problem entirely. The queue maintains two pointers:

- `head` (or `front`): points to the first node.
- `tail` (or `rear`): points to the last node.

When an element is dequeued, the `head` pointer is simply advanced to the next node. No other elements are affected.

```
Initial Queue (Linked List):
Head -> [Matt] -> [Joy] -> [Samir] -> [Pavel] <- Tail

After dequeue (Matt removed):
Head -> [Joy] -> [Samir] -> [Pavel] <- Tail
```

Both enqueue and dequeue operations execute in **O(1)** time.

### 3.4 Comparative Summary for Queues

| Criterion | Naive Array Queue | Circular Array Queue | Linked List Queue |
|-----------|-------------------|----------------------|-------------------|
| Enqueue Complexity | O(1) | O(1) | O(1) |
| Dequeue Complexity | O(n) | O(1) | O(1) |
| Memory Overhead | None | None | Extra pointer per node |
| Capacity Limit | Fixed | Fixed | Dynamic |

**Conclusion for Queues:** A naive array implementation is **inefficient and should be avoided** for any performance-sensitive application. For fixed-size scenarios, a circular array provides optimal cache performance with O(1) operations. For unbounded queues, a linked list is the preferred choice due to its dynamic nature and constant-time operations.

## 4. JavaScript Implementation Examples

The following code examples demonstrate both stack and queue implementations in JavaScript, illustrating the concepts discussed.

### 4.1 Stack Implementation (Linked List)

```javascript
/**
 * Stack implementation using a singly linked list in JavaScript.
 * Provides O(1) push and pop operations.
 */
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedListStack {
    constructor() {
        this.top = null;
        this.size = 0;
    }

    /**
     * Pushes a new element onto the top of the stack.
     * @param {*} value - The element to add.
     */
    push(value) {
        const newNode = new Node(value);
        newNode.next = this.top; // Link new node to current top
        this.top = newNode;      // Update top to new node
        this.size++;
    }

    /**
     * Removes and returns the top element.
     * @returns {*} The removed element, or undefined if empty.
     */
    pop() {
        if (this.isEmpty()) {
            return undefined;
        }
        const value = this.top.value;
        this.top = this.top.next; // Move top to next node
        this.size--;
        return value;
    }

    /**
     * Returns the top element without removal.
     * @returns {*} The top element, or undefined if empty.
     */
    peek() {
        return this.isEmpty() ? undefined : this.top.value;
    }

    /**
     * Checks if the stack is empty.
     * @returns {boolean} True if empty, false otherwise.
     */
    isEmpty() {
        return this.top === null;
    }

    /**
     * Returns the number of elements in the stack.
     * @returns {number} The size of the stack.
     */
    getSize() {
        return this.size;
    }
}

// Example usage:
// const historyStack = new LinkedListStack();
// historyStack.push("google.com");
// historyStack.push("udemy.com");
// historyStack.push("youtube.com");
// console.log(historyStack.pop()); // "youtube.com"
```

### 4.2 Queue Implementation (Linked List)

```javascript
/**
 * Queue implementation using a singly linked list with tail pointer.
 * Provides O(1) enqueue and dequeue operations.
 */
class QueueNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedListQueue {
    constructor() {
        this.front = null; // Head of the queue
        this.rear = null;  // Tail of the queue
        this.size = 0;
    }

    /**
     * Adds an element to the rear of the queue.
     * @param {*} value - The element to enqueue.
     */
    enqueue(value) {
        const newNode = new QueueNode(value);
        if (this.isEmpty()) {
            this.front = newNode;
            this.rear = newNode;
        } else {
            this.rear.next = newNode; // Link current tail to new node
            this.rear = newNode;      // Update tail to new node
        }
        this.size++;
    }

    /**
     * Removes and returns the element at the front of the queue.
     * @returns {*} The dequeued element, or undefined if empty.
     */
    dequeue() {
        if (this.isEmpty()) {
            return undefined;
        }
        const value = this.front.value;
        this.front = this.front.next; // Advance front pointer
        if (this.front === null) {
            this.rear = null; // Queue became empty, update rear as well
        }
        this.size--;
        return value;
    }

    /**
     * Returns the front element without removal.
     * @returns {*} The front element, or undefined if empty.
     */
    peek() {
        return this.isEmpty() ? undefined : this.front.value;
    }

    /**
     * Checks if the queue is empty.
     * @returns {boolean} True if empty, false otherwise.
     */
    isEmpty() {
        return this.front === null;
    }

    /**
     * Returns the number of elements in the queue.
     * @returns {number} The size of the queue.
     */
    getSize() {
        return this.size;
    }
}

// Example usage:
// const waitlist = new LinkedListQueue();
// waitlist.enqueue("Matt");
// waitlist.enqueue("Joy");
// waitlist.enqueue("Samir");
// console.log(waitlist.dequeue()); // "Matt"
// console.log(waitlist.peek());    // "Joy"
```

### 4.3 Alternative: Circular Array Queue Implementation

For completeness, a circular array implementation in JavaScript is provided to demonstrate O(1) dequeue without element shifting.

```javascript
/**
 * Queue implementation using a circular array (ring buffer).
 * Provides O(1) enqueue and dequeue operations with fixed capacity.
 */
class CircularArrayQueue {
    constructor(capacity) {
        this.capacity = capacity;
        this.queue = new Array(capacity);
        this.front = 0;
        this.rear = -1;
        this.currentSize = 0;
    }

    /**
     * Adds an element to the rear of the queue.
     * @param {*} value - The element to enqueue.
     * @throws {Error} If queue is full.
     */
    enqueue(value) {
        if (this.currentSize === this.capacity) {
            throw new Error("Queue Overflow: Cannot enqueue, queue is full.");
        }
        this.rear = (this.rear + 1) % this.capacity; // Wrap around
        this.queue[this.rear] = value;
        this.currentSize++;
    }

    /**
     * Removes and returns the element at the front.
     * @returns {*} The dequeued element.
     * @throws {Error} If queue is empty.
     */
    dequeue() {
        if (this.isEmpty()) {
            throw new Error("Queue Underflow: Cannot dequeue, queue is empty.");
        }
        const value = this.queue[this.front];
        this.front = (this.front + 1) % this.capacity; // Advance front with wrap
        this.currentSize--;
        return value;
    }

    /**
     * Returns the front element without removal.
     * @returns {*} The front element, or undefined if empty.
     */
    peek() {
        return this.isEmpty() ? undefined : this.queue[this.front];
    }

    /**
     * Checks if the queue is empty.
     * @returns {boolean} True if empty, false otherwise.
     */
    isEmpty() {
        return this.currentSize === 0;
    }

    /**
     * Returns the current number of elements.
     * @returns {number} The size of the queue.
     */
    getSize() {
        return this.currentSize;
    }
}
```

## 5. Summary

- **Stacks** can be effectively implemented using either arrays or linked lists. Arrays benefit from cache locality and lower memory overhead, while linked lists offer true dynamic sizing without resizing penalties.
- **Queues** should **never** be implemented using a naive array due to the **O(n)** cost of element shifting during dequeue operations. Efficient alternatives include **circular arrays** (for fixed capacity) and **linked lists** (for unbounded growth), both providing **O(1)** enqueue and dequeue performance.
- The implementation choice directly impacts the time complexity and memory characteristics of the data structure, and understanding these trade-offs is essential for designing high-performance software systems.