# Reversing a String: Algorithm and Implementation

## 1. Problem Statement

Given an input string, the task is to return a new string containing the same characters in reverse order.

**Example:**
```
Input:  "Hi My name is Andrei"
Output: "ierdnA si eman yM iH"
```

This is a foundational string manipulation problem frequently encountered in technical interviews.

## 2. Conceptual Approach

As established in prior discussions, strings can be treated as **character arrays**. Reversing a string is equivalent to reversing an array of characters. The solution workflow follows a three-step pattern:

1. **Convert** the input string to an array of individual characters.
2. **Reverse** the array using either built-in methods or manual algorithms.
3. **Reconstruct** the string by joining the reversed array elements.

## 3. Implementation Strategies

### 3.1 Using Built-in JavaScript Methods

The simplest and most concise approach utilises native array methods.

```javascript
function reverseString(str) {
    // Step 1: Split string into array of characters
    const charArray = str.split('');
    
    // Step 2: Reverse the array (mutates the array)
    charArray.reverse();
    
    // Step 3: Join the reversed array back into a string
    return charArray.join('');
}

// One-liner equivalent
// return str.split('').reverse().join('');
```

**Time Complexity:** O(n) – Each method (`split`, `reverse`, `join`) traverses the entire array once.
**Space Complexity:** O(n) – A new array of size *n* is created.

### 3.2 Manual Reversal Using Two-Pointer Technique

For interviews where built-in methods are disallowed or when demonstrating algorithmic thinking, the two-pointer (or in-place swap) approach is preferred.

```javascript
function reverseStringManual(str) {
    // Convert to array for mutability
    const charArray = str.split('');
    
    let leftIndex = 0;
    let rightIndex = charArray.length - 1;
    
    // Swap characters from both ends moving toward center
    while (leftIndex < rightIndex) {
        // ES6 destructuring swap
        [charArray[leftIndex], charArray[rightIndex]] = 
        [charArray[rightIndex], charArray[leftIndex]];
        
        leftIndex++;
        rightIndex--;
    }
    
    // Reconstruct string
    return charArray.join('');
}
```

**Algorithm Steps:**
1. Initialise two pointers: `leftIndex` at the start (0) and `rightIndex` at the end (`length - 1`).
2. While `leftIndex` is less than `rightIndex`, swap the characters at these positions.
3. Increment `leftIndex` and decrement `rightIndex` to move inward.
4. Once the pointers meet or cross, the array is reversed.

**Time Complexity:** O(n/2) ≈ O(n) – The loop runs for half the length of the string.
**Space Complexity:** O(n) – The character array occupies linear space.

### 3.3 Backward Traversal with String Concatenation

An alternative approach builds the reversed string by iterating from the end.

```javascript
function reverseStringLoop(str) {
    let reversed = '';
    
    // Iterate from last character to first
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    
    return reversed;
}
```

**Time Complexity:** O(n) – Single pass through the string.
**Space Complexity:** O(n) – New string of length *n* is constructed.

> **Note:** In languages with immutable strings (like JavaScript), repeated string concatenation can be less efficient due to intermediate string creation. Using an array and `join` is generally more performant.

### 3.4 Recursive Approach

For completeness, a recursive solution is presented.

```javascript
function reverseStringRecursive(str) {
    // Base case: empty string or single character
    if (str === '') {
        return '';
    }
    // Recursive step: last character + reverse of remaining substring
    return str[str.length - 1] + reverseStringRecursive(str.slice(0, -1));
}
```

**Time Complexity:** O(n²) due to `slice` creating new substrings at each recursive call.
**Space Complexity:** O(n) call stack depth.

## 4. Complexity Comparison

| Method                    | Time Complexity | Space Complexity | Remarks                                      |
|---------------------------|-----------------|------------------|----------------------------------------------|
| Built-in `split/reverse/join` | O(n)            | O(n)             | Concise; preferred for production code.      |
| Two-pointer swap          | O(n)            | O(n)             | Demonstrates algorithmic proficiency.         |
| Backward loop with string concat | O(n)        | O(n)             | Simple; may be less efficient due to string immutability. |
| Recursive                 | O(n²)           | O(n)             | Elegant but inefficient; avoid in practice.  |

## 5. Key Interview Insights

- **Treat strings as arrays:** This mindset unlocks numerous array-based algorithms for string manipulation.
- **Multiple valid solutions exist:** Interviewers value the ability to explain trade-offs and choose appropriate methods based on constraints.
- **Built-in methods are acceptable** if the interviewer permits them, but demonstrating understanding of underlying mechanics (e.g., two-pointer swap) is advantageous.
- **Always discuss time and space complexity** to showcase analytical skills.

## 6. Summary

Reversing a string is a fundamental exercise that reinforces the connection between strings and character arrays. Efficient solutions operate in O(n) time and O(n) space. The choice of implementation—built-in methods, manual loops, or two-pointer techniques—should be guided by interview constraints and the need to communicate algorithmic reasoning.