# Binary Search Tree Implementation in JavaScript

## 1. Introduction

This document presents a detailed implementation of a Binary Search Tree (BST) in JavaScript, focusing on the fundamental `insert` and `lookup` operations. The `remove` operation, due to its increased complexity involving multiple cases and subtree restructuring, is intentionally deferred to a subsequent discussion.

Understanding the internal mechanics of a BST—how nodes are created, linked, and traversed—builds essential foundational knowledge for working with tree-based data structures. While production environments frequently utilize well-tested libraries for tree operations, the ability to implement core BST functionality demonstrates a thorough grasp of the underlying principles.

## 2. Node Structure

Each element within the BST is encapsulated as a `Node` object. A node stores its data payload and maintains two reference pointers: one to its left child and one to its right child.

```javascript
class Node {
    constructor(value) {
        // The data value stored in this node
        this.value = value;

        // Reference to the left child node (initialized to null)
        this.left = null;

        // Reference to the right child node (initialized to null)
        this.right = null;
    }
}
```

**Properties:**
| Property | Type | Description |
|----------|------|-------------|
| `value` | any | The data held by the node (commonly a number for comparison-based trees) |
| `left` | Node \| null | Reference to the left child node |
| `right` | Node \| null | Reference to the right child node |

## 3. Binary Search Tree Class Initialization

The `BinarySearchTree` class serves as the container for the tree structure. It maintains a reference to the `root` node, which serves as the entry point for all tree operations.

```javascript
class BinarySearchTree {
    constructor() {
        // The tree initially contains no nodes
        this.root = null;
    }

    // Insert and lookup methods will be defined here
}
```

## 4. Insert Operation

### 4.1 Algorithm Overview

The `insert` method adds a new node containing the specified value to the BST while preserving the binary search property:

- Left subtree values are strictly less than the parent node's value.
- Right subtree values are strictly greater than or equal to the parent node's value.

The algorithm traverses the tree starting from the root, comparing the new value with each visited node's value to determine the appropriate direction (left or right). Traversal continues until a `null` child reference is encountered, at which point the new node is attached.

### 4.2 Implementation

```javascript
insert(value) {
    // Step 1: Create a new node with the provided value
    const newNode = new Node(value);

    // Step 2: Handle the empty tree case
    if (this.root === null) {
        this.root = newNode;
        return this;
    }

    // Step 3: Traverse the tree to find insertion point
    let currentNode = this.root;

    while (true) {
        // Case A: Value is less than current node's value -> go left
        if (value < currentNode.value) {
            // If left child is absent, insert here
            if (currentNode.left === null) {
                currentNode.left = newNode;
                return this;    // Exit loop and method
            }
            // Otherwise, continue traversing left subtree
            currentNode = currentNode.left;
        }
        // Case B: Value is greater than or equal -> go right
        else {
            // If right child is absent, insert here
            if (currentNode.right === null) {
                currentNode.right = newNode;
                return this;    // Exit loop and method
            }
            // Otherwise, continue traversing right subtree
            currentNode = currentNode.right;
        }
    }
}
```

### 4.3 Explanation of Key Steps

1. **Node Instantiation:** A new `Node` object is created with the given `value`.

2. **Empty Tree Check:** If `this.root` is `null`, the tree is empty. The new node becomes the root, and the method returns.

3. **Traversal Loop:** A `while (true)` loop continues indefinitely until an insertion point is found and the method explicitly returns.

4. **Direction Decision:**
   - If `value < currentNode.value`, the algorithm moves to the left child.
   - Otherwise, it moves to the right child (values equal to or greater than the current node go right in this implementation).

5. **Insertion Condition:** When the intended child reference (`left` or `right`) is `null`, the new node is assigned to that reference, and the method returns.

6. **Continuation:** If the child reference is occupied, `currentNode` is updated to that child, and the loop repeats.

### 4.4 Handling Duplicate Values

The implementation above places values equal to the current node's value in the right subtree. Alternative policies include:

- Disallowing duplicates entirely and ignoring insertion attempts.
- Maintaining a `count` property within each node to track frequency.

The choice depends on application requirements.

## 5. Lookup Operation

### 5.1 Algorithm Overview

The `lookup` method searches for a node containing a specified value. It follows the same traversal logic as `insert`, comparing the target value with each visited node and moving left or right accordingly. If the value is found, the corresponding node is returned; otherwise, the method returns `null`.

### 5.2 Implementation

```javascript
lookup(value) {
    // Start traversal from the root
    let currentNode = this.root;

    // Continue while there are nodes to examine
    while (currentNode !== null) {
        // Value matches current node
        if (value === currentNode.value) {
            return currentNode;
        }
        // Value is smaller: go left
        else if (value < currentNode.value) {
            currentNode = currentNode.left;
        }
        // Value is larger: go right
        else {
            currentNode = currentNode.right;
        }
    }

    // Value not found in the tree
    return null;
}
```

### 5.3 Explanation

- The loop condition `currentNode !== null` ensures traversal continues only while there is a node to examine.
- At each step, the target `value` is compared with `currentNode.value`.
- Equality results in immediate return of the node.
- Inequality determines the direction of descent.
- If the loop exits without finding the value, `null` is returned.

## 6. Testing and Verification

### 6.1 Building a Sample Tree

The following sequence of insertions constructs a BST with the structure shown below:

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

**Expected Tree Structure (ASCII Representation):**
```
          9
        /   \
       4     20
      / \   /  \
     1   6 15   170
```

### 6.2 Traversal Helper for Verification

A recursive helper function converts the tree into a nested object suitable for JSON serialization, enabling visual inspection of the tree's structure in the console.

```javascript
/**
 * Recursively traverses the tree and returns an object representation.
 * @param {Node} node - The current node being visited.
 * @returns {Object|null} - Nested object representing the subtree.
 */
function traverse(node) {
    if (node === null) return null;
    return {
        value: node.value,
        left: traverse(node.left),
        right: traverse(node.right)
    };
}

// Usage for verification
console.log(JSON.stringify(traverse(bst.root), null, 2));
```

### 6.3 Expected JSON Output (Abbreviated)

```json
{
  "value": 9,
  "left": {
    "value": 4,
    "left": {
      "value": 1,
      "left": null,
      "right": null
    },
    "right": {
      "value": 6,
      "left": null,
      "right": null
    }
  },
  "right": {
    "value": 20,
    "left": {
      "value": 15,
      "left": null,
      "right": null
    },
    "right": {
      "value": 170,
      "left": null,
      "right": null
    }
  }
}
```

This output confirms that the tree has been constructed correctly according to BST rules.

## 7. Practical Considerations

### 7.1 Use of Libraries in Production

In real-world software development, developers rarely implement BSTs from scratch. Established libraries and built-in language features provide optimized, well-tested tree implementations. For example:

- **JavaScript:** Libraries such as `bintrees` offer Red-Black tree and Binomial Heap implementations.
- **Other Languages:** Standard libraries often include balanced tree structures (e.g., `std::map` in C++, `TreeMap` in Java).

Understanding the underlying mechanics, however, remains crucial for:

- Debugging unexpected behavior in tree-based structures.
- Making informed decisions about which data structure to employ.
- Successfully navigating technical interviews that assess fundamental knowledge.

### 7.2 Complexity and Cognitive Load

Implementing tree operations requires careful attention to pointer manipulation and traversal logic. Visualizing the tree structure—either on paper or using tools like VisualGo—can significantly aid comprehension. It is normal for the process to feel challenging initially; repeated practice builds familiarity.

## 8. Summary

- The `Node` class encapsulates a value and references to left and right children.
- The `BinarySearchTree` class maintains a `root` reference and provides `insert` and `lookup` methods.
- The `insert` method traverses the tree to find an appropriate `null` child position, attaching the new node there.
- The `lookup` method traverses similarly, returning the found node or `null`.
- A recursive traversal helper facilitates visual verification of the tree structure.
- The `remove` operation, involving more complex rebalancing logic, is deferred for separate study.

Mastery of these fundamental BST operations prepares the learner for advanced topics such as tree balancing algorithms and alternative tree structures.