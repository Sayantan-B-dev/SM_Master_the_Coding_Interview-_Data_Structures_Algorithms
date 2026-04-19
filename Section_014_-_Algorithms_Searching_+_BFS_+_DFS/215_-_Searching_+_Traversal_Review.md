# Section Summary: Searching and Traversal Algorithms

## 1. Introduction

This document provides a comprehensive summary of the core concepts and algorithms covered in the "Searching and Traversal" section of the curriculum. The topics addressed include fundamental search algorithms on linear and sorted data structures, systematic traversal techniques for trees and graphs, comparative analysis of Breadth-First Search (BFS) and Depth-First Search (DFS), and an introduction to shortest path algorithms for weighted graphs.

The material presented herein serves as a consolidated reference suitable for examination preparation, long-term retention, and rapid conceptual review.

---

## 2. Linear Search

### 2.1 Definition and Operation

Linear search, also termed sequential search, is the simplest searching algorithm. It iterates through each element of a collection sequentially until the target value is located or the end of the collection is reached.

### 2.2 Characteristics

| Property | Value |
|----------|-------|
| **Data Requirement** | Works on both sorted and unsorted data |
| **Time Complexity (Worst/Average)** | O(n) |
| **Time Complexity (Best)** | O(1) |
| **Space Complexity** | O(1) |
| **Primary Advantage** | Simplicity; no preprocessing required |

### 2.3 JavaScript Implementation

```javascript
/**
 * Performs linear search on an array.
 * @param {Array} array - The array to search within.
 * @param {*} target - The value to locate.
 * @returns {number} - Index of target if found; otherwise -1.
 */
function linearSearch(array, target) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === target) {
            return i;  // Target found at index i
        }
    }
    return -1;  // Target not present
}
```

### 2.4 Use Cases and Limitations

Linear search is appropriate for small datasets or when data is inherently unsorted and only a single search operation is anticipated. For larger datasets or repeated searches, sorting followed by binary search offers superior performance despite the initial sorting overhead.

---

## 3. Binary Search

### 3.1 Definition and Prerequisite

Binary search is an efficient algorithm for locating a target value within a **sorted** collection. It operates by repeatedly dividing the search interval in half, discarding the portion that cannot contain the target based on comparison with the middle element.

### 3.2 Algorithmic Principle

1. Determine the middle index of the current search interval.
2. Compare the middle element with the target.
3. If equal, the search concludes.
4. If the target is smaller, restrict search to the left half.
5. If the target is larger, restrict search to the right half.
6. Repeat until the target is found or the interval becomes empty.

### 3.3 Characteristics

| Property | Value |
|----------|-------|
| **Data Requirement** | Must be sorted in ascending (or descending) order |
| **Time Complexity** | O(log n) |
| **Space Complexity (Iterative)** | O(1) |
| **Space Complexity (Recursive)** | O(log n) due to call stack |

### 3.4 JavaScript Implementation (Iterative)

```javascript
/**
 * Performs binary search on a sorted array.
 * @param {Array<number>} sortedArray - Sorted array of numbers.
 * @param {number} target - Value to find.
 * @returns {number} - Index of target, or -1 if not found.
 */
function binarySearch(sortedArray, target) {
    let left = 0;
    let right = sortedArray.length - 1;

    while (left <= right) {
        // Compute middle index, avoiding overflow for large arrays
        const mid = Math.floor((left + right) / 2);
        const midValue = sortedArray[mid];

        if (midValue === target) {
            return mid;  // Target found
        } else if (midValue < target) {
            left = mid + 1;  // Discard left half
        } else {
            right = mid - 1; // Discard right half
        }
    }
    return -1;  // Target not found
}
```

### 3.5 Efficiency Considerations

Binary search achieves logarithmic time complexity by eliminating half of the remaining elements at each step. For a collection of size `n = 1,000,000`, at most 20 comparisons are required. Sorting an initially unsorted collection costs O(n log n), which is amortized over multiple search operations.

---

## 4. Tree and Graph Traversal

### 4.1 Overview

Traversal refers to the systematic visitation of every node in a tree or graph exactly once. Since trees are a specialized form of graph (acyclic, connected), the same fundamental algorithms—Breadth-First Search (BFS) and Depth-First Search (DFS)—apply to both structures with minor adaptations for cycles in graphs.

### 4.2 Breadth-First Search (BFS)

#### 4.2.1 Definition

BFS explores vertices in order of increasing distance from a source. It processes all vertices at depth `d` before any vertex at depth `d+1`.

#### 4.2.2 Algorithm

- **Data Structure:** Queue (FIFO)
- **Procedure:**
  1. Enqueue source vertex and mark visited.
  2. While queue is not empty:
     - Dequeue vertex `v`.
     - Process `v`.
     - Enqueue all unvisited adjacent vertices and mark visited.

#### 4.2.3 JavaScript Implementation for Trees

```javascript
/**
 * BFS traversal of a binary tree.
 * @param {Node} root - Root node of the tree.
 * @returns {Array} - Node values in BFS order.
 */
function bfsTree(root) {
    if (!root) return [];
    const result = [];
    const queue = [root];
    
    while (queue.length) {
        const current = queue.shift();
        result.push(current.value);
        if (current.left) queue.push(current.left);
        if (current.right) queue.push(current.right);
    }
    return result;
}
```

#### 4.2.4 Key Properties

- **Shortest Path:** Guarantees shortest path (in edges) for unweighted graphs.
- **Memory Usage:** O(w), where w is the maximum width of the tree/graph.
- **Applications:** Proximity-based searches, social network friend suggestions, web crawling.

### 4.3 Depth-First Search (DFS)

#### 4.3.1 Definition

DFS explores as deeply as possible along a branch before backtracking to examine alternative paths.

#### 4.3.2 Algorithm

- **Data Structure:** Stack (explicitly or via recursion)
- **Procedure (Recursive):**
  1. Mark current vertex visited and process it.
  2. For each unvisited neighbor, recursively apply DFS.
  3. Backtrack when no unvisited neighbors remain.

#### 4.3.3 Traversal Orders for Binary Trees

| Order | Visit Sequence | Use Case |
|-------|----------------|----------|
| **Pre-order** | Root → Left → Right | Tree serialization / copy creation |
| **In-order** | Left → Root → Right | Retrieve sorted data from BST |
| **Post-order** | Left → Right → Root | Safe tree deletion |

#### 4.3.4 JavaScript Implementation (In-order)

```javascript
/**
 * In-order DFS traversal of a binary tree.
 * @param {Node} node - Current node.
 * @param {Array} result - Accumulator for values.
 */
function inOrderDFS(node, result = []) {
    if (node) {
        inOrderDFS(node.left, result);
        result.push(node.value);
        inOrderDFS(node.right, result);
    }
    return result;
}
```

#### 4.3.5 Key Properties

- **Path Existence:** Efficient for determining if a path exists between two vertices.
- **Memory Usage:** O(h), where h is the height of the tree/graph (depth of recursion).
- **Applications:** Maze solving, cycle detection, topological sorting.

### 4.4 BFS vs. DFS Comparison

| Criterion | BFS | DFS |
|-----------|-----|-----|
| **Traversal Pattern** | Level by level (horizontal) | Branch by branch (vertical) |
| **Data Structure** | Queue | Stack (or recursion) |
| **Shortest Path** | Yes (unweighted) | Not guaranteed |
| **Space Complexity** | O(width) | O(height) |
| **When to Use** | Target likely near source; need shortest path | Memory constrained; deep target; path existence |

---

## 5. Weighted Graphs and Shortest Path Algorithms

### 5.1 Limitations of BFS and DFS

BFS and DFS treat all edges as having equal weight. In real-world scenarios (e.g., road networks with varying travel times, network routing with latency), edges possess numeric weights. For such **weighted graphs**, specialized algorithms are required.

### 5.2 Bellman-Ford Algorithm

- **Capability:** Handles graphs with **negative edge weights** and detects negative cycles.
- **Approach:** Relaxes all edges |V| - 1 times.
- **Time Complexity:** O(V · E)
- **Drawback:** Slower than Dijkstra for non-negative weights.

### 5.3 Dijkstra's Algorithm

- **Capability:** Finds shortest paths in graphs with **non-negative edge weights**.
- **Approach:** Greedy selection of the vertex with minimum tentative distance.
- **Time Complexity:** O((V + E) log V) with a priority queue.
- **Advantage:** More efficient than Bellman-Ford for graphs without negative weights.

### 5.4 Algorithm Selection Heuristic

| Graph Characteristic | Recommended Algorithm |
|----------------------|-----------------------|
| Contains negative edge weights | Bellman-Ford |
| All edge weights non-negative | Dijkstra |
| Need to detect negative cycles | Bellman-Ford |

**Interview Note:** Implementation of these algorithms is rarely expected in full due to time constraints; however, candidates should recognize the problem type and articulate the appropriate algorithm with its trade-offs.

---

## 6. Integration with Broader Algorithmic Knowledge

The concepts learned in this section complete a significant portion of the foundational algorithms mind map. Key insights include:

- **Sorted vs. Unsorted Data:** Sorting (O(n log n)) enables binary search (O(log n)), which outperforms linear search (O(n)) for multiple queries.
- **Traversal Efficiency:** Both BFS and DFS visit every node exactly once (O(n) time), but their memory profiles and visitation orders suit different problems.
- **Graph Modeling:** Real-world systems (social networks, maps, recommendation engines) are modeled as graphs, and traversal algorithms power core functionalities.

---

## 7. Visual Summary (Mermaid Diagram)

```mermaid
graph TD
    A[Data Structure] --> B{Is it sorted?}
    B -->|No| C[Linear Search O(n)]
    B -->|Yes| D[Binary Search O(log n)]
    A --> E[Tree / Graph]
    E --> F[Traversal O(n)]
    F --> G[BFS - Shortest Path]
    F --> H[DFS - Path Existence]
    E --> I[Weighted Graph]
    I --> J[Bellman-Ford<br>O(VE)]
    I --> K[Dijkstra<br>O((V+E) log V)]
```

---

## 8. Conclusion

This section has equipped learners with a thorough understanding of searching and traversal algorithms, ranging from elementary linear search to sophisticated graph traversal techniques. The material bridges the gap between theoretical complexity analysis and practical implementation, preparing students for both technical interviews and real-world software development challenges. The remaining area of the algorithmic mind map—dynamic programming—awaits exploration in the subsequent section.