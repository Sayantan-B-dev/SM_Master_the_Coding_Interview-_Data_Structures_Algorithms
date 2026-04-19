# Validating a Binary Search Tree (BST)

## 1. Introduction

Validating whether a given binary tree satisfies the properties of a Binary Search Tree (BST) is a classic problem in data structures and algorithms. It frequently appears in technical interviews and serves as an excellent exercise for applying tree traversal techniques, particularly Depth-First Search (DFS) and Breadth-First Search (BFS). The problem tests a candidate's understanding of recursive thinking, range-based constraints, and the fundamental definition of a BST.

The official problem statement (LeetCode #98) defines the task as follows: given the `root` of a binary tree, determine if it is a valid BST.

---

## 2. Definition of a Valid Binary Search Tree

A valid BST is defined by the following properties:

1. **Left Subtree Rule:** The left subtree of a node contains *only* nodes with keys strictly **less than** the node's key.
2. **Right Subtree Rule:** The right subtree of a node contains *only* nodes with keys strictly **greater than** the node's key.
3. **Recursive Property:** Both the left and right subtrees must themselves be valid binary search trees.

### 2.1 Critical Nuance: Global vs. Local Constraints

A common pitfall is to check only the immediate parent-child relationship. The BST property must hold **globally** across all ancestors. For example, in the invalid tree `[5,1,4,null,null,3,6]`, the root node's value is 5, but its right child's value is 4, which violates the rule that all nodes in the right subtree must be greater than the root. Even more subtle is the case of `[5,4,6,null,null,3,7]`, where the node 3 is in the right subtree of 5 (via 6) but is less than 5, making the tree invalid.

---

## 3. Algorithmic Approaches

Three primary approaches are used to solve the BST validation problem. Each leverages either DFS or BFS traversal patterns.

### 3.1 Approach 1: DFS with Range Constraints (Recursive)

**Intuition:** Each node in a BST has a valid range of values determined by its ancestors. Moving left tightens the upper bound; moving right tightens the lower bound.

**Algorithm Steps:**
1. Begin at the root with an initial valid range of `(-∞, ∞)`.
2. For each node, check whether its value lies strictly within the current `(min, max)` range.
3. Recursively validate the left subtree, using the current node's value as the new upper bound.
4. Recursively validate the right subtree, using the current node's value as the new lower bound.
5. If any node violates its range, return `false`. If all nodes satisfy their ranges, return `true`.

**Visual Representation:**

```
        5
       / \
      1   8
         / \
        6   9

Validation Flow:
1. Node 5: valid in (-∞, ∞)
2. Left child 1: valid in (-∞, 5)
3. Right child 8: valid in (5, ∞)
4. Node 8's left child 6: valid in (5, 8)  ← Must be > 5 and < 8
5. Node 8's right child 9: valid in (8, ∞)
```

**JavaScript Implementation:**

```javascript
/**
 * Validates a binary tree using DFS with range constraints (recursive).
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {boolean} - True if the tree is a valid BST, false otherwise.
 *
 * Time Complexity: O(n) - Each node is visited exactly once.
 * Space Complexity: O(h) - Recursion stack depth equals tree height.
 */
function isValidBST_DFS_Range(root) {
    /**
     * Recursive helper function that validates a subtree.
     * @param {TreeNode} node - Current node being examined.
     * @param {number} min - Lower bound (exclusive) for current node's value.
     * @param {number} max - Upper bound (exclusive) for current node's value.
     * @returns {boolean} - True if the subtree rooted at `node` is a valid BST.
     */
    function validate(node, min, max) {
        // Base case: an empty subtree is always valid
        if (node === null) {
            return true;
        }

        // Check if current node's value is within the allowed range
        // The BST definition requires STRICT inequality (no duplicates allowed)
        if (node.val <= min || node.val >= max) {
            return false;  // Node value violates BST property
        }

        // Recursively validate left and right subtrees
        // For left subtree: current node's value becomes the new upper bound
        // For right subtree: current node's value becomes the new lower bound
        return validate(node.left, min, node.val) &&
               validate(node.right, node.val, max);
    }

    // Initial call with infinite bounds
    return validate(root, -Infinity, Infinity);
}
```

**Edge Case Handling (JavaScript Number Bounds):** When node values can be exactly `-Infinity` or `Infinity` (which are valid numeric values in JavaScript), use `null` as the sentinel for unconstrained bounds:

```javascript
/**
 * Alternative implementation using null sentinels to avoid conflicts
 * with -Infinity/Infinity values.
 */
function isValidBST_DFS_Range_Safe(root) {
    function validate(node, min, max) {
        if (node === null) return true;

        // Check lower bound if it exists
        if (min !== null && node.val <= min) return false;
        // Check upper bound if it exists
        if (max !== null && node.val >= max) return false;

        return validate(node.left, min, node.val) &&
               validate(node.right, node.val, max);
    }

    return validate(root, null, null);
}
```

---

### 3.2 Approach 2: DFS with In-Order Traversal

**Intuition:** An in-order traversal of a valid BST visits nodes in strictly ascending order. By performing an in-order traversal and comparing each visited node's value with the previously visited node's value, we can verify the BST property.

**Algorithm Steps:**
1. Initialize a variable `prev` to track the previously visited node's value (initially `null`).
2. Perform an in-order traversal (left → node → right).
3. At each node, if `prev` is not `null`, verify that `current.val > prev`.
4. If any node violates the ascending order, return `false`.
5. Update `prev` to the current node's value and continue.
6. If traversal completes without violations, return `true`.

**Why In-Order Works:** The in-order traversal of a BST produces a sorted sequence because it visits the left subtree (smaller values), then the node (middle value), then the right subtree (larger values).

**JavaScript Implementation:**

```javascript
/**
 * Validates a BST using in-order DFS traversal.
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {boolean} - True if the tree is a valid BST.
 *
 * Time Complexity: O(n) - Each node visited once.
 * Space Complexity: O(h) - Recursion stack depth.
 */
function isValidBST_InOrder(root) {
    // prev stores the value of the previously visited node in in-order sequence.
    // Using an object with a mutable property allows updates across recursive calls.
    const prev = { val: null };

    /**
     * Recursive in-order traversal with validation.
     * @param {TreeNode} node - Current node.
     * @returns {boolean} - True if the subtree is a valid BST in-order sequence.
     */
    function inOrderValidate(node) {
        // Base case: empty node
        if (node === null) {
            return true;
        }

        // Step 1: Validate left subtree (all values must be < current node)
        if (!inOrderValidate(node.left)) {
            return false;
        }

        // Step 2: Validate current node against previous value
        // In a valid BST, in-order traversal yields strictly increasing values
        if (prev.val !== null && node.val <= prev.val) {
            return false;  // Violation: not strictly greater than previous
        }
        prev.val = node.val;  // Update previous value for next comparison

        // Step 3: Validate right subtree (all values must be > current node)
        return inOrderValidate(node.right);
    }

    return inOrderValidate(root);
}
```

**Iterative In-Order Implementation (Avoids Recursion):**

```javascript
/**
 * Iterative in-order validation using an explicit stack.
 * @param {TreeNode} root - The root node.
 * @returns {boolean} - True if valid BST.
 */
function isValidBST_InOrder_Iterative(root) {
    const stack = [];
    let current = root;
    let prev = null;

    while (stack.length > 0 || current !== null) {
        // Traverse to the leftmost node
        while (current !== null) {
            stack.push(current);
            current = current.left;
        }

        // Process the node
        current = stack.pop();

        // Check BST property: current value must be > previous value
        if (prev !== null && current.val <= prev) {
            return false;
        }
        prev = current.val;

        // Move to right subtree
        current = current.right;
    }

    return true;
}
```

---

### 3.3 Approach 3: BFS with Range Constraints (Iterative)

**Intuition:** The same range-constraint logic from the DFS approach can be implemented iteratively using BFS. A queue stores tuples of `(node, min, max)`. At each step, the current node is validated against its bounds, and children are enqueued with appropriately updated bounds.

**Algorithm Steps:**
1. Initialize a queue with the root node and bounds `(-∞, ∞)`.
2. While the queue is not empty:
   - Dequeue a tuple `(node, min, max)`.
   - If `node.val` is not within `(min, max)`, return `false`.
   - If the node has a left child, enqueue it with bounds `(min, node.val)`.
   - If the node has a right child, enqueue it with bounds `(node.val, max)`.
3. If the queue is exhausted without violations, return `true`.

**Why BFS Works:** BFS processes nodes level by level while propagating range constraints downward. This ensures that every node is checked against the global BST conditions derived from all its ancestors.

**JavaScript Implementation:**

```javascript
/**
 * Validates a BST using BFS with range constraints (iterative).
 * @param {TreeNode} root - The root node.
 * @returns {boolean} - True if valid BST.
 *
 * Time Complexity: O(n) - Each node processed once.
 * Space Complexity: O(w) - Queue stores at most the width of the tree.
 */
function isValidBST_BFS(root) {
    // Empty tree is a valid BST
    if (root === null) {
        return true;
    }

    // Queue stores objects: { node, min, max }
    // min and max are the exclusive bounds for the node's value
    const queue = [];
    queue.push({ node: root, min: -Infinity, max: Infinity });

    while (queue.length > 0) {
        // Dequeue the front element (FIFO behavior for BFS)
        const { node, min, max } = queue.shift();

        // Validate current node against its allowed range
        // Strict inequality: node.val must be > min and < max
        if (node.val <= min || node.val >= max) {
            return false;  // BST property violated
        }

        // Enqueue left child with updated upper bound
        // All nodes in left subtree must be < current node's value
        if (node.left !== null) {
            queue.push({
                node: node.left,
                min: min,          // Lower bound unchanged
                max: node.val      // New upper bound = current node's value
            });
        }

        // Enqueue right child with updated lower bound
        // All nodes in right subtree must be > current node's value
        if (node.right !== null) {
            queue.push({
                node: node.right,
                min: node.val,     // New lower bound = current node's value
                max: max           // Upper bound unchanged
            });
        }
    }

    // All nodes validated successfully
    return true;
}
```

---

## 4. Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|-----------------|------------------|-------|
| **DFS with Range (Recursive)** | O(n) | O(h) | h = tree height; O(n) worst-case (skewed tree) |
| **DFS In-Order (Recursive)** | O(n) | O(h) | Same as above |
| **DFS In-Order (Iterative)** | O(n) | O(h) | Explicit stack; same space bounds |
| **BFS with Range (Iterative)** | O(n) | O(w) | w = maximum width of tree; O(n) worst-case |

All approaches visit each node exactly once, resulting in linear time complexity. The space complexity differs: DFS uses memory proportional to tree height (stack depth), while BFS uses memory proportional to tree width (queue size).

---

## 5. Edge Cases and Constraints

### 5.1 Important Edge Cases

| Scenario | Expected Result | Reason |
|----------|-----------------|--------|
| Empty tree (`root = null`) | `true` | An empty tree trivially satisfies BST properties |
| Single node | `true` | No constraints are violated |
| Duplicate values | `false` | BST requires strict inequality (`<` and `>`, not `≤` and `≥`) |
| Integer boundary values | Handle carefully | Node values may be `-2^31` to `2^31 - 1` |

### 5.2 Common Pitfall: Local vs. Global Validation

Checking only immediate children is insufficient. Consider the following invalid BST:

```
      10
     /  \
    5   15
       /  \
      6   20
```

Node 6 is the left child of 15 (local condition satisfied: 6 < 15), but 6 is in the right subtree of 10, so it must be greater than 10. Since 6 < 10, the tree is invalid. This demonstrates why range constraints must be propagated from the root.

---

## 6. Summary Table: Choosing an Approach

| Approach | When to Use | Key Advantage |
|----------|-------------|---------------|
| **DFS with Range** | Default choice; clean recursive logic | Intuitive range propagation |
| **DFS In-Order** | When sorted order is conceptually helpful | Leverages BST's fundamental property |
| **BFS with Range** | When deep recursion might cause stack overflow | Iterative; avoids recursion limits |
| **In-Order Iterative** | Memory-constrained environments | Explicit stack control |

---

## 7. Conclusion

Validating a Binary Search Tree is a fundamental problem that reinforces essential concepts in tree traversal and constraint propagation. The three primary approaches—DFS with range constraints, in-order traversal, and BFS with range constraints—each offer different trade-offs in terms of implementation clarity and memory usage. A correct solution must enforce the BST property globally across all ancestors, not merely locally between parent and child nodes. Mastery of this problem provides a strong foundation for more advanced tree and graph algorithms.

---

## 8. Practice Resources

- **LeetCode Problem 98:** [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- **Additional Test Cases:** `[2,1,3]`, `[5,1,4,null,null,3,6]`, `[0]`, `[1,1]`, `[0,-1]`, `[5,14,null,1]`, `[5,4,6,null,null,3,7]`, `[10,5,15,null,null,6,20]`