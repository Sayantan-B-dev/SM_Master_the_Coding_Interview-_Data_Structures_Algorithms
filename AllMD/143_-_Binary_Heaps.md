# Binary Heaps

## 1. Introduction

A heap is a specialized tree-based data structure that satisfies the **heap property**. Heaps are commonly implemented as binary heaps, which are complete binary trees with ordering constraints. Unlike binary search trees, which enforce a strict left-right ordering, heaps prioritize the relationship between a parent and its children based solely on a comparative criterion.

Binary heaps find extensive application in algorithms requiring efficient access to the minimum or maximum element, such as priority queues, sorting algorithms (heapsort), and graph algorithms (Dijkstra's shortest path, Prim's minimum spanning tree).

## 2. Definition and Core Properties

### 2.1 Structural Property: Complete Binary Tree

A binary heap is a **complete binary tree**. This means:

- All levels of the tree are completely filled except possibly the last level.
- The last level is filled from left to right without gaps.

This structural constraint enables efficient array-based representation, where parent-child relationships are computed using index arithmetic rather than explicit pointers.

### 2.2 Heap Order Property

The heap order property governs the relationship between a node and its parent. Two variants exist:

| Heap Type | Order Property | Description |
|-----------|----------------|-------------|
| **Max Heap** | Parent ≥ Children | The value of each parent node is greater than or equal to the values of its children. The maximum element resides at the root. |
| **Min Heap** | Parent ≤ Children | The value of each parent node is less than or equal to the values of its children. The minimum element resides at the root. |

**Max Heap Example (ASCII Representation):**
```
        101
       /   \
     72     33
    /  \   /  \
   2   45 5    1
```
- 101 ≥ 72 and 33
- 72 ≥ 2 and 45
- 33 ≥ 5 and 1

**Min Heap Example:**
```
         1
       /   \
      5     2
     / \   / \
    8  10 6   3
```
- 1 ≤ 5 and 2
- 5 ≤ 8 and 10
- 2 ≤ 6 and 3

### 2.3 Absence of Left-Right Ordering

A critical distinction from binary search trees is that **no ordering exists between sibling nodes**. In a max heap, for example, it is permissible for the left child to be either smaller or larger than the right child. The only constraint is that both are less than or equal to the parent.

This relaxed ordering makes heaps unsuitable for efficient general-purpose searching (lookup is O(n)), but highly efficient for operations that involve only the extremum (root) element.

## 3. Array Representation of Binary Heaps

Because a binary heap is a complete binary tree, it can be compactly stored in an array without explicit `left` and `right` pointers.

**Index Mapping Rules (0-based indexing):**
- Root element: `index 0`
- For an element at index `i`:
  - Left child index: `2i + 1`
  - Right child index: `2i + 2`
  - Parent index: `Math.floor((i - 1) / 2)`

**Example: Max Heap Array Representation**

```
Tree:           101
               /   \
             72     33
            /  \   /  \
           2   45 5    1

Array: [101, 72, 33, 2, 45, 5, 1]
Indices: 0    1   2  3   4  5  6
```

**Relationships:**
- Node 72 (index 1): left child is at 2*1+1 = 3 (value 2), right child at 4 (value 45).
- Node 33 (index 2): left child at 5 (value 5), right child at 6 (value 1).
- Node 2 (index 3): parent is at floor((3-1)/2) = 1 (value 72).

## 4. Core Operations and Time Complexity

### 4.1 Peek (Find Maximum/Minimum)

Retrieving the extremum element (max in a max heap, min in a min heap) is a constant-time operation. The value is stored at the root (index 0).

**Time Complexity:** O(1)

### 4.2 Insertion

Inserting a new element into a binary heap involves two steps:

1. **Append:** Place the new element at the next available position in the array (maintaining the complete tree property).
2. **Bubble Up (Heapify Up):** Compare the newly inserted element with its parent. If the heap order property is violated, swap the element with its parent. Repeat this process up the tree until the property is restored.

**Time Complexity:** O(log n) — in the worst case, the element may need to bubble up from a leaf to the root.

**Insertion Visualization (Max Heap):**
```
Insert 100 into [101, 72, 33, 2, 45, 5, 1]

Step 1: Append at end → [101, 72, 33, 2, 45, 5, 1, 100]
Step 2: Compare 100 (index 7) with parent (index 3, value 2) → swap → [101, 72, 33, 100, 45, 5, 1, 2]
Step 3: Compare 100 (index 3) with parent (index 1, value 72) → swap → [101, 100, 33, 72, 45, 5, 1, 2]
Step 4: Compare 100 (index 1) with parent (index 0, value 101) → property satisfied; stop.
```

### 4.3 Extract Max / Extract Min

Removing the root element (the extremum) involves:

1. **Replace Root:** Replace the root element with the last element in the array (the rightmost leaf).
2. **Remove Last:** Remove the last element (now duplicate) from the array.
3. **Bubble Down (Heapify Down):** Compare the new root with its children. If the heap order property is violated, swap the root with the larger child (in a max heap) or the smaller child (in a min heap). Continue this process down the tree until the property is restored.

**Time Complexity:** O(log n) — the element may need to sink from root to leaf.

### 4.4 Lookup (Search)

Searching for an arbitrary value in a binary heap requires examining nodes without the benefit of directional guidance (unlike BST). In the worst case, all nodes must be visited.

**Time Complexity:** O(n)

## 5. Comparison with Binary Search Tree

| Aspect | Binary Heap | Binary Search Tree (BST) |
|--------|-------------|--------------------------|
| **Ordering** | Parent ≥ Children (max) or ≤ (min). No sibling order. | Left < Parent < Right (strict). |
| **Lookup** | O(n) — requires potentially scanning all nodes. | O(log n) average; O(n) worst. |
| **Insertion** | O(log n) — bubble up. | O(log n) average; O(n) worst. |
| **Deletion** | O(log n) — bubble down (only root removal is efficient). | O(log n) average; O(n) worst. |
| **Find Min/Max** | O(1) — root element. | O(log n) (follow left/right to leaf). |
| **Memory Representation** | Compact array; no pointers. | Node objects with left/right references. |
| **Primary Use** | Priority queues, heap sort, graph algorithms. | Dynamic sorted data, range queries. |

## 6. JavaScript Implementation: Max Heap

The following example demonstrates a Max Heap implementation using an array.

```javascript
class MaxHeap {
    constructor() {
        this.heap = [];  // Array to store heap elements
    }

    // Helper: Get parent index
    _parentIndex(index) {
        return Math.floor((index - 1) / 2);
    }

    // Helper: Get left child index
    _leftChildIndex(index) {
        return 2 * index + 1;
    }

    // Helper: Get right child index
    _rightChildIndex(index) {
        return 2 * index + 2;
    }

    // Swap two elements in the heap array
    _swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    // Insert a value into the heap
    insert(value) {
        // Step 1: Append to end
        this.heap.push(value);
        let currentIndex = this.heap.length - 1;

        // Step 2: Bubble up
        while (currentIndex > 0) {
            const parentIdx = this._parentIndex(currentIndex);
            if (this.heap[currentIndex] <= this.heap[parentIdx]) {
                break;  // Heap property satisfied
            }
            this._swap(currentIndex, parentIdx);
            currentIndex = parentIdx;
        }
    }

    // Remove and return the maximum element (root)
    extractMax() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const max = this.heap[0];
        // Move last element to root
        this.heap[0] = this.heap.pop();
        this._heapifyDown(0);
        return max;
    }

    // Restore heap property from given index downward
    _heapifyDown(index) {
        const length = this.heap.length;
        while (true) {
            let largest = index;
            const left = this._leftChildIndex(index);
            const right = this._rightChildIndex(index);

            if (left < length && this.heap[left] > this.heap[largest]) {
                largest = left;
            }
            if (right < length && this.heap[right] > this.heap[largest]) {
                largest = right;
            }
            if (largest === index) break;  // Heap property satisfied

            this._swap(index, largest);
            index = largest;
        }
    }

    // Return the maximum element without removing it
    peek() {
        return this.heap.length > 0 ? this.heap[0] : null;
    }
}

// Example usage
const maxHeap = new MaxHeap();
maxHeap.insert(101);
maxHeap.insert(72);
maxHeap.insert(33);
maxHeap.insert(2);
maxHeap.insert(45);
maxHeap.insert(5);
maxHeap.insert(1);

console.log(maxHeap.peek());       // 101
console.log(maxHeap.extractMax()); // 101
console.log(maxHeap.extractMax()); // 72
```

## 7. Priority Queues and Applications

### 7.1 Relationship to Heaps

A **priority queue** is an abstract data type that supports insertion of elements with associated priorities and retrieval of the element with the highest (or lowest) priority. Binary heaps provide an efficient concrete implementation for priority queues because:

- The element with highest priority is always at the root (O(1) access).
- Insertions and extractions preserve the heap order in O(log n) time.

### 7.2 Common Use Cases

| Application | Description |
|-------------|-------------|
| **Task Scheduling** | Operating system schedulers use priority queues to determine which process runs next based on priority. |
| **Dijkstra's Algorithm** | Finds shortest paths in graphs; uses a min-heap priority queue to repeatedly extract the node with the smallest tentative distance. |
| **Huffman Coding** | Data compression algorithm that builds a Huffman tree using a min-heap to repeatedly extract two smallest frequency nodes. |
| **Heapsort** | Comparison-based sorting algorithm that builds a heap and repeatedly extracts the maximum/minimum element. O(n log n) time complexity. |
| **Event Simulation** | Discrete event simulation systems use priority queues to process events in chronological order. |

## 8. Summary

- A **binary heap** is a complete binary tree that satisfies the heap order property (max-heap or min-heap).
- Heaps are efficiently implemented using arrays, with index arithmetic replacing explicit pointers.
- Core operations: **peek** (O(1)), **insert** (O(log n)), **extract-max/min** (O(log n)).
- **Lookup** of arbitrary elements is O(n) because no left-right ordering exists.
- Heaps differ from binary search trees in their relaxed ordering; they prioritize parent-child relationships over sibling order.
- Binary heaps are the standard implementation for **priority queues** and are fundamental to many graph and sorting algorithms.
- Understanding heap operations and complexities is essential for algorithm design and technical interviews.