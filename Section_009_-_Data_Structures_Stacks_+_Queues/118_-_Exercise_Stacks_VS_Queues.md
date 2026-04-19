# Implementation Analysis: Stacks and Queues Using Arrays and Linked Lists

## 1. Introduction

Stacks and Queues are abstract data types (ADTs) that define a set of operations without specifying the underlying implementation. In practice, they can be constructed using two fundamental data structures: **Arrays** and **Linked Lists**. Each implementation choice presents distinct trade-offs in terms of time complexity, memory utilization, and operational efficiency. Understanding these trade-offs is essential for selecting the appropriate implementation for a given application.

This document examines the considerations for implementing Stacks and Queues using arrays versus linked lists, providing a comparative analysis and Java code examples.

## 2. Stack Implementation: Array vs Linked List

A Stack follows the **LIFO (Last-In-First-Out)** principle. Consider a browser history scenario where a user navigates through a sequence of web pages. The stack records the visited pages in the order of arrival, and the back button pops the most recent entry.

### 2.1 Array-Based Stack

**Advantages:**
- **Memory Locality**: Array elements are stored in contiguous memory locations, which improves cache performance and reduces access time.
- **Simplicity**: Straightforward implementation with minimal pointer overhead.
- **Fast Indexed Access**: Peek and push operations are O(1) without pointer chasing.

**Disadvantages:**
- **Fixed Capacity**: The stack size must be defined at creation, leading to potential overflow if the limit is exceeded, or wasted memory if the allocated space is underutilized.
- **Resizing Overhead**: Dynamic resizing (e.g., doubling array size) incurs an O(n) cost when triggered, though amortized cost remains O(1).

**Java Implementation (Array-Based Stack):**

```java
/**
 * Stack implementation using a dynamic array.
 * Provides amortized O(1) push and O(1) pop operations.
 */
public class ArrayStack {
    private int[] stackArray;
    private int top;
    private static final int DEFAULT_CAPACITY = 10;

    public ArrayStack() {
        stackArray = new int[DEFAULT_CAPACITY];
        top = -1;
    }

    public void push(int value) {
        if (top == stackArray.length - 1) {
            resize(stackArray.length * 2); // Double capacity
        }
        stackArray[++top] = value;
    }

    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stackArray[top--];
    }

    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stackArray[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    private void resize(int newCapacity) {
        int[] newArray = new int[newCapacity];
        System.arraycopy(stackArray, 0, newArray, 0, top + 1);
        stackArray = newArray;
    }
}
```

### 2.2 Linked List-Based Stack

**Advantages:**
- **Dynamic Size**: The stack can grow and shrink without predefined capacity, allocating memory exactly as needed.
- **No Overflow (Within Memory Limits)**: As long as heap memory is available, elements can be added.

**Disadvantages:**
- **Memory Overhead**: Each node requires additional memory for storing the reference (pointer) to the next node.
- **Pointer Chasing**: Traversal involves following references, which may lead to cache misses and slightly slower access compared to contiguous arrays.

**Java Implementation (Linked List-Based Stack):**

```java
/**
 * Stack implementation using a singly linked list.
 * Provides O(1) push and pop operations.
 */
public class LinkedListStack {
    private class Node {
        int data;
        Node next;
        Node(int data) { this.data = data; }
    }

    private Node top;
    private int size;

    public LinkedListStack() {
        top = null;
        size = 0;
    }

    public void push(int value) {
        Node newNode = new Node(value);
        newNode.next = top;
        top = newNode;
        size++;
    }

    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        int value = top.data;
        top = top.next;
        size--;
        return value;
    }

    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return top.data;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public int size() {
        return size;
    }
}
```

### 2.3 Comparative Summary for Stacks

| Criteria | Array-Based | Linked List-Based |
|----------|-------------|-------------------|
| Time Complexity (push/pop) | O(1) amortized | O(1) |
| Memory Usage | Contiguous, no pointer overhead | Extra memory per node for references |
| Dynamic Resizing | Required (costly occasionally) | Inherently dynamic |
| Cache Performance | Excellent | Moderate due to scattered nodes |
| Implementation Complexity | Simple | Simple |

For most stack applications where the maximum size is known or dynamic resizing is acceptable, the array-based implementation is efficient and cache-friendly. Linked list stacks are preferable when the stack size is highly unpredictable and memory fragmentation is a concern.

## 3. Queue Implementation: Array vs Linked List

A Queue follows the **FIFO (First-In-First-Out)** principle. Consider a waitlist application where users join a line and are served in order of arrival.

### 3.1 Array-Based Queue

**Problem with Naive Array Implementation:**
Using a simple array with a fixed front and rear leads to **O(n)** dequeue cost due to element shifting. When the front element is removed, all remaining elements must shift left to maintain contiguous storage.

**Solution: Circular Array (Ring Buffer):**
A circular array overcomes this inefficiency by allowing the front and rear pointers to wrap around the end of the array using modulo arithmetic. This provides O(1) enqueue and dequeue operations.

**Advantages of Circular Array:**
- O(1) enqueue and dequeue without shifting.
- Good cache locality.
- Fixed memory footprint.

**Disadvantages:**
- Fixed capacity; queue may become full.
- Slightly more complex pointer management.

**Java Implementation (Circular Array Queue):**

```java
/**
 * Queue implementation using a circular array.
 * Provides O(1) enqueue and dequeue operations.
 */
public class CircularArrayQueue {
    private int[] queueArray;
    private int front;
    private int rear;
    private int capacity;
    private int currentSize;

    public CircularArrayQueue(int capacity) {
        this.capacity = capacity;
        queueArray = new int[capacity];
        front = 0;
        rear = -1;
        currentSize = 0;
    }

    public void enqueue(int value) {
        if (currentSize == capacity) {
            throw new IllegalStateException("Queue is full");
        }
        rear = (rear + 1) % capacity;
        queueArray[rear] = value;
        currentSize++;
    }

    public int dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        int value = queueArray[front];
        front = (front + 1) % capacity;
        currentSize--;
        return value;
    }

    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        return queueArray[front];
    }

    public boolean isEmpty() {
        return currentSize == 0;
    }

    public int size() {
        return currentSize;
    }
}
```

### 3.2 Linked List-Based Queue

**Advantages:**
- **Dynamic Size**: No fixed capacity; queue can grow indefinitely (limited by heap memory).
- **O(1) Operations**: Enqueue (add to tail) and dequeue (remove from head) are constant time with appropriate tail pointer maintenance.

**Disadvantages:**
- **Memory Overhead**: Each node requires extra space for a reference.
- **Potential Cache Inefficiency**: Non-contiguous nodes may lead to more cache misses.

**Java Implementation (Linked List Queue):**

```java
/**
 * Queue implementation using a singly linked list with tail pointer.
 * Provides O(1) enqueue and dequeue operations.
 */
public class LinkedListQueue {
    private class Node {
        int data;
        Node next;
        Node(int data) { this.data = data; }
    }

    private Node front;
    private Node rear;
    private int size;

    public LinkedListQueue() {
        front = null;
        rear = null;
        size = 0;
    }

    public void enqueue(int value) {
        Node newNode = new Node(value);
        if (isEmpty()) {
            front = newNode;
            rear = newNode;
        } else {
            rear.next = newNode;
            rear = newNode;
        }
        size++;
    }

    public int dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        int value = front.data;
        front = front.next;
        if (front == null) {
            rear = null;
        }
        size--;
        return value;
    }

    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        return front.data;
    }

    public boolean isEmpty() {
        return front == null;
    }

    public int size() {
        return size;
    }
}
```

### 3.3 Comparative Summary for Queues

| Criteria | Circular Array | Linked List |
|----------|----------------|-------------|
| Time Complexity (enqueue/dequeue) | O(1) | O(1) |
| Space Efficiency | No overhead for pointers | Overhead per node |
| Capacity Limit | Fixed (unless resized) | Dynamic |
| Cache Performance | Good | Moderate |
| Implementation Complexity | Moderate (modulo arithmetic) | Simple with tail pointer |

For queues, **circular arrays** are often preferred in systems programming (e.g., device drivers, network buffers) due to their predictable memory usage and cache efficiency. **Linked lists** are advantageous in applications where the queue size is highly variable and unknown at compile time.

## 4. Selection Guidelines

The choice between array-based and linked list-based implementations depends on the specific requirements of the application:

- **Use Array-Based Implementation When:**
  - The maximum size is known in advance or can be bounded.
  - Cache performance and memory locality are critical.
  - Memory overhead for references is undesirable.

- **Use Linked List-Based Implementation When:**
  - The size of the data structure is unpredictable and may change dramatically.
  - Frequent resizing of an array would be costly.
  - Simplicity of dynamic growth outweighs cache considerations.

## 5. Conclusion

Both arrays and linked lists provide viable foundations for implementing Stacks and Queues. The array-based stack offers excellent cache performance and simplicity, while the linked list stack provides true dynamic sizing. For queues, the naive array approach is inefficient due to shifting; the circular array resolves this with O(1) operations, and the linked list offers a straightforward dynamic alternative. Understanding these implementation trade-offs enables informed decisions in software design and algorithm development.