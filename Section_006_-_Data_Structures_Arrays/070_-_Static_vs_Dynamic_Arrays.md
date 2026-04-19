# Static Arrays and Dynamic Arrays

## 1. Introduction

Arrays are categorised into two fundamental types based on their memory allocation strategy: **static arrays** and **dynamic arrays**. The distinction lies in how memory is reserved and managed for the array elements. Understanding this difference is essential for writing efficient code and appreciating the internal workings of high-level programming languages.

---

## 2. Static Arrays

### 2.1 Definition and Characteristics

A static array has a **fixed size** that must be specified at the time of creation. Once allocated, the array cannot grow or shrink in its original memory location. The number of elements it can hold is determined in advance and remains constant throughout its lifetime.

Key features of static arrays:

- Size is immutable after declaration.
- Memory is allocated as a single contiguous block.
- Attempting to add elements beyond the declared capacity is not permitted without creating a new, larger array.

### 2.2 Memory Allocation

Static arrays are allocated in adjacent blocks of memory when they are created. For example, if an array of seven elements is declared, the computer reserves exactly seven contiguous memory slots. There is no guarantee that additional contiguous memory is available immediately after the allocated block, which prevents in-place expansion.

```
Memory allocation for static array of size 7:

[Slot 0][Slot 1][Slot 2][Slot 3][Slot 4][Slot 5][Slot 6]
```

### 2.3 Example in C++

C++ provides static arrays where the size must be known at compile time.

```cpp
// Declaration of a static array with capacity for 20 integers
int a[20];

// Declaration and initialisation of a static array with 5 elements
int b[5] = {1, 2, 3, 4, 5};
```

In the above example, the array `b` has a fixed capacity of five integers. Adding a sixth element would require allocating a new array of larger size and copying all existing elements to the new memory location.

### 2.4 Expanding a Static Array

If additional space is required after a static array is filled, the following steps must be performed manually:

1. Allocate a new, larger block of memory (e.g., twice the original size).
2. Copy all elements from the original array to the new array.
3. Insert the new element at the end.
4. Release the original memory block (if dynamically allocated).

This process is computationally expensive, with a time complexity of **O(n)** due to the copying step.

```
Original array (size 7):
[A][B][C][D][E][F][G]

After expansion to size 14:
[A][B][C][D][E][F][G][H][ ][ ][ ][ ][ ][ ]
                         ↑
                    New element added
```

---

## 3. Dynamic Arrays

### 3.1 Definition and Characteristics

A dynamic array **automatically resizes** itself when its capacity is exceeded. The programmer is not required to specify a maximum size ahead of time, nor is manual memory management necessary in most high-level languages. The underlying implementation handles allocation and copying transparently.

Key features of dynamic arrays:

- Capacity grows automatically as elements are appended.
- Memory management is abstracted away from the developer.
- Resizing involves copying elements to a new, larger memory block, which incurs an occasional performance cost.

### 3.2 Languages with Built-in Dynamic Arrays

Many modern programming languages provide dynamic array implementations as standard:

| Language   | Dynamic Array Type          |
|------------|-----------------------------|
| JavaScript | `Array`                     |
| Python     | `list`                      |
| Java       | `ArrayList`                 |
| C#         | `List<T>`                   |

In these languages, arrays behave as dynamic by default, freeing the developer from manual memory allocation concerns.

### 3.3 Append Operation and Time Complexity

The **push** operation (or equivalent `append` method) adds an element to the end of a dynamic array. Its time complexity is:

- **Amortised O(1):** Most appends occur in constant time.
- **Occasional O(n):** When the array reaches its current capacity, the underlying implementation:
  1. Allocates a new memory block (typically double the current size).
  2. Copies all existing elements to the new block.
  3. Adds the new element.

This occasional linear-time resizing makes the append operation **amortised constant time** over a sequence of pushes. The average cost per operation remains O(1).

### 3.4 Example in JavaScript

JavaScript arrays are dynamic. The `push()` method illustrates automatic resizing.

```javascript
// Creating a dynamic array with four elements
const letters = ['A', 'B', 'C', 'D'];

// Appending a fifth element
letters.push('E'); // Usually O(1)
console.log(letters); // Output: ['A', 'B', 'C', 'D', 'E']
```

Internally, if the initial memory allocation was exactly four slots, pushing the fifth element would trigger a resize operation:

1. A new memory block (e.g., eight slots) is allocated.
2. The elements 'A', 'B', 'C', 'D' are copied to the new location.
3. 'E' is placed in the fifth slot.

This copying step causes that specific `push` call to be **O(n)**, where *n* is the number of elements before resizing.

---

## 4. Comparison: Static Arrays vs Dynamic Arrays

| Aspect                  | Static Array                                      | Dynamic Array                                         |
|-------------------------|---------------------------------------------------|-------------------------------------------------------|
| **Size Declaration**    | Fixed size specified at creation                  | Size not required; grows automatically                |
| **Memory Management**   | Manual or compile-time allocation                 | Automatic resizing handled by language runtime        |
| **Append Complexity**   | Not allowed directly; requires manual expansion O(n) | Amortised O(1), occasional O(n) during resize         |
| **Memory Flexibility**  | Inflexible; cannot grow in place                  | Flexible; adapts to data volume                       |
| **Language Examples**   | C++ (static arrays), C (fixed-size arrays)        | JavaScript `Array`, Python `list`, Java `ArrayList`   |
| **Control Over Memory** | High; programmer manages allocation and copying   | Low; abstracted for ease of use                       |

---

## 5. Practical Considerations

### 5.1 Performance Implications

While dynamic arrays are convenient, the occasional O(n) resizing cost should be acknowledged in performance-critical applications. In most scenarios, the amortised constant time is acceptable, and the overhead is negligible.

### 5.2 Low-Level vs High-Level Languages

- **Low-level languages (e.g., C, C++):** Offer static arrays and manual memory control, enabling fine-tuned optimisation at the cost of increased complexity.
- **High-level languages (e.g., JavaScript, Python):** Provide dynamic arrays with automatic memory management, prioritising developer productivity and safety.

### 5.3 Interview Context

During technical interviews, discussions about arrays typically assume **dynamic array** behaviour. Candidates may be expected to explain the amortised O(1) complexity of the `push` operation and the underlying resizing mechanism.

---

## 6. Summary

- **Static arrays** have a fixed size defined at creation and cannot expand without copying to a new memory location. They are common in low-level languages and offer precise memory control.
- **Dynamic arrays** automatically resize when capacity is exceeded, abstracting memory management from the programmer. Appending elements is amortised O(1) due to occasional O(n) resizing steps.
- Understanding both types provides insight into array performance characteristics and the trade-offs between control and convenience in different programming environments.