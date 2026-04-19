# Strings as Character Arrays: Interview Strategy

## 1. Introduction

In technical interviews, questions involving string manipulation are frequently encountered. An effective strategic approach is to conceptualise strings as **arrays of characters**. This mental model allows candidates to leverage array operations and algorithms to solve string-based problems efficiently.

## 2. Conceptual Foundation

### 2.1 String Representation

At a fundamental level, a string is a sequence of characters stored contiguously in memory. This representation closely parallels that of an array, where each element occupies an indexed position.

```
String: "hello"
Index:   0     1     2     3     4
Chars:  'h'   'e'   'l'   'l'   'o'
```

### 2.2 Implications for Problem-Solving

Because strings exhibit array-like properties (indexed access, sequential ordering), many string manipulation tasks can be reduced to array operations. This approach often simplifies the problem and allows the reuse of well-known array algorithms.

## 3. Recommended Interview Strategy

When presented with a string manipulation question, the following workflow is recommended:

1. **Convert the string to an array of characters.**
   - In JavaScript, this is achieved using the `.split('')` method.
2. **Perform the required operations using array methods or loops.**
   - Examples include reversing, filtering, mapping, or using two-pointer techniques.
3. **Convert the modified array back to a string.**
   - In JavaScript, use the `.join('')` method.

### 3.1 Example: Reversing a String

**Problem Statement:** Reverse a given string.

**Solution Using Array Conversion:**

```javascript
function reverseString(str) {
    // Step 1: Convert string to character array
    const charArray = str.split('');
    
    // Step 2: Reverse the array (using built-in or custom logic)
    const reversedArray = charArray.reverse();
    
    // Step 3: Join array back into a string
    return reversedArray.join('');
}

console.log(reverseString("hello")); // Output: "olleh"
```

**Alternative Manual Reversal (without built-in reverse):**

```javascript
function reverseStringManual(str) {
    const charArray = str.split('');
    let left = 0;
    let right = charArray.length - 1;
    
    // Two-pointer approach to swap characters
    while (left < right) {
        // Swap elements
        [charArray[left], charArray[right]] = [charArray[right], charArray[left]];
        left++;
        right--;
    }
    
    return charArray.join('');
}

console.log(reverseStringManual("hello")); // Output: "olleh"
```

## 4. Common String Manipulation Questions as Array Problems

| String Question              | Array Equivalent Operation                         |
|------------------------------|----------------------------------------------------|
| Reverse a string             | Reverse an array                                   |
| Check for palindrome         | Compare array elements from both ends              |
| Count vowels/consonants      | Iterate and filter array elements                  |
| Remove duplicate characters  | Use Set on array or filter with index checking     |
| Find first non-repeating char| Build frequency map using array/object             |
| Anagram check                | Sort both character arrays and compare             |

## 5. Language-Specific Considerations

### 5.1 JavaScript Methods

- **String to Array:** `str.split('')` or `[...str]` (spread operator)
- **Array to String:** `arr.join('')`

### 5.2 Immutability of Strings

In many languages, strings are immutable. Attempting to modify a character directly (e.g., `str[0] = 'H'`) is either disallowed or has no effect. Converting to an array overcomes this limitation because array elements are mutable.

## 6. Summary

- Strings are essentially character arrays; treating them as such simplifies many algorithmic problems.
- A common interview pattern is: **Convert → Process → Reconstruct**.
- This strategy enables the application of efficient array algorithms (e.g., two-pointer, in-place swaps) to string problems.
- Mastery of string-array conversion methods in one's language of choice is essential for swift implementation during interviews.