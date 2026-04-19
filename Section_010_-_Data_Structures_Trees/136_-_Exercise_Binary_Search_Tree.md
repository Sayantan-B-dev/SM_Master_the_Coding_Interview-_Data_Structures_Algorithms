# Binary Search Tree Implementation: Insert and Lookup

## 1. Exercise Overview

This document outlines an implementation exercise for constructing a Binary Search Tree (BST) in JavaScript. The objective is to implement two core methods—`insert` and `lookup`—that enable the creation and querying of a BST with the structure illustrated below.

The exercise provides a foundational understanding of how nodes are organized and traversed within a BST. Implementation of the `remove` method is intentionally deferred due to its increased complexity.

## 2. Target Tree Structure

After successful execution of the `insert` method calls, the resulting BST shall match the following hierarchical arrangement:

```
          9
        /   \
       4     20
      / \   /  \
     1   6 15   170
```

**Node Values and Relationships:**
- Root node: `9`
- Left child of `9`: `4`
- Right child of `9`: `20`
- Children of `4`: `1` (left) and `6` (right)
- Children of `20`: `15` (left) and `170` (right)

## 3. Provided Code Scaffolding

The initial code setup includes a `Node` class and a `BinarySearchTree` class with placeholder methods. A testing utility function, `traverse`, is also supplied to verify the structure of the constructed tree.

### 3.1 Node Class

The `Node` class represents an individual element within the BST. Each node stores a value and maintains references to its left and right children.

```javascript
class Node {
    constructor(value) {
        this.value = value;   // Data stored in the node
        this.left = null;     // Reference to left child node
        this.right = null;    // Reference to right child node
    }
}
```

### 3.2 BinarySearchTree Class Skeleton

The `BinarySearchTree` class encapsulates the tree structure and its operations. The `root` property references the topmost node.

```javascript
class BinarySearchTree {
    constructor() {
        this.root = null;     // Tree initially empty
    }

    /**
     * Inserts a value into the BST.
     * @param {number} value - The value to insert.
     */
    insert(value) {
        // Implementation to be completed
    }

    /**
     * Searches for a value in the BST.
     * @param {number} value - The value to find.
     * @returns {Node|null} - The node containing the value, or null if not found.
     */
    lookup(value) {
        // Implementation to be completed
    }

    // The remove method is omitted for this exercise
}
```

### 3.3 Testing Helper: Traverse Function

A recursive helper function is provided to serialize the tree structure into a JSON string. This facilitates visual verification in the console.

```javascript
/**
 * Recursively traverses the tree and returns an object representation.
 * This function is provided for testing purposes only.
 * @param {Node} node - The current node being visited.
 * @returns {Object} - Nested object representing the tree structure.
 */
function traverse(node) {
    if (node === null) return null;
    return {
        value: node.value,
        left: traverse(node.left),
        right: traverse(node.right)
    };
}

// Usage for verification:
// const tree = new BinarySearchTree();
// ... perform insertions ...
// console.log(JSON.stringify(traverse(tree.root), null, 2));
```

## 4. Implementation Requirements

### 4.1 Insert Method

The `insert(value)` method shall add a new node containing the specified value to the BST while preserving the binary search property.

**Behavioral Specifications:**
- If the tree is empty (`this.root === null`), the new node becomes the root.
- Otherwise, traverse the tree starting from the root:
  - If `value` is **less than** the current node's value, move to the left child.
  - If `value` is **greater than** the current node's value, move to the right child.
  - If the appropriate child reference is `null`, insert the new node at that position.
- Duplicate values are disallowed in this implementation; insertion of an existing value may be ignored or handled according to a defined policy.

**Example Insertion Sequence:**
```javascript
const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
```

### 4.2 Lookup Method

The `lookup(value)` method shall locate and return the node containing the specified value. If the value does not exist within the tree, the method shall return `null` or `false`.

**Behavioral Specifications:**
- Begin traversal at the root node.
- While the current node is not `null`:
  - If `value` equals the current node's value, return the current node.
  - If `value` is less than the current node's value, set the current node to its left child.
  - If `value` is greater, set the current node to its right child.
- If the loop exits without finding the value, return `null` (or `false`).

**Example Usage:**
```javascript
const foundNode = tree.lookup(20);   // Returns Node with value 20
const missingNode = tree.lookup(99); // Returns null
```

## 5. Verification Process

After implementing the `insert` and `lookup` methods, the structure of the tree can be verified using the provided `traverse` helper function.

**Verification Code:**
```javascript
const bst = new BinarySearchTree();
bst.insert(9);
bst.insert(4);
bst.insert(6);
bst.insert(20);
bst.insert(170);
bst.insert(15);
bst.insert(1);

console.log(JSON.stringify(traverse(bst.root), null, 2));
```

**Expected Console Output (Abbreviated):**
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

The output should precisely reflect the target tree structure defined in Section 2.

## 6. Additional Notes

- The `remove` method is intentionally excluded from this exercise due to the complexity introduced by the three deletion cases (leaf node, single child, two children). It will be addressed in a subsequent implementation session.
- The `traverse` function employs recursion, a concept that will be formally introduced later. For this exercise, it suffices to understand its purpose as a testing utility.
- Edge cases such as inserting duplicate values may be handled according to the implementer's discretion; a common approach is to ignore duplicates or throw an error.