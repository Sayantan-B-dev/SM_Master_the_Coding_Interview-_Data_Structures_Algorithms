# Binary Search Tree Removal Operation

## 1. Introduction

The removal (deletion) operation in a Binary Search Tree (BST) is the most complex of the core operations. Unlike insertion and lookup, which follow a straightforward traversal path to a leaf or a match, removal must account for the structural implications of eliminating a node while preserving the binary search property.

The difficulty arises because a node to be deleted may occupy an internal position with one or two children. The BST property requires that all values in the left subtree remain less than the node's value and all values in the right subtree remain greater. Simply excising a node could break this invariant.

This document presents a systematic approach to implementing the `remove` method in JavaScript, covering the three distinct cases encountered during deletion and providing a fully commented code solution.

## 2. Three Cases of Deletion

When removing a node from a BST, the node to be deleted falls into exactly one of three categories based on its number of children.

### 2.1 Case 1: Deleting a Leaf Node (No Children)

If the target node has no children (i.e., both `left` and `right` references are `null`), removal is trivial. The node is simply detached by setting the corresponding child reference of its parent to `null`.

**ASCII Representation:**
```
Before:          After:
    10              10
   /  \            /  \
  5    15   =>    5    15
 /
3                 (3 removed)
```
Here, node `3` is a leaf. The left child of node `5` becomes `null`.

### 2.2 Case 2: Deleting a Node with One Child

If the target node has exactly one child (either a left child or a right child, but not both), removal involves bypassing the node. The parent of the deleted node adopts the deleted node's single child as its own child.

**Example: Removing a node with only a right child:**
```
Before:          After:
    10              10
   /  \            /  \
  5    15   =>    7    15
   \
    7
```
Node `5` has only a right child `7`. Node `5` is removed, and `7` becomes the new left child of `10`.

### 2.3 Case 3: Deleting a Node with Two Children

This case is the most involved. The node to be deleted has both a left and a right subtree. Removing the node directly would orphan one of the subtrees. To maintain the BST property, the node is replaced with its **in-order successor** (or alternatively, its **in-order predecessor**).

- **In-order Successor:** The node with the smallest value in the right subtree of the target node. This successor is guaranteed to have no left child, making its removal straightforward (Case 1 or 2).
- **In-order Predecessor:** The node with the largest value in the left subtree. Either works; the choice is implementation-dependent.

**Algorithm Steps for Case 3:**
1. Locate the in-order successor (minimum value in the right subtree).
2. Copy the successor's value into the target node.
3. Recursively delete the successor node from the right subtree (which will fall into Case 1 or 2).

**ASCII Representation:**
```
Before:                   After:
      10                      10
     /  \                    /  \
    5    15     =>          5    17
   / \   / \               / \   / \
  3   7 12  20            3   7 12  20
          \
           17
```
Here, deleting `15` requires finding the in-order successor, which is `17` (the leftmost node in the right subtree). The value `17` replaces `15`, and the original `17` node is removed (as a leaf).

## 3. Implementation in JavaScript

The `remove` method is implemented recursively. The recursive approach simplifies handling of parent references and the three deletion cases.

### 3.1 Code Listing

```javascript
/**
 * Removes a node with the specified value from the BST.
 * Returns the new root of the (sub)tree after deletion.
 * @param {number} value - The value to remove.
 * @param {Node} currentNode - The current node in recursion (defaults to root).
 * @returns {Node|null} - The updated node for the current position.
 */
remove(value, currentNode = this.root) {
    // Base case: value not found
    if (currentNode === null) {
        return null;
    }

    // Step 1: Traverse to find the node to delete
    if (value < currentNode.value) {
        // Target is in left subtree; recursively remove from left
        currentNode.left = this.remove(value, currentNode.left);
        return currentNode;
    } else if (value > currentNode.value) {
        // Target is in right subtree; recursively remove from right
        currentNode.right = this.remove(value, currentNode.right);
        return currentNode;
    } else {
        // Step 2: Node to delete is found (value === currentNode.value)

        // Case 1: No children (leaf node)
        if (currentNode.left === null && currentNode.right === null) {
            return null;  // Remove by returning null to parent
        }

        // Case 2: One child
        if (currentNode.left === null) {
            // Only right child exists
            return currentNode.right;
        }
        if (currentNode.right === null) {
            // Only left child exists
            return currentNode.left;
        }

        // Case 3: Two children
        // Find in-order successor (minimum value in right subtree)
        const successor = this.findMin(currentNode.right);
        // Replace current node's value with successor's value
        currentNode.value = successor.value;
        // Delete the successor node from the right subtree
        currentNode.right = this.remove(successor.value, currentNode.right);
        return currentNode;
    }
}

/**
 * Helper: Finds the node with the minimum value in a given subtree.
 * @param {Node} node - The root of the subtree to search.
 * @returns {Node} - The node with the smallest value.
 */
findMin(node) {
    while (node.left !== null) {
        node = node.left;
    }
    return node;
}
```

### 3.2 Explanation of Recursive Logic

1. **Base Case (Not Found):** If `currentNode` is `null`, the value does not exist in the tree. The method returns `null` to indicate no change at that position.

2. **Traversal:** The method compares the target `value` with `currentNode.value`. If smaller, it recurses into the left subtree; if larger, into the right subtree. The recursive call returns the updated child node, which is reassigned to `currentNode.left` or `currentNode.right`.

3. **Deletion Cases (When Found):**
   - **Leaf:** Returns `null`, effectively deleting the node by breaking the parent's reference.
   - **One Child:** Returns the existing child (`left` or `right`), which the parent will adopt.
   - **Two Children:** Finds the in-order successor using `findMin`, copies its value, and then recursively deletes the successor from the right subtree.

4. **Return Value:** Each recursive call returns the (possibly modified) current node, ensuring the tree structure remains intact up the call stack.

### 3.3 In-Order Successor Function

The `findMin` helper iteratively traverses the left children of a given subtree until it reaches a node with no left child. This node contains the minimum value in that subtree.

## 4. Visualizing the Deletion Process

Using a tool like VisualGo to step through deletion animations can solidify understanding. The following sequence summarizes the logic observed when removing a node with two children (e.g., value `51` in a sample tree):

1. **Locate Target:** Traverse from the root to the node containing `51`.
2. **Find Successor:** From the right child of `51`, move left repeatedly to find the smallest value greater than `51`. Let this be `54`.
3. **Replace Value:** Overwrite `51` with `54`.
4. **Delete Successor:** Remove the original `54` node from the right subtree. Since `54` had no left child (by definition of being the leftmost), its removal follows Case 1 or Case 2.

## 5. Complexity Analysis

| Case | Time Complexity (Balanced) | Time Complexity (Unbalanced) |
|------|----------------------------|------------------------------|
| **Traversal to Find Node** | O(log n) | O(n) |
| **Finding Successor** | O(log n) | O(n) |
| **Overall** | O(log n) | O(n) |

In a balanced BST, the height is logarithmic, so both finding the target and finding the successor take O(log n) time. The recursive removal of the successor adds another O(log n) traversal, but the constant factors are small.

Space complexity is O(h) due to recursion stack depth, where `h` is the height of the tree. An iterative implementation could reduce this to O(1).

## 6. Edge Cases and Considerations

- **Deleting the Root:** The recursive method handles root deletion naturally. If the root is removed, the method returns the new root (either `null`, the single child, or the modified node with successor value).
- **Duplicate Values:** The standard BST removal algorithm assumes unique values. If duplicates are allowed, additional logic is required to decide which occurrence to remove.
- **Empty Tree:** Calling `remove` on an empty tree simply returns `null` and does nothing.

## 7. Summary

- The `remove` operation in a BST involves three distinct cases based on the number of children of the target node.
- Leaf nodes are deleted by setting the parent's reference to `null`.
- Nodes with one child are bypassed by linking the parent directly to the child.
- Nodes with two children are replaced by their in-order successor (or predecessor) to maintain the BST property.
- A recursive implementation elegantly handles the traversal and reassignment of child references.
- The time complexity is O(log n) for balanced trees and O(n) in the worst-case unbalanced scenario.
- Mastery of the removal algorithm reinforces understanding of tree traversal, pointer manipulation, and the importance of maintaining invariants in data structures.