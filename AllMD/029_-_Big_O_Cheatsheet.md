A solid grasp of algorithmic complexity is a fundamental requirement for technical interviews and writing efficient code. The following is a quick reference for the most common Big O complexities, data structure operations, and algorithms.

### Complexity Classes

| Notation | Name | Description |
| :--- | :--- | :--- |
| **O(1)** | Constant | Execution time is constant and does not change based on the input size. Common examples include accessing an array element by index, hash table lookups, and stack push/pop operations. |
| **O(log n)** | Logarithmic | Time increases very slowly, even for large inputs. This is typical of divide-and-conquer algorithms like **binary search**, where the dataset is cut in half with each step. |
| **O(n)** | Linear | Time increases linearly with the input size. This is seen in operations like traversing a list or performing a simple linear search. |
| **O(n log n)** | Linearithmic | This is the best possible time complexity for comparison-based sorting algorithms. **Merge sort** and **heap sort** are common examples. |
| **O(n²)** | Quadratic | Time increases quadratically with the input size. This is typical of algorithms with nested loops, such as the **bubble sort**, **insertion sort**, and **selection sort**. |
| **O(2ⁿ)** | Exponential | Time doubles with each new input element. This is typical of recursive algorithms that solve a problem of size `n` by recursively solving two smaller problems of size `n-1`, like the naive Fibonacci sequence. |
| **O(n!)** | Factorial | Execution time grows factorially, making it extremely inefficient. This is common in algorithms that generate all permutations of a dataset. |

---

### Data Structure Operations (Average Time)

| Data Structure | Access | Search | Insert | Delete |
| :--- | :--- | :--- | :--- | :--- |
| **Array** | O(1) | O(n) | O(n) | O(n) |
| **Stack / Queue** | O(n) | O(n) | O(1) | O(1) |
| **Linked List** | O(n) | O(n) | O(1) | O(1) |
| **Hash Table** | O(1) | O(1) | O(1) | O(1) |
| **Binary Search Tree (BST)** | O(log n) | O(log n) | O(log n) | O(log n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) |
| **Heap** | O(1) | O(n) | O(log n) | O(log n) |

Data in this table is sourced from a comprehensive online cheat sheet.

---

### Common Algorithm Complexities (Time)

| Algorithm | Best | Average | Worst | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n + k) |

Data in this table is sourced from a comprehensive online cheat sheet.

---

### Space Complexity

Space complexity measures the amount of memory an algorithm uses relative to the input size. A few common patterns to keep in mind:

*   **O(1)**: The algorithm uses a constant amount of memory. Sorting algorithms like bubble, insertion, and selection sort are in-place.
*   **O(n)**: The algorithm creates a new data structure proportional to the input size. **Merge sort** has an O(n) space complexity because it creates a new array for merging.
*   **O(log n)**: The algorithm uses memory proportional to the recursion depth. **Quick sort** has O(log n) space complexity due to the recursive call stack.

---

### Interview Tips & Rules of Thumb

*   **Always state the complexity**: When you present a solution in an interview, you should always state its time and space complexity.
*   **Consider trade-offs**: Sometimes using extra space (e.g., with a hash table) can significantly reduce time complexity. For example, an O(n) space solution can reduce an O(n²) time problem to O(n).
*   **Drop constants and non-dominants**: O(2n) simplifies to O(n). O(n² + n) simplifies to O(n²), as the `n` term is non-dominant.
*   **Worst-case is the standard**: Unless specified otherwise, you should assume that Big O notation refers to an algorithm's worst-case runtime. For example, while insertion sort is very fast on a small or nearly sorted dataset (O(n)), in the worst case it is still O(n²).
*   **Amortized analysis**: For some data structures, like dynamic arrays, the occasional resizing operation is expensive (O(n)), but it is rare enough that the average cost of an insertion over many operations is O(1).

---

### Additional Resources

*   **Interactive Website**: `Big-O-Buddy` is a comprehensive and interactive cheat sheet for understanding notation and algorithm complexity.
*   **GitHub Repository**: `ReaVNaiL/Big-O-Complexity-Cheat-Sheet` provides a concise summary of the key concepts.
*   **PDF Download**: A downloadable 1-page PDF cheat sheet covering the most important complexity classes is available from HappyCoders.

If you have questions about a specific concept or need further clarification on any of these topics, feel free to ask in our private Discord community's help channels.