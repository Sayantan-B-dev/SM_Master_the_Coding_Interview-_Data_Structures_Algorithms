# Amazon Technical Interview Questions: A Comprehensive Study Guide

## 1. Introduction

This document compiles authentic technical interview questions sourced from Amazon's recruitment process. The problems encompass core data structures and algorithms that form the foundation of software engineering evaluations at the organization. Mastery of these concepts is essential for candidates aspiring to secure positions at Amazon and similar technology-driven enterprises.

The compilation includes problems from past interview records, curated LeetCode selections, and a bonus problem illustrating dynamic programming principles. Each problem is presented with a direct hyperlink to its corresponding online judge platform for immediate practice.

## 2. Curated LeetCode Problem Set

The following problems are frequently cited in Amazon interview experiences. They assess proficiency in arrays, strings, linked lists, trees, and graph traversal.

| # | Title | Core Data Structure / Algorithm | Difficulty |
| :--- | :--- | :--- | :--- |
| [1](https://leetcode.com/problems/two-sum/) | Two Sum | Hash Map | Easy |
| [2](https://leetcode.com/problems/add-two-numbers/) | Add Two Numbers | Linked List, Math | Medium |
| [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters | Sliding Window, Hash Set | Medium |
| [200](https://leetcode.com/problems/number-of-islands/) | Number of Islands | Graph BFS/DFS, Union-Find | Medium |
| [20](https://leetcode.com/problems/valid-parentheses/) | Valid Parentheses | Stack | Easy |
| [5](https://leetcode.com/problems/longest-palindromic-substring/) | Longest Palindromic Substring | Dynamic Programming, Expand Around Center | Medium |
| [138](https://leetcode.com/problems/copy-list-with-random-pointer/) | Copy List with Random Pointer | Linked List, Hash Map | Medium |
| [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Best Time to Buy and Sell Stock | Array, Greedy | Easy |
| [21](https://leetcode.com/problems/merge-two-sorted-lists/) | Merge Two Sorted Lists | Linked List, Two-Pointer | Easy |

## 3. Bonus Problem: Staircase Climbing (Dynamic Programming)

### 3.1. Problem Statement

A staircase consists of `N` steps. An individual can ascend either **1 step** or **2 steps** at a time. The order of steps taken matters. The objective is to determine the total number of distinct ways to reach the top of the staircase.

**Example:** For `N = 4`, the following `5` unique sequences exist:

- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2

**Generalization:** Extend the solution to accommodate an arbitrary set of positive integers `X`, representing the allowed step sizes an individual may take.

### 3.2. Analysis and Recurrence Relation

The problem exhibits optimal substructure, rendering it amenable to dynamic programming.

**Base Cases:**
- `N = 0`: There is exactly **1** way to stand at the ground level (take no steps).
- `N < 0`: There are **0** ways, as negative step positions are invalid.

**Recurrence for Two Steps (1 and 2):**
To reach step `N`, the final move must have originated from either step `N-1` (by taking 1 step) or step `N-2` (by taking 2 steps). Therefore:

```
f(n) = f(n - 1) + f(n - 2)
```

This is precisely the Fibonacci sequence, with `f(0) = 1` and `f(1) = 1`.

**Recurrence for Arbitrary Step Set X:**
The principle extends naturally. The number of ways to reach step `n` is the sum of ways to reach step `n - x` for every valid step size `x` in `X` where `n - x ≥ 0`.

```
f(n) = Σ f(n - x)   for all x ∈ X such that n - x ≥ 0
f(0) = 1
f(negative) = 0
```

### 3.3. Naive Recursive Implementation

A direct translation of the recurrence into code yields an exponential time complexity **O(|X|^N)** due to overlapping subproblems being recomputed.

```javascript
/**
 * Naive recursive solution for the generalized staircase problem.
 * WARNING: Exhibits exponential time complexity and is unsuitable for large N.
 *
 * @param {number} n - The target step number to reach.
 * @param {number[]} X - Array of allowed step sizes.
 * @return {number} - Number of distinct ways to climb to step n.
 */
function staircaseRecursive(n, X) {
    // Base Case 1: Negative step count is impossible to reach.
    if (n < 0) {
        return 0;
    }
    // Base Case 2: Exactly one way to be at step 0 (do nothing).
    if (n === 0) {
        return 1;
    }

    // Recursive Case: Sum ways from all possible previous steps.
    // For each allowed step size x, compute ways from (n - x) and aggregate.
    let totalWays = 0;
    for (let x of X) {
        totalWays += staircaseRecursive(n - x, X);
    }
    return totalWays;
}
```

### 3.4. Optimized Solutions Using Dynamic Programming

#### 3.4.1. Bottom-Up Tabulation (Iterative DP)

This approach constructs a cache array `dp` where `dp[i]` stores the number of ways to reach step `i`. It eliminates redundant calculations, achieving **O(N * |X|)** time complexity and **O(N)** space complexity.

```javascript
/**
 * Optimized bottom-up dynamic programming solution for generalized staircase problem.
 *
 * @param {number} n - The target step number to reach.
 * @param {number[]} X - Array of allowed step sizes.
 * @return {number} - Number of distinct ways to climb to step n.
 */
function staircaseDP(n, X) {
    // Initialize a cache array of size n+1 with all zeros.
    // dp[i] will store the number of distinct ways to reach step i.
    const dp = new Array(n + 1).fill(0);

    // Base Condition: There is exactly one way to be at the ground step (step 0).
    // This serves as the foundation for building up solutions for positive steps.
    dp[0] = 1;

    // Iterate through each step from 1 up to the target step n.
    for (let currentStep = 1; currentStep <= n; currentStep++) {
        // For the current step, consider every possible step size in the allowed set X.
        for (let stepSize of X) {
            // Calculate the previous step index from which we could have arrived here.
            const previousStep = currentStep - stepSize;

            // If the previous step index is valid (non-negative), it means we could have
            // legally taken this step size from a prior step. Add the number of ways
            // to reach that previous step to the current step's total.
            if (previousStep >= 0) {
                dp[currentStep] += dp[previousStep];
            }
        }
    }

    // The answer for the target step n is stored at index n in the dp array.
    return dp[n];
}
```

#### 3.4.2. Space-Optimized Solution for Two-Step Case (Fibonacci)

When `X = {1, 2}`, the recurrence reduces to the Fibonacci sequence. We can achieve **O(1)** space complexity by maintaining only the last two computed values.

```javascript
/**
 * Space-optimized iterative solution for the two-step (Fibonacci) staircase problem.
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 *
 * @param {number} n - The target step number.
 * @return {number} - Number of distinct ways using steps of 1 or 2.
 */
function staircaseFibonacci(n) {
    // Base cases for n = 0 and n = 1.
    if (n <= 1) {
        return 1;
    }

    // Initialize variables representing f(0) and f(1).
    // 'twoStepsBefore' corresponds to f(i-2), initially f(0) = 1.
    let twoStepsBefore = 1;
    // 'oneStepBefore' corresponds to f(i-1), initially f(1) = 1.
    let oneStepBefore = 1;
    // 'current' will hold f(i).
    let current = 0;

    // Compute values from f(2) up to f(n).
    for (let i = 2; i <= n; i++) {
        // Recurrence: f(i) = f(i-1) + f(i-2)
        current = oneStepBefore + twoStepsBefore;

        // Shift the window forward for the next iteration.
        twoStepsBefore = oneStepBefore;
        oneStepBefore = current;
    }

    // After the loop, 'current' contains f(n).
    return current;
}
```

### 3.5. Complexity Analysis Summary

| Approach | Time Complexity | Space Complexity | Applicability |
| :--- | :--- | :--- | :--- |
| Naive Recursion | O(\|X\|^N) | O(N) call stack | Small N only |
| Bottom-Up DP | O(N * \|X\|) | O(N) | General X, any N |
| Space-Optimized (X={1,2}) | O(N) | O(1) | Two-step variant only |

### 3.6. Test Case Validation

Using the provided example `N = 4` with `X = {1, 2}`:

**Manual Trace of DP Array:**
- `dp[0] = 1`
- `dp[1] = dp[0] = 1`
- `dp[2] = dp[1] + dp[0] = 1 + 1 = 2`
- `dp[3] = dp[2] + dp[1] = 2 + 1 = 3`
- `dp[4] = dp[3] + dp[2] = 3 + 2 = 5`

The computed result `5` matches the expected output.

## 4. Conclusion

The problems presented in this document encapsulate the algorithmic rigor expected in Amazon's technical interviews. The staircase problem, in particular, illustrates the critical transition from a naive recursive formulation to an efficient dynamic programming solution—a paradigm highly valued in software engineering.

Consistent practice with these problems, coupled with a thorough understanding of their underlying principles, will significantly enhance a candidate's problem-solving acumen. Engagement with community platforms such as Discord study groups is recommended to foster collaborative learning and exposure to diverse solution strategies.