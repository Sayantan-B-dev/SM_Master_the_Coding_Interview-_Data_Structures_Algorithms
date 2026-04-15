# Practical Implementation Exercise: Replicating the Model Interview Solution

## Abstract

This document presents a guided practical exercise designed to reinforce the problem-solving framework observed in the Google model interview. The exercise involves implementing a classic interview problem—determining whether two arrays contain a common element—using both a naive, quadratic-time approach and an optimized, linear-time approach. The learner is encouraged to implement these solutions independently in a programming language of their choice, adhering to the structured, step-by-step methodology outlined in the "15-Step Problem Solving Guide." The objective is to develop procedural fluency and to internalize the transition from brute-force to optimal solution patterns.

---

## 1. Introduction

### 1.1 From Observation to Action

The preceding observational exercise provided a passive exposure to the behavioral and procedural norms of a high-caliber technical interview. The next stage in skill acquisition is **active practice**. Merely watching an expert solve a problem does not confer the ability to replicate the performance under pressure.

This exercise bridges the gap between observation and execution. The learner is tasked with implementing, from scratch, the very solution demonstrated in the Google interview video, following the same cognitive and communicative steps employed by the successful candidate.

### 1.2 The Problem Statement

The problem addressed in the model interview is a classic algorithmic question:

> **Given two arrays, write a function to determine if there exists at least one element that is present in both arrays (i.e., the arrays contain a common item).**

**Function Signature (JavaScript Example):**
```javascript
/**
 * Determines whether two arrays share at least one common element.
 * @param {Array} arr1 - The first input array.
 * @param {Array} arr2 - The second input array.
 * @returns {boolean} - true if a common element exists, false otherwise.
 */
function containsCommonItem(arr1, arr2) {
    // Implementation to be provided
}
```

**Examples:**
- `containsCommonItem(['a', 'b', 'c'], ['x', 'y', 'z'])` → `false`
- `containsCommonItem(['a', 'b', 'c'], ['x', 'y', 'a'])` → `true`

---

## 2. Guided Implementation Task

### 2.1 Phase 1: The Naive (Brute-Force) Solution

The initial approach, often termed the "naive" or "brute-force" solution, employs a nested loop structure to compare every element of the first array with every element of the second array.

#### 2.1.1 Algorithm Description

1.  Iterate over each element in `arr1` using an outer loop.
2.  For each element in `arr1`, iterate over each element in `arr2` using an inner loop.
3.  If a match is found, immediately return `true`.
4.  If the loops complete without finding a match, return `false`.

#### 2.1.2 Complexity Analysis

| Metric | Value | Justification |
| :--- | :--- | :--- |
| **Time Complexity** | **O(a * b)** | Where `a = arr1.length` and `b = arr2.length`. The outer loop runs `a` times; for each iteration, the inner loop runs `b` times. |
| **Space Complexity** | **O(1)** | No auxiliary data structures are created; only loop counters are used. |

#### 2.1.3 Reference Implementation (JavaScript)

```javascript
/**
 * Naive approach using nested loops.
 * Time Complexity: O(a * b)
 * Space Complexity: O(1)
 */
function containsCommonItemNaive(arr1, arr2) {
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) {
                return true;
            }
        }
    }
    return false;
}
```

### 2.2 Phase 2: The Optimized Solution

The optimized solution improves upon the time complexity by trading space for time. It leverages a **hash set** (or equivalent data structure in the chosen language) to store the elements of the first array, enabling O(1) average-time lookups.

#### 2.2.1 Algorithm Description

1.  Create an empty hash set (or object/map) to serve as a lookup table.
2.  Iterate over `arr1`, adding each element to the set.
3.  Iterate over `arr2`. For each element, check if it exists in the set.
4.  If a match is found, return `true`.
5.  If the loop completes, return `false`.

#### 2.2.2 Complexity Analysis

| Metric | Value | Justification |
| :--- | :--- | :--- |
| **Time Complexity** | **O(a + b)** | Iterating over `arr1` takes `a` steps. Iterating over `arr2` takes `b` steps. Each lookup in the set is O(1) on average. |
| **Space Complexity** | **O(a)** | In the worst case, all elements of `arr1` are stored in the hash set. |

#### 2.2.3 Reference Implementation (JavaScript)

```javascript
/**
 * Optimized approach using a Set for O(1) lookups.
 * Time Complexity: O(a + b)
 * Space Complexity: O(a)
 */
function containsCommonItemOptimized(arr1, arr2) {
    // Step 1: Populate a Set with elements from the first array
    const lookupSet = new Set(arr1);

    // Step 2: Check if any element from the second array exists in the Set
    for (let i = 0; i < arr2.length; i++) {
        if (lookupSet.has(arr2[i])) {
            return true;
        }
    }
    return false;
}
```

**Note on Language-Specific Implementation:** The `Set` object in JavaScript provides an efficient built-in hash-based collection. In other languages, analogous structures include:
- **Python:** `set()`
- **Java:** `HashSet<T>`
- **C++:** `std::unordered_set<T>`

---

## 3. Exercise Instructions and Learning Objectives

### 3.1 Recommended Workflow

To maximize the pedagogical value of this exercise, the learner is advised to adhere strictly to the following workflow, mirroring the structure of a real technical interview.

1.  **Environment Setup:** Open a code editor, online IDE (e.g., Replit), or a simple text file. **Do not refer to the reference implementations provided above.**
2.  **Step-by-Step Adherence:** Using the "15-Step Problem Solving Guide" as a checklist, work through the problem.
    - **Step 1-3:** Clarify the problem statement, input types, and edge cases (e.g., empty arrays, duplicate elements).
    - **Step 4-6:** Propose the naive approach verbally (or in written comments). Explain its time complexity (O(a * b)).
    - **Step 7-8:** Write the code for the naive solution. Test it manually with a few small inputs.
    - **Step 9-11:** Identify the bottleneck (nested loops) and suggest an optimization using a hash set. Explain the space-time trade-off.
    - **Step 12-14:** Write the code for the optimized solution. Test with the same inputs and additional edge cases.
    - **Step 15:** Conclude with a final complexity summary.
3.  **Language-Agnostic Implementation:** Write the solution in the programming language of your choice. Focus on translating the *algorithmic logic* rather than memorizing JavaScript syntax.
4.  **Self-Correction:** Only after completing your own implementation should you compare it against the reference code provided in this document or in the course materials.

### 3.2 Learning Outcomes

Upon successful completion of this exercise, the learner will have:

- Demonstrated the ability to **transition** from a brute-force solution to an optimized solution.
- Internalized the **process** of analyzing time and space complexity trade-offs.
- Practiced the **communication** pattern of explaining a solution before coding it.
- Developed muscle memory for using a **hash-based data structure** to achieve linear time complexity.

---

## 4. Conclusion

This practical exercise serves as a critical bridge between theoretical understanding and applied performance. By actively implementing both the naive and optimized solutions to the "common element" problem while following a structured interview workflow, the learner reinforces the behavioral patterns that distinguish successful candidates.

The provided reference implementations are intended for post-exercise comparison and validation, not as a crutch during the practice session. Mastery of this problem and its associated process will serve as a template for tackling a wide array of algorithmic challenges that follow a similar optimization pattern: **recognizing a quadratic time bottleneck and resolving it through the strategic application of auxiliary space.**

The skills practiced here—methodical problem decomposition, complexity analysis, and clear articulation of trade-offs—are universally applicable and will be exercised repeatedly throughout the remainder of the course.