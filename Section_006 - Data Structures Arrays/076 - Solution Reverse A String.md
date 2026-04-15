# Reversing a String: Implementation Strategies and Analysis

## 1. Problem Statement

Given an input string, the task is to produce a new string that contains the same characters arranged in reverse order. This is a classic string manipulation problem frequently presented in technical interviews to assess a candidate's understanding of arrays, iteration, and language-specific features.

**Example:**
```
Input:  "Hi My name is Andrei"
Output: "ierdnA si eman yM iH"
```

## 2. Input Validation Considerations

Robust functions include validation of input parameters before performing core logic. The following checks are recommended:

- **Existence Check:** Verify that the input is not `undefined` or `null`.
- **Type Check:** Confirm that the input is of type `string` using the `typeof` operator.
- **Length Check:** If the string length is less than 2 (i.e., empty string or single character), it can be returned unchanged as it is already trivially reversed.

```javascript
function reverseString(str) {
    // Input validation
    if (!str || typeof str !== 'string' || str.length < 2) {
        return str;
    }
    // Core reversal logic follows...
}
```

These validations prevent runtime errors and improve the function's reliability.

## 3. Implementation Approaches

### 3.1 Manual Iteration with Array Accumulation

This approach builds the reversed string by iterating from the last character to the first and appending each character to an array, which is subsequently joined.

```javascript
function reverseStringManual(str) {
    // Input validation (optional but recommended)
    if (!str || typeof str !== 'string' || str.length < 2) {
        return str;
    }

    const backwardsArray = [];
    const totalItems = str.length - 1; // Index of last character

    // Iterate from the end of the string to the beginning
    for (let i = totalItems; i >= 0; i--) {
        backwardsArray.push(str[i]); // Access character using bracket notation
    }

    // Convert array back to string
    return backwardsArray.join('');
}
```

**Explanation:**
- `totalItems` stores the zero-based index of the final character.
- The `for` loop decrements `i` from the last index down to `0`.
- Each character is pushed onto `backwardsArray`.
- The `join('')` method concatenates array elements into a single string.

**Time Complexity:** O(n) – The loop iterates through each character once.
**Space Complexity:** O(n) – An array of size *n* is created to hold the reversed characters.

### 3.2 Utilising Built-in Array Methods

JavaScript arrays provide a `reverse()` method that can be leveraged after converting the string to an array of characters.

```javascript
function reverseStringBuiltIn(str) {
    // Input validation omitted for brevity; include as shown above
    return str.split('')   // Step 1: Convert string to character array
              .reverse()   // Step 2: Reverse the array in-place
              .join('');   // Step 3: Convert array back to string
}
```

**Explanation:**
- `split('')` divides the string into an array where each element is a single character.
- `reverse()` mutates the array to invert element order.
- `join('')` reconstructs the string.

**Time Complexity:** O(n) – Each method traverses the entire data set.
**Space Complexity:** O(n) – Intermediate array allocation.

### 3.3 Modern ES6 One-Liner with Arrow Function

ES6 introduced arrow functions, enabling concise, single-expression function definitions.

```javascript
const reverseStringES6 = str => str.split('').reverse().join('');
```

**Characteristics:**
- Implicit return when using concise body syntax.
- Equivalent functionality to the built-in method approach.

### 3.4 Spread Operator Alternative

The spread operator (`...`) can be used to expand a string into an array of characters without calling `split()`.

```javascript
const reverseStringSpread = str => [...str].reverse().join('');
```

**Explanation:**
- `[...str]` creates a new array containing each character of `str`.
- The `reverse()` and `join('')` methods are applied as before.

**Note:** The spread operator is syntactically elegant but performs similarly to `split('')` for string-to-array conversion.

## 4. Comparative Analysis of Approaches

| Approach                      | Code Conciseness | Readability | Use Case                                      |
|-------------------------------|------------------|-------------|-----------------------------------------------|
| Manual Loop with Array        | Verbose          | Clear logic | Demonstrates fundamental algorithmic thinking |
| Built-in Methods              | Concise          | Very high   | Production code; well-known pattern           |
| ES6 Arrow Function            | Minimal          | High        | Modern JavaScript environments                |
| Spread Operator               | Minimal          | High        | ES6+ environments; stylistic preference       |

All approaches exhibit **O(n) time** and **O(n) space** complexity. The choice among them often depends on interview constraints, language familiarity, and personal coding style.

## 5. Key Interview Considerations

- **Input Validation:** Always consider edge cases (empty strings, non-string inputs) and discuss them with the interviewer.
- **String Immutability:** In JavaScript, strings are immutable; any operation that appears to modify a string actually creates a new one. This characteristic necessitates the use of arrays or concatenation.
- **Language-Specific Features:** Demonstrating knowledge of built-in methods (e.g., `split`, `reverse`, `join`) shows familiarity with the language's standard library. However, interviewers may request a manual implementation to assess algorithmic comprehension.
- **Communicating Trade-offs:** Discuss the time and space complexity of each solution and justify the chosen approach.

## 6. Summary

Reversing a string is a foundational exercise that reinforces the connection between strings and character arrays. Multiple implementation strategies exist, ranging from manual loops to concise built-in method chains. The core algorithm operates in linear time and linear space. Successful candidates demonstrate not only correct syntax but also an understanding of input validation, language behaviour, and algorithmic complexity.