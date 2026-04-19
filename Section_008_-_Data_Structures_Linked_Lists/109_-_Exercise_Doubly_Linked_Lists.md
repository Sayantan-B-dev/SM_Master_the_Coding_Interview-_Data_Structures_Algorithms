# Exercise: Implementation of a Doubly Linked List

## 1. Objective

The purpose of this exercise is to apply the conceptual understanding of doubly linked lists by implementing a fully functional `DoublyLinkedList` class in JavaScript. Building upon the previously constructed singly linked list, the task involves modifying the node structure and updating all core methods to accommodate bidirectional pointers (`next` and `prev`).

## 2. Prerequisite Knowledge

Before attempting this implementation, ensure familiarity with the following concepts:

- Singly linked list node structure (`value`, `next`).
- Core linked list operations: `append`, `prepend`, `insert`, `remove`, and traversal.
- Pointer manipulation and reference semantics in JavaScript.
- Time complexity implications of bidirectional linkage.

## 3. Exercise Requirements

Convert the existing `LinkedList` class (singly linked) into a `DoublyLinkedList` class. The new implementation must maintain a doubly linked structure where each node contains `value`, `next`, and `prev` properties. All methods must correctly update both forward and backward pointers.

### 3.1 Node Class Modification

Create a `DoublyNode` class that includes a `prev` pointer in addition to `value` and `next`.

**Expected Structure:**

```javascript
class DoublyNode {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}
```

### 3.2 DoublyLinkedList Class Outline

The class should expose the following methods with appropriate doubly linked behavior:

| Method | Description |
| :--- | :--- |
| `constructor(value)` | Initializes the list with a single node. Sets `head`, `tail`, and `length`. |
| `append(value)` | Adds a node to the end of the list. Updates `tail` and `prev` pointers. |
| `prepend(value)` | Adds a node to the beginning of the list. Updates `head` and `prev` pointers. |
| `insert(index, value)` | Inserts a node at the specified index. Adjusts `next` and `prev` of adjacent nodes. |
| `remove(index)` | Deletes the node at the specified index. Updates surrounding pointers. |
| `printList()` | Returns an array of node values in forward order. |
| `printListReverse()` | (Optional) Returns an array of node values in reverse order using `prev` pointers. |
| `traverseToIndex(index)` | Helper method to locate a node at a given index. |

### 3.3 Specific Considerations for Each Method

#### 3.3.1 Constructor

- Create a new `DoublyNode` with the provided value.
- Set `head` and `tail` to this node.
- Ensure `prev` of the head is `null`.
- Set `length = 1`.

#### 3.3.2 Append

- Create a new node.
- Set `newNode.prev = this.tail`.
- Set `this.tail.next = newNode`.
- Update `this.tail = newNode`.
- Increment `length`.

#### 3.3.3 Prepend

- Create a new node.
- Set `newNode.next = this.head`.
- Set `this.head.prev = newNode`.
- Update `this.head = newNode`.
- Increment `length`.

#### 3.3.4 Insert

- Validate `index`.
- If `index === 0`, delegate to `prepend`.
- If `index >= this.length`, delegate to `append`.
- Otherwise, traverse to the `leader` node at `index - 1`.
- Create new node.
- Set `newNode.next = leader.next`.
- Set `newNode.prev = leader`.
- Set `leader.next.prev = newNode`.
- Set `leader.next = newNode`.
- Increment `length`.

#### 3.3.5 Remove

- Validate `index`.
- If `index === 0`: update `head = head.next`; if new head exists, set `head.prev = null`; else `tail = null`.
- Else:
  - Traverse to `leader` at `index - 1`.
  - `unwantedNode = leader.next`.
  - `leader.next = unwantedNode.next`.
  - If `unwantedNode.next` exists, set `unwantedNode.next.prev = leader`.
  - If removing the tail (`index === this.length - 1`), update `tail = leader`.
- Decrement `length`.

#### 3.3.6 PrintListReverse (Optional)

- Start from `tail`.
- Traverse backwards using `prev` pointers until `null`.
- Collect values into an array and return.

## 4. Implementation Guidelines

### 4.1 Code Skeleton

A recommended starting template is provided below.

```javascript
class DoublyNode {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    constructor(value) {
        this.head = new DoublyNode(value);
        this.tail = this.head;
        this.length = 1;
    }

    append(value) {
        // TODO: Implement append for doubly linked list
    }

    prepend(value) {
        // TODO: Implement prepend for doubly linked list
    }

    insert(index, value) {
        // TODO: Implement insert for doubly linked list
    }

    remove(index) {
        // TODO: Implement remove for doubly linked list
    }

    printList() {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }

    // Optional: Reverse traversal
    printListReverse() {
        const array = [];
        let currentNode = this.tail;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.prev;
        }
        return array;
    }

    traverseToIndex(index) {
        let counter = 0;
        let currentNode = this.head;
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }
}
```

### 4.2 Testing the Implementation

Use the following test cases to verify correctness:

```javascript
const dll = new DoublyLinkedList(10);
dll.append(5);
dll.append(16);
console.log(dll.printList());          // Expected: [10, 5, 16]
console.log(dll.printListReverse());   // Expected: [16, 5, 10]

dll.prepend(1);
console.log(dll.printList());          // Expected: [1, 10, 5, 16]

dll.insert(2, 99);
console.log(dll.printList());          // Expected: [1, 10, 99, 5, 16]

dll.remove(3);
console.log(dll.printList());          // Expected: [1, 10, 99, 16]
```

### 4.3 Common Pitfalls to Avoid

| Pitfall | Consequence | Prevention |
| :--- | :--- | :--- |
| Forgetting to update `prev` pointers | Broken backward traversal; potential null reference errors. | Always update both `next` and `prev` of affected nodes. |
| Not handling edge cases (empty list, single node) | Runtime errors when accessing `prev` of `null`. | Add conditional checks for `head` and `tail` updates. |
| Incorrect pointer assignment order | Loss of references leading to detached nodes. | Assign `prev` pointers after establishing new `next` links, or store temporary references. |
| Neglecting to update `tail` on removal | Tail points to a removed node, causing incorrect list state. | Check if removed index equals `length - 1` and reassign `tail`. |

## 5. Expected Learning Outcomes

Upon successful completion of this exercise, the following competencies will be demonstrated:

- Ability to extend a singly linked list to a doubly linked structure.
- Proficiency in managing multiple pointer reassignments during insertions and deletions.
- Understanding of the trade-offs between memory overhead and operational efficiency.
- Capability to implement bidirectional traversal.

## 6. Solution Reference

The complete solution to this exercise is presented in the subsequent video and accompanying code materials. It is strongly recommended to attempt the implementation independently before consulting the solution to maximize learning retention.