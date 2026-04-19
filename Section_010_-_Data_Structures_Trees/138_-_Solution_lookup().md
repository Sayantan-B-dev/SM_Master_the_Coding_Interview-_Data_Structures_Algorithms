# Binary Search Tree Lookup Implementation

## 1. Introduction

The lookup operation is a fundamental component of a Binary Search Tree (BST). It enables efficient retrieval of a node containing a specified value by exploiting the ordered structure of the tree. Unlike linear search in arrays or linked lists, BST lookup achieves logarithmic time complexity under balanced conditions by systematically eliminating half of the remaining search space at each step.

This document details the implementation of the `lookup` method within the `BinarySearchTree` class introduced previously. The method returns the node if found; otherwise, it returns `false` or `null`.

## 2. Algorithm Overview

The lookup algorithm traverses the tree from the root downward, guided by the binary search property:

- All values in the left subtree are strictly less than the current node's value.
- All values in the right subtree are strictly greater than or equal to the current node's value.

At each node visited, the target value is compared with the node's value:

| Comparison Result | Action |
|-------------------|--------|
| `target < current.value` | Move to the left child. |
| `target > current.value` | Move to the right child. |
| `target === current.value` | Node found; return the current node. |

If traversal reaches a `null` reference (i.e., a non-existent child), the target value does not exist in the tree, and the search terminates unsuccessfully.

## 3. Implementation in JavaScript

### 3.1 Code Listing

The following implementation of the `lookup` method resides within the `BinarySearchTree` class.

```javascript
/**
 * Searches for a node with the specified value in the BST.
 * @param {number} value - The value to locate.
 * @returns {Node|boolean} - The node if found; otherwise false.
 */
lookup(value) {
    // Case 1: Tree is empty - value cannot exist
    if (!this.root) {
        return false;
    }

    // Begin traversal at the root node
    let currentNode = this.root;

    // Continue traversing while a node exists to examine
    while (currentNode !== null) {
        // Value is smaller than current node's value: go left
        if (value < currentNode.value) {
            currentNode = currentNode.left;
        }
        // Value is larger than current node's value: go right
        else if (value > currentNode.value) {
            currentNode = currentNode.right;
        }
        // Value matches current node's value: node found
        else if (value === currentNode.value) {
            return currentNode;
        }
    }

    // Traversal ended without finding the value
    return false;
}
```

### 3.2 Explanation of Key Components

#### 3.2.1 Empty Tree Check

```javascript
if (!this.root) {
    return false;
}
```

If the `root` property of the tree is `null`, the BST contains no nodes. The method immediately returns `false` because the sought value cannot be present.

#### 3.2.2 Traversal Initialization

```javascript
let currentNode = this.root;
```

A reference variable `currentNode` is initialized to the root node. This variable will be updated as the algorithm descends through the tree.

#### 3.2.3 Traversal Loop

```javascript
while (currentNode !== null) {
    // ...
}
```

The loop continues as long as `currentNode` references a valid node. If traversal reaches a `null` child (i.e., a missing left or right reference), the loop exits, and the method returns `false`.

#### 3.2.4 Directional Decision Making

```javascript
if (value < currentNode.value) {
    currentNode = currentNode.left;
}
else if (value > currentNode.value) {
    currentNode = currentNode.right;
}
```

- **Less than:** The algorithm updates `currentNode` to the left child, effectively discarding the right subtree and all values greater than the current node.
- **Greater than:** The algorithm updates `currentNode` to the right child, discarding the left subtree.

#### 3.2.5 Match Detection

```javascript
else if (value === currentNode.value) {
    return currentNode;
}
```

When the target value equals the current node's value, the desired node has been located. The method immediately returns the node object.

### 3.3 Return Value Semantics

The method returns:
- A `Node` object when the value is found.
- The boolean value `false` when the value is absent (or `null` depending on implementation preference).

## 4. Testing and Verification

### 4.1 Sample Tree Construction

The following sequence of insertions constructs a BST with a known structure for testing the `lookup` method.

```javascript
const bst = new BinarySearchTree();
bst.insert(9);
bst.insert(4);
bst.insert(6);
bst.insert(20);
bst.insert(170);
bst.insert(15);
bst.insert(1);
```

**Resulting Tree Structure (ASCII):**
```
          9
        /   \
       4     20
      / \   /  \
     1   6 15   170
```

### 4.2 Lookup Test Cases

| Lookup Value | Expected Result | Reason |
|--------------|-----------------|--------|
| `9` | Node with value 9 | Root node exists |
| `4` | Node with value 4 | Left child of root exists |
| `20` | Node with value 20 | Right child of root exists |
| `170` | Node with value 170 | Leaf node in right subtree exists |
| `90` | `false` | Value not present in tree |
| `171` | `false` | Value not present |

### 4.3 Verification Code

```javascript
console.log(bst.lookup(9));    // Node { value: 9, left: Node, right: Node }
console.log(bst.lookup(90));   // false
console.log(bst.lookup(20));   // Node { value: 20, left: Node, right: Node }
console.log(bst.lookup(170));  // Node { value: 170, left: null, right: null }
console.log(bst.lookup(171));  // false
```

## 5. Complexity Analysis

### 5.1 Time Complexity

The `lookup` operation exhibits the following time complexities:

| Case | Complexity | Description |
|------|------------|-------------|
| **Average (Balanced Tree)** | O(log n) | Each comparison eliminates approximately half of the remaining nodes. |
| **Worst (Unbalanced Tree)** | O(n) | In a completely skewed tree, traversal degenerates to linear search. |

The logarithmic behavior in balanced trees arises from the **divide and conquer** strategy: at each step, the algorithm chooses one of two directions, thereby halving the search space.

### 5.2 Space Complexity

The iterative implementation presented above uses **O(1)** auxiliary space, as it maintains only a single `currentNode` reference variable. A recursive implementation would consume O(h) space on the call stack, where `h` is the height of the tree.

## 6. Divide and Conquer Paradigm

The lookup algorithm exemplifies the **divide and conquer** approach:

1. **Divide:** The search space (the set of possible node locations) is split into two disjoint subsets—the left subtree and the right subtree—based on comparison with the current node.
2. **Conquer:** The algorithm recursively (or iteratively) solves the subproblem in the chosen subtree.
3. **Combine:** No combination step is required; the result from the subproblem is directly returned.

This paradigm is responsible for the efficiency gains observed in BST operations compared to linear data structures.

## 7. Comparison with Insert Method

The `lookup` and `insert` methods share a nearly identical traversal logic:

| Aspect | Insert | Lookup |
|--------|--------|--------|
| Traversal Condition | Continue until `null` child is found for insertion | Continue until value matches or `null` is reached |
| Direction Decision | Compare new value with current node's value | Compare target value with current node's value |
| Termination | Insert new node at `null` child and return | Return node or `false` |

The primary distinction lies in the action taken upon reaching the target location: `insert` creates a new node, whereas `lookup` either returns an existing node or indicates absence.

## 8. Summary

- The `lookup` method traverses a BST by comparing the target value with each visited node's value.
- Traversal proceeds left for smaller values and right for larger values.
- A match results in immediate return of the node; reaching `null` indicates the value is absent.
- The iterative implementation uses a `while` loop and constant extra space.
- Balanced BSTs achieve O(log n) lookup time through divide-and-conquer reduction of the search space.
- The method complements the `insert` operation, forming the core retrieval mechanism of the Binary Search Tree.