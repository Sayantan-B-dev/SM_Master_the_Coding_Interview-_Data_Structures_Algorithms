# Practice Problems: Arrays

## 1. Introduction

This document provides a curated list of array-based algorithmic problems commonly encountered in technical interviews. These exercises are designed to reinforce fundamental array manipulation techniques, pattern recognition, and optimization strategies. While completion of these problems is optional, they serve as valuable practice for developing fluency in time and space complexity analysis.

**Note:** For guidance on approaching these problems using online platforms and accessing solutions in multiple programming languages, refer to the supplementary material titled "How To Use Leetcode" available in the bonus section of the course curriculum.

## 2. Recommended Problem Set

The following problems progress from foundational operations to more complex array transformations.

### 2.1 Two Sum

**Problem Statement:**  
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

**Constraints:**
- Each input has exactly one solution.
- The same element may not be used twice.
- Returned indices can be in any order.

**Key Concepts Evaluated:**
- Hash Table (Object) lookup for O(n) time complexity.
- Trade-off between brute-force nested loops O(n²) and space-time optimization.

### 2.2 Maximum Subarray

**Problem Statement:**  
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Key Concepts Evaluated:**
- Kadane's Algorithm for O(n) time complexity.
- Dynamic Programming fundamentals.
- Handling of negative numbers and edge cases.

### 2.3 Move Zeroes

**Problem Statement:**  
Given an array `nums`, write a function to move all `0`'s to the end of the array while maintaining the relative order of the non-zero elements.

**Constraints:**
- Operations must be performed in-place without creating a copy of the array.
- Minimize the total number of operations.

**Key Concepts Evaluated:**
- Two-pointer technique.
- In-place array modification.
- Order preservation logic.

### 2.4 Contains Duplicate

**Problem Statement:**  
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Key Concepts Evaluated:**
- Utilization of Hash Set or Hash Map for O(n) time complexity.
- Comparison of space-efficient sorting approach O(n log n) vs. time-efficient hashing approach.

### 2.5 Rotate Array

**Problem Statement:**  
Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example:**
- Input: `nums = [1,2,3,4,5,6,7]`, `k = 3`
- Output: `[5,6,7,1,2,3,4]`

**Key Concepts Evaluated:**
- Array reversal technique (O(1) extra space).
- Modulo arithmetic for handling `k` larger than array length.
- Avoidance of excessive auxiliary memory.

## 3. Bonus Challenge

### 3.1 Longest Word

**Problem Statement:**  
Given a string containing words separated by spaces or punctuation, return the longest word present in the string. If multiple words have the same maximum length, return the first occurrence.

**Approach Considerations:**
- **Array-Based Solution:** Split the string into an array of words using delimiters (spaces, punctuation) and iterate to track the longest element.
- **Regular Expression (Regex) Solution:** Utilize pattern matching (`/\w+/g`) to extract word tokens efficiently.

**Key Concepts Evaluated:**
- String manipulation and parsing.
- Regular expression proficiency.
- Handling edge cases (empty strings, special characters, multiple spaces).

## 4. Recommended Practice Workflow

To derive maximum benefit from these exercises, adhere to the following structured approach:

1.  **Understand the Problem:** Restate the problem in your own words. Clarify input types, edge cases, and expected output.
2.  **Brute-Force First:** Verbally or mentally outline the simplest, least efficient solution to ensure understanding of the core requirement.
3.  **Optimize:** Analyze the bottlenecks (e.g., nested loops) and identify the appropriate data structure (e.g., Hash Map, Two Pointers) to improve time or space complexity.
4.  **Code in Environment:** Write clean, commented code in your preferred language. Test against provided examples and custom edge cases.
5.  **Analyze Complexity:** Explicitly state the final time and space complexity using Big O notation.

## 5. Conclusion

Mastery of these array problems builds the foundational intuition required for more advanced data structures and algorithms. Consistent practice with this set will significantly enhance both problem-solving speed and the ability to articulate solutions under interview conditions.