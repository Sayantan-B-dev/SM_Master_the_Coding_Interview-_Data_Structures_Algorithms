# Implementation Approach: JavaScript Classes for Data Structures

## 1. Introduction

Throughout this course, custom data structures will be implemented from fundamental principles using the **JavaScript programming language**. The primary construct employed for defining these structures is the `class` keyword, which provides a familiar and widely adopted syntax for object-oriented programming.

This document outlines the rationale behind the chosen implementation approach and provides supplementary information regarding variable declaration practices in JavaScript.

---

## 2. Use of JavaScript Classes

### 2.1 Rationale

The `class` syntax in JavaScript offers a structured and intuitive mechanism for encapsulating data and associated behaviours. Key advantages of this approach include:

- **Familiarity Across Languages:** The class-based paradigm is common to numerous programming languages, including Java, C++, Python, and C#. This reduces the cognitive load for learners transitioning between languages.
- **Encapsulation:** Classes group properties (data) and methods (functions) together, mirroring the conceptual model of a data structure as a self-contained entity.
- **Reusability and Extensibility:** Class definitions can be instantiated multiple times and extended through inheritance, facilitating the construction of complex structures from simpler components.

### 2.2 Basic Class Syntax

The following template illustrates the standard structure used for defining a data structure in JavaScript:

```javascript
class DataStructureName {
    constructor(parameters) {
        // Initialise properties, e.g., storage array, size counters
        this.storage = [];
        this.length = 0;
    }

    methodOne() {
        // Define operational behaviour
    }

    methodTwo() {
        // Define additional functionality
    }
}
```

### 2.3 Application to Data Structures

When implementing structures such as arrays, linked lists, stacks, or queues, the class definition serves as a blueprint. For instance, a custom dynamic array class would contain:

- A constructor to set up the underlying storage mechanism.
- Methods for insertion, deletion, access, and traversal.
- Auxiliary properties to track capacity and element count.

This modular approach isolates the internal representation from external usage, a principle known as **abstraction**.

---

## 3. Variable Declaration in JavaScript

### 3.1 Declarations Used: `var`, `let`, and `const`

Throughout the course materials, the keywords `var`, `let`, and `const` appear for variable declaration. While a deep understanding of their distinctions is not essential for grasping data structure concepts, a brief overview is provided for contextual awareness.

| Keyword | Scope          | Reassignable | Redeclarable | Hoisting Behaviour                      |
|---------|----------------|--------------|--------------|-----------------------------------------|
| `var`   | Function-scoped| Yes          | Yes          | Hoisted with initialisation to `undefined` |
| `let`   | Block-scoped   | Yes          | No           | Hoisted but not initialised (Temporal Dead Zone) |
| `const` | Block-scoped   | No           | No           | Hoisted but not initialised (Temporal Dead Zone) |

### 3.2 Recommended Modern Practice

In contemporary JavaScript development:

- **`const`** is preferred for values that should not be reassigned.
- **`let`** is used when reassignment is necessary.
- **`var`** is generally avoided due to its function-scoping behaviour, which can lead to unintended consequences.

For the purpose of understanding and implementing data structures, any of these declarations may appear; the core algorithmic logic remains unaffected.

---

## 4. Supplementary Resources

Learners seeking additional clarity on the distinctions between `var`, `let`, and `const` are encouraged to consult the following external reference:

- **Article:** "Var vs Let vs Const" – [https://dev.to/sethusenthil/var-vs-let-vs-const-1cgc](https://dev.to/sethusenthil/var-vs-let-vs-const-1cgc)

This resource provides detailed explanations and practical examples of scope, hoisting, and best practices.

---

## 5. Summary

- Data structures in this course will be constructed using **JavaScript classes** due to their clarity, cross-language familiarity, and suitability for encapsulation.
- Variable declarations using `var`, `let`, and `const` appear interchangeably; understanding the nuances of each is beneficial but not mandatory for mastering the material.
- The class-based implementation strategy ensures that the focus remains on the underlying data structure principles, independent of language-specific idiosyncrasies.