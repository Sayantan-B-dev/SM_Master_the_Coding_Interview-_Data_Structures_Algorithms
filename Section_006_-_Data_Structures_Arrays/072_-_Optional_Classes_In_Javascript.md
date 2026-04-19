# Advanced Object Concepts in JavaScript

## 1. Introduction

In JavaScript, objects exhibit behaviours that distinguish them from primitive data types. Understanding these advanced characteristics is essential for effective programming, particularly when working with data structures and object-oriented design patterns. This document examines three fundamental concepts:

- **Reference Type:** The mechanism by which objects are stored and accessed via memory references.
- **Context:** The determination of the current execution environment as reflected by the `this` keyword.
- **Instantiation:** The process of creating multiple instances from a class blueprint.

These concepts form the foundation for building robust and reusable code in modern JavaScript applications.

---

## 2. Reference Type

### 2.1 Primitive Types versus Reference Types

JavaScript classifies data types into two broad categories:

| Category          | Types                                                                 | Behaviour                                                                                   |
|-------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Primitive Types** | `number`, `string`, `boolean`, `null`, `undefined`, `symbol`          | Defined by the language specification. Values are immutable and stored directly in memory.   |
| **Reference Types** | `object`, `array`, `function` (and any user-defined non-primitive)    | Created by the programmer. Variables store a reference (memory address) to the actual data.  |

Primitive values are compared by their content, whereas reference types are compared by their memory address.

### 2.2 Behavioural Demonstration

Consider the following code snippets and their outcomes:

```javascript
// Primitive comparison
let num1 = 1;
let num2 = 1;
console.log(num1 === num2); // true (values are identical)

// Array comparison (reference type)
let array1 = [];
let array2 = [];
console.log(array1 === array2); // false (different memory addresses)

// Object reference assignment
let object1 = { value: 10 };
let object2 = object1;        // object2 references the same memory location as object1
let object3 = { value: 10 };  // object3 is a new, distinct object

console.log(object1 === object2); // true (same reference)
console.log(object1 === object3); // false (different references)
```

### 2.3 Mutability and Shared References

When two variables reference the same object, modifications made through one variable are visible to the other. This occurs because both variables point to the same underlying data structure.

```javascript
object1.value = 15;
console.log(object2.value); // 15 (affected by change via object1)
console.log(object3.value); // 10 (unaffected, separate object)
```

### 2.4 Conceptual Diagram

```
Memory Representation:

Box 1 (Address: 0x001)          Box 3 (Address: 0x003)
+-------------------+           +-------------------+
| { value: 15 }     |           | { value: 10 }     |
+-------------------+           +-------------------+
        ↑                                 ↑
        |                                 |
object1 (stores 0x001)             object3 (stores 0x003)
object2 (stores 0x001)
```

The variables `object1` and `object2` hold the same memory address (`0x001`), while `object3` holds a distinct address (`0x003`). Consequently, changes to the contents at `0x001` affect both `object1` and `object2`.

---

## 3. Context and the `this` Keyword

### 3.1 Scope versus Context

**Scope** and **context** are distinct concepts often conflated:

- **Scope** refers to the visibility and accessibility of variables within a particular region of code. In JavaScript, a new scope is created by functions or block statements (`{ }`). Variables declared within a scope are not accessible outside it.

  ```javascript
  function demoScope() {
      let localVar = 'visible only inside function';
  }
  console.log(localVar); // ReferenceError: localVar is not defined
  ```

- **Context** pertains to the object that the currently executing code belongs to. It is determined by the value of the `this` keyword.

### 3.2 Understanding `this`

The `this` keyword references the object that is the **execution context** at the time of invocation. Its value is dynamic and depends on how a function is called.

In the global execution context (outside any function or object), `this` refers to the global object, which is `window` in browsers.

```javascript
console.log(this);           // Window object (in browser environment)
console.log(this === window); // true
this.alert('Hello');         // Equivalent to window.alert('Hello')
```

### 3.3 Determining the Value of `this`

A helpful rule for deducing `this` is: **`this` refers to whatever is to the left of the dot at the time of invocation.**

#### Example 1: Function in Global Context

```javascript
function showContext() {
    console.log(this);
}
showContext(); // Window object (left of dot is implicitly window)
```

#### Example 2: Method Invocation on an Object

```javascript
const myObject = {
    property: 'value',
    myMethod: function() {
        console.log(this);
    }
};
myObject.myMethod(); // myObject (left of dot is myObject)
```

In the second example, `myObject` is to the left of the dot, so `this` inside `myMethod` refers to `myObject`.

### 3.4 Importance in Instantiation

The `this` keyword becomes particularly significant when creating multiple instances of an object. Within a constructor function or class, `this` refers to the newly created instance, allowing properties and methods to be assigned to that specific object.

---

## 4. Instantiation

### 4.1 Concept and Motivation

**Instantiation** is the process of creating a concrete instance from a class blueprint. This mechanism enables the creation of multiple objects sharing the same structure and behaviour without duplicating code. In large-scale applications, such as multiplayer games or complex user interfaces, instantiation promotes code reusability and maintainability.

### 4.2 Class Syntax in JavaScript

ES6 introduced the `class` keyword, providing a clearer and more familiar syntax for object-oriented programming compared to traditional prototype-based inheritance.

#### Basic Class Structure

```javascript
class ClassName {
    constructor(parameters) {
        // Initialisation code executed upon instance creation
        this.property = value;
    }

    methodName() {
        // Method available to all instances
    }
}
```

- **`constructor`:** A special method invoked automatically when a new instance is created using the `new` keyword. It initialises the object's properties.
- **`this` inside constructor:** Refers to the newly created instance.

### 4.3 Example: Player Class

```javascript
class Player {
    constructor(name, type) {
        this.name = name;   // Instance property
        this.type = type;   // Instance property
        console.log('Player constructor executed');
    }

    introduce() {
        // Template literal for string interpolation
        console.log(`Hi, I am ${this.name}, I'm a ${this.type}`);
    }
}
```

### 4.4 Inheritance with `extends` and `super`

The `extends` keyword allows a class to inherit properties and methods from a parent (base) class. The `super` keyword is used within the child class constructor to call the parent class constructor, ensuring proper initialisation of inherited properties.

#### Example: Wizard Class Extending Player

```javascript
class Wizard extends Player {
    constructor(name, type) {
        // Call parent class constructor with required arguments
        super(name, type);
        console.log('Wizard constructor executed');
    }

    play() {
        console.log(`WEEEE, I'm a ${this.type}`);
    }
}
```

**Key Points:**
- `extends` establishes the inheritance relationship.
- `super(name, type)` invokes the `Player` constructor, setting `this.name` and `this.type`.
- The `super` call **must** occur before accessing `this` in the child constructor; otherwise, a `ReferenceError` is thrown.

### 4.5 Creating Instances

Instances are created using the `new` operator followed by the class name and constructor arguments.

```javascript
const wizard1 = new Wizard('Shelly', 'Healer');
const wizard2 = new Wizard('Shawn', 'Dark Magic');

// Invoking inherited method
wizard1.introduce(); // Output: Hi, I am Shelly, I'm a Healer

// Invoking child-specific method
wizard1.play();      // Output: WEEEE, I'm a Healer

wizard2.introduce(); // Output: Hi, I am Shawn, I'm a Dark Magic
```

### 4.6 Execution Flow During Instantiation

When `new Wizard('Shelly', 'Healer')` is executed:

1. A new empty object is created.
2. The `Wizard` constructor is invoked.
3. `super(name, type)` calls the `Player` constructor.
4. The `Player` constructor assigns `this.name` and `this.type`.
5. Control returns to the `Wizard` constructor.
6. Any additional initialisation specific to `Wizard` occurs.
7. The fully constructed object is assigned to `wizard1`.

### 4.7 Historical Note: Prototypal Inheritance

Prior to ES6, similar behaviour was achieved using constructor functions and prototype manipulation, often termed "classical inheritance" in JavaScript. The modern class syntax is essentially syntactic sugar over this underlying prototype system, offering improved readability and reduced boilerplate.

```javascript
// Legacy approach (not recommended for new code)
function Player(name, type) {
    this.name = name;
    this.type = type;
}
Player.prototype.introduce = function() {
    console.log('Hi, I am ' + this.name + ", I'm a " + this.type);
};

function Wizard(name, type) {
    Player.call(this, name, type);
}
Wizard.prototype = Object.create(Player.prototype);
Wizard.prototype.constructor = Wizard;
Wizard.prototype.play = function() {
    console.log("WEEEE, I'm a " + this.type);
};
```

The modern class syntax is preferred for its clarity and alignment with object-oriented conventions found in other programming languages.

---

## 5. Summary

- **Reference Type:** Non-primitive values are stored as references. Assigning an object to another variable copies the reference, not the actual data. Modifications via one reference affect all references pointing to the same object.
- **Context (`this`):** The `this` keyword refers to the object that is the current execution context, determined by how a function is invoked. It is essential for accessing instance-specific properties within methods.
- **Instantiation:** Classes serve as blueprints for creating objects. The `new` keyword instantiates an object, invoking the `constructor`. Inheritance using `extends` and `super` allows child classes to reuse and extend parent functionality.

These concepts collectively empower developers to write modular, reusable, and maintainable code, forming the basis for advanced JavaScript patterns and data structure implementations.