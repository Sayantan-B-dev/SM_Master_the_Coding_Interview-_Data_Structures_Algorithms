# Google Technical Interview Questions: A Comprehensive Study Guide

## 1. Introduction

This document presents a curated collection of technical interview questions sourced from Google's engineering recruitment process. The problems emphasize algorithmic depth, data structure proficiency, and the ability to reason about edge cases and optimizations. Mastery of these concepts is essential for candidates seeking software engineering roles at Google and other premier technology organizations.

The compilation includes a set of LeetCode problems frequently referenced in Google interview experiences, followed by an in-depth analysis of a bonus problem focusing on string manipulation and immutability considerations.

## 2. Curated LeetCode Problem Set

The following problems represent core algorithmic challenges encountered in Google technical screenings and on-site interviews. Each entry includes a direct hyperlink to the LeetCode platform for immediate practice.

| # | Title | Core Data Structure / Algorithm | Difficulty |
| :--- | :--- | :--- | :--- |
| [155](https://leetcode.com/problems/min-stack/) | Min Stack | Stack, Auxiliary Data Structure | Easy |
| [200](https://leetcode.com/problems/number-of-islands/) | Number of Islands | Graph BFS/DFS, Union-Find | Medium |
| [20](https://leetcode.com/problems/valid-parentheses/) | Valid Parentheses | Stack | Easy |
| [42](https://leetcode.com/problems/trapping-rain-water/) | Trapping Rain Water | Two-Pointer, Dynamic Programming | Hard |
| [56](https://leetcode.com/problems/merge-intervals/) | Merge Intervals | Sorting, Array Traversal | Medium |
| [681](https://leetcode.com/problems/next-closest-time/) | Next Closest Time | String, Enumeration, Simulation | Medium |
| [139](https://leetcode.com/problems/word-break/) | Word Break | Dynamic Programming, Trie | Medium |
| [31](https://leetcode.com/problems/next-permutation/) | Next Permutation | Array, Two-Pointer | Medium |

### 2.1. Detailed Solution: Min Stack (#155)

**Problem Synopsis:** Design a stack that supports push, pop, top, and retrieving the minimum element in constant time O(1).

**Approach:** Maintain two stacks internally. The primary stack stores all elements. An auxiliary `minStack` stores the minimum value seen so far at each level of the stack. When pushing, if the new value is less than or equal to the current minimum, push it onto `minStack`. When popping, if the popped value equals the top of `minStack`, pop from `minStack` as well.

**Time Complexity:** O(1) for all operations  
**Space Complexity:** O(n) worst case

```javascript
/**
 * #155 Min Stack
 * Implements a stack with O(1) retrieval of the minimum element.
 */
class MinStack {
    constructor() {
        // Primary stack to store all pushed values.
        this.stack = [];
        // Auxiliary stack to keep track of the minimum value at each level.
        // The top of minStack always holds the current minimum of the entire stack.
        this.minStack = [];
    }

    /**
     * Pushes an element onto the stack.
     * @param {number} val - The value to push.
     */
    push(val) {
        // Always push the value onto the primary stack.
        this.stack.push(val);

        // Determine the new minimum after this push.
        // If minStack is empty, this value becomes the new minimum.
        // Otherwise, compare val with the current minimum (top of minStack).
        if (this.minStack.length === 0) {
            this.minStack.push(val);
        } else {
            const currentMin = this.minStack[this.minStack.length - 1];
            // Push the smaller of the new value and the current minimum.
            // This ensures minStack maintains a non-increasing sequence of minima.
            this.minStack.push(Math.min(val, currentMin));
        }
    }

    /**
     * Removes the top element from the stack.
     */
    pop() {
        // Remove from both stacks to maintain synchronization.
        this.stack.pop();
        this.minStack.pop();
    }

    /**
     * Returns the top element of the stack without removing it.
     * @return {number} The top element.
     */
    top() {
        return this.stack[this.stack.length - 1];
    }

    /**
     * Returns the minimum element currently in the stack in O(1) time.
     * @return {number} The minimum element.
     */
    getMin() {
        // The top of minStack holds the current global minimum.
        return this.minStack[this.minStack.length - 1];
    }
}
```

### 2.2. Detailed Solution: Trapping Rain Water (#42)

**Problem Synopsis:** Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water can be trapped after raining.

**Approach:** Use the two-pointer technique. Initialize `left` at index `0` and `right` at index `n-1`. Maintain `leftMax` and `rightMax` representing the maximum height encountered from the left and right sides respectively. At each step, process the pointer with the smaller maximum height, calculating trapped water as the difference between that maximum and the current height.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```javascript
/**
 * #42 Trapping Rain Water
 * Calculates the total units of water trapped between bars.
 *
 * @param {number[]} height - Array of non-negative integers representing bar heights.
 * @return {number} - Total units of trapped water.
 */
function trap(height) {
    // Edge case: Need at least three bars to trap any water.
    if (height.length < 3) return 0;

    let left = 0;
    let right = height.length - 1;
    let leftMax = 0;
    let rightMax = 0;
    let totalWater = 0;

    // The two-pointer technique converges from both ends.
    // Water trapped at any index i depends on min(leftMax, rightMax) - height[i].
    while (left < right) {
        // Process the side with the smaller current maximum.
        // This ensures that the water level on that side is bounded by the known maximum.
        if (height[left] < height[right]) {
            // Update leftMax if the current height is taller.
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                // Current bar is lower than leftMax, so it can trap water.
                // The water trapped is the difference between leftMax and current height.
                totalWater += leftMax - height[left];
            }
            left++;
        } else {
            // Update rightMax if the current height is taller.
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                // Current bar is lower than rightMax, so it can trap water.
                totalWater += rightMax - height[right];
            }
            right--;
        }
    }

    return totalWater;
}
```

### 2.3. Detailed Solution: Next Permutation (#31)

**Problem Synopsis:** Given an array of integers `nums`, rearrange the numbers into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, rearrange it as the lowest possible order (sorted in ascending order). The replacement must be in-place and use only constant extra memory.

**Approach:** The algorithm follows three steps:
1. Find the first decreasing element from the right (pivot).
2. Find the smallest element to the right of the pivot that is greater than the pivot, and swap them.
3. Reverse the subarray to the right of the pivot to get the next smallest lexicographical order.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```javascript
/**
 * #31 Next Permutation
 * Transforms the array into its next lexicographical permutation in-place.
 *
 * @param {number[]} nums - The array of numbers to be permuted.
 * @return {void} Do not return anything, modify nums in-place.
 */
function nextPermutation(nums) {
    // Step 1: Find the first decreasing element when scanning from right to left.
    // This element is the "pivot" that needs to be increased.
    let pivotIndex = -1;
    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] < nums[i + 1]) {
            pivotIndex = i;
            break;
        }
    }

    // If no pivot is found, the array is in descending order (largest permutation).
    // Reverse the entire array to get the smallest permutation.
    if (pivotIndex === -1) {
        reverse(nums, 0, nums.length - 1);
        return;
    }

    // Step 2: Find the smallest element to the right of the pivot that is greater than the pivot.
    // Since the right portion is descending, we scan from right to find the first greater element.
    let swapIndex = -1;
    for (let i = nums.length - 1; i > pivotIndex; i--) {
        if (nums[i] > nums[pivotIndex]) {
            swapIndex = i;
            break;
        }
    }

    // Swap the pivot with the found element.
    [nums[pivotIndex], nums[swapIndex]] = [nums[swapIndex], nums[pivotIndex]];

    // Step 3: Reverse the subarray to the right of the pivot.
    // This portion was originally descending; reversing makes it ascending (smallest order).
    reverse(nums, pivotIndex + 1, nums.length - 1);
}

/**
 * Helper function to reverse a portion of an array in-place.
 * @param {number[]} arr - The array to modify.
 * @param {number} start - Starting index (inclusive).
 * @param {number} end - Ending index (inclusive).
 */
function reverse(arr, start, end) {
    while (start < end) {
        [arr[start], arr[end]] = [arr[end], arr[start]];
        start++;
        end--;
    }
}
```

### 2.4. Detailed Solution: Word Break (#139)

**Problem Synopsis:** Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Approach:** Use dynamic programming. Let `dp[i]` be a boolean indicating whether the prefix of length `i` can be segmented. `dp[0] = true` (empty string). For each position `i`, check all `j < i`; if `dp[j]` is true and the substring `s[j...i-1]` is in the dictionary, then `dp[i]` becomes true.

**Time Complexity:** O(n^2) where n is string length  
**Space Complexity:** O(n)

```javascript
/**
 * #139 Word Break
 * Determines if a string can be segmented into dictionary words.
 *
 * @param {string} s - The input string.
 * @param {string[]} wordDict - Array of dictionary words.
 * @return {boolean} - True if segmentation is possible, false otherwise.
 */
function wordBreak(s, wordDict) {
    // Convert wordDict array to a Set for O(1) average-time lookups.
    const wordSet = new Set(wordDict);

    // dp[i] represents whether the prefix s[0...i-1] can be segmented.
    const dp = new Array(s.length + 1).fill(false);
    // Base case: empty string can always be formed.
    dp[0] = true;

    // Iterate through each ending position i (1-indexed for dp convenience).
    for (let i = 1; i <= s.length; i++) {
        // For each ending position, try all possible starting positions j.
        for (let j = 0; j < i; j++) {
            // If the prefix up to j is segmentable AND the substring from j to i
            // exists in the dictionary, then the prefix up to i is segmentable.
            const substring = s.substring(j, i);
            if (dp[j] && wordSet.has(substring)) {
                dp[i] = true;
                // Once we find a valid segmentation, no need to check other j values.
                break;
            }
        }
    }

    // The final answer is whether the entire string (prefix of length n) is segmentable.
    return dp[s.length];
}
```

## 3. Bonus Problem: Remove Given Character from String

### 3.1. Problem Statement

Write a function that removes all occurrences of a specified character from a given input string. The function should return the modified string without the target character.

### 3.2. Considerations and Constraints

| Aspect | Consideration |
| :--- | :--- |
| **String Immutability** | In JavaScript, strings are immutable. Any modification operation creates a new string. |
| **Character Type** | The character to remove could be any valid Unicode character. |
| **Case Sensitivity** | Removal is case-sensitive unless otherwise specified. |
| **Performance** | For large strings, minimizing intermediate string allocations is desirable. |

### 3.3. Solution Approaches

#### Approach 1: Using String Replacement with Regular Expression

This method uses the built-in `replace()` method with a global regular expression to match all occurrences of the target character.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```javascript
/**
 * Removes all occurrences of a specified character from a string using regex.
 *
 * @param {string} str - The original string.
 * @param {string} charToRemove - The single character to remove.
 * @return {string} - The modified string with the character removed.
 */
function removeCharRegex(str, charToRemove) {
    // Edge case: If the character is empty or longer than one character,
    // behavior may be undefined. We assume a single character.
    if (charToRemove.length !== 1) {
        throw new Error('charToRemove must be a single character');
    }

    // Create a RegExp object with the 'g' (global) flag to replace all occurrences.
    // We need to escape the character in case it's a regex special character (e.g., '.', '*', '?').
    // For simplicity, we assume standard alphanumeric; a production version would use proper escaping.
    const regex = new RegExp(charToRemove, 'g');
    return str.replace(regex, '');
}
```

#### Approach 2: Manual Iteration and Filtering

This method iterates through each character of the string and builds a new string by concatenating only characters that are not the target.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```javascript
/**
 * Removes all occurrences of a specified character from a string by manual iteration.
 *
 * @param {string} str - The original string.
 * @param {string} charToRemove - The single character to remove.
 * @return {string} - The modified string with the character removed.
 */
function removeCharIterative(str, charToRemove) {
    // Use an array to collect characters that should be kept.
    // This avoids repeated string concatenation which is inefficient due to immutability.
    const resultChars = [];

    // Iterate through each character of the input string.
    for (let i = 0; i < str.length; i++) {
        const currentChar = str[i];
        // If the current character is not the one to remove, add it to the result array.
        if (currentChar !== charToRemove) {
            resultChars.push(currentChar);
        }
    }

    // Join the array of characters into a single string.
    return resultChars.join('');
}
```

#### Approach 3: Using Array Methods (Functional Style)

Leverage JavaScript's array transformation methods: split the string into an array of characters, filter out the target character, and join back.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```javascript
/**
 * Removes all occurrences of a specified character from a string using array methods.
 *
 * @param {string} str - The original string.
 * @param {string} charToRemove - The single character to remove.
 * @return {string} - The modified string with the character removed.
 */
function removeCharFunctional(str, charToRemove) {
    // Step 1: Convert string to array of individual characters.
    // Step 2: Filter out characters that equal the target character.
    // Step 3: Join the remaining characters back into a string.
    return str.split('')
              .filter(char => char !== charToRemove)
              .join('');
}
```

### 3.4. Comparative Analysis

| Method | Pros | Cons |
| :--- | :--- | :--- |
| **Regex Replace** | Concise, single-line, optimized internally. | Requires escaping special regex characters; may be less readable. |
| **Manual Iteration** | Explicit control, no hidden regex behavior. | Slightly more verbose. |
| **Array Functional** | Expressive, modern JavaScript style. | Creates intermediate array, slightly more memory overhead. |

### 3.5. Test Cases

```javascript
// Example test cases for validation.
console.log(removeCharIterative('hello world', 'l'));     // Output: 'heo word'
console.log(removeCharIterative('Google', 'o'));          // Output: 'Ggle'
console.log(removeCharIterative('Mississippi', 's'));     // Output: 'Miiippi'
console.log(removeCharIterative('abcdef', 'z'));          // Output: 'abcdef' (no change)
console.log(removeCharIterative('aaaaa', 'a'));           // Output: '' (empty string)
```

### 3.6. Handling Edge Cases

**Empty String Input:**
The function should gracefully return an empty string if the input string is empty.

**Target Character Not Present:**
The function should return the original string unchanged.

**Multi-character Target String:**
The problem statement specifies a "given character." The function may either restrict input to a single character or extend to remove any substring (not required).

**Unicode and Emoji Characters:**
JavaScript strings are UTF-16 encoded. Characters outside the Basic Multilingual Plane (e.g., emojis) are represented as surrogate pairs. The manual iteration methods above treat each 16-bit code unit individually, which may break surrogate pairs. For full Unicode support, use `Array.from(str)` or the spread operator `[...str]` to correctly split by code points.

```javascript
/**
 * Unicode-safe version using spread operator to split by code points.
 */
function removeCharUnicodeSafe(str, charToRemove) {
    // The spread operator correctly splits the string into an array of Unicode code points.
    return [...str]
        .filter(char => char !== charToRemove)
        .join('');
}
```

## 4. Conclusion

The Google interview question set emphasizes both algorithmic rigor and the ability to write clean, efficient code under constraints. The problems curated here span a range of difficulties and core computer science topics, including stack design, graph traversal, dynamic programming, and string manipulation.

The bonus character removal problem, while seemingly trivial, tests a candidate's understanding of language-specific string handling nuances, performance considerations, and edge case awareness. Mastery of these fundamentals, combined with consistent practice on the linked LeetCode problems, will substantially enhance a candidate's preparedness for technical evaluations at Google and comparable technology firms.