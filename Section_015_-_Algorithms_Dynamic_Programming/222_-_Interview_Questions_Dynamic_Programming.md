# Dynamic Programming: Classic Interview Problems

## 1. Introduction

Dynamic Programming (DP) is a powerful optimization technique applied to problems exhibiting **optimal substructure** and **overlapping subproblems**. This document examines three classic LeetCode problems that frequently appear in technical interviews: **House Robber**, **Best Time to Buy and Sell Stock**, and **Climbing Stairs**. Each problem is analyzed through the lens of dynamic programming, highlighting the recurrence relations, implementation strategies, and the unifying patterns that characterize DP solutions.

## 2. Problem 1: House Robber

### 2.1 Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. However, adjacent houses have security systems connected, and if two adjacent houses are broken into on the same night, the police will be alerted.

Given an integer array `nums` representing the amount of money in each house, return the **maximum** amount of money you can rob tonight **without alerting the police**.

**Constraints:**
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

**Example:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), then house 3 (money = 9), and then house 5 (money = 1).
Total = 2 + 9 + 1 = 12.
```

### 2.2 Dynamic Programming Approach

The problem exhibits **optimal substructure** and **overlapping subproblems**. At each house `i`, the robber faces a binary choice:
- **Rob house `i`**: Then the robber cannot rob house `i-1` but can add the loot from `i` to the maximum loot from houses up to `i-2`.
- **Skip house `i`**: The robber retains the maximum loot from houses up to `i-1`.

This leads to the recurrence relation:

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

Where:
- `dp[i]` = maximum amount of money that can be robbed from the first `i` houses (0-indexed).
- Base cases:
  - `dp[0] = nums[0]`
  - `dp[1] = max(nums[0], nums[1])`

### 2.3 Implementation in JavaScript

```javascript
/**
 * House Robber - Bottom-Up Dynamic Programming (Tabulation)
 * Time Complexity: O(n) - Single pass through the array.
 * Space Complexity: O(n) - DP array of size n.
 *
 * @param {number[]} nums - Array of non-negative integers representing money in each house.
 * @return {number} - Maximum amount of money that can be robbed without alerting police.
 */
function rob(nums) {
    const n = nums.length;

    // Edge cases: empty array or single house.
    if (n === 0) return 0;
    if (n === 1) return nums[0];

    // Initialize DP array. dp[i] represents the max loot considering houses 0..i.
    const dp = new Array(n);

    // Base Cases:
    // For the first house, the only option is to rob it.
    dp[0] = nums[0];
    // For the second house, choose the maximum between robbing first or second.
    dp[1] = Math.max(nums[0], nums[1]);

    // Fill the DP table iteratively.
    // For each house i, decide whether to rob it (nums[i] + dp[i-2]) or skip it (dp[i-1]).
    for (let i = 2; i < n; i++) {
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
    }

    // The last element contains the answer for the entire street.
    return dp[n - 1];
}

// Example usage:
console.log(rob([2,7,9,3,1])); // Output: 12
```

### 2.4 Space-Optimized Implementation

Since each state depends only on the two previous states, the space complexity can be reduced to **O(1)**.

```javascript
/**
 * House Robber - Space Optimized (O(1) Space)
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 *
 * @param {number[]} nums
 * @return {number}
 */
function robOptimized(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    if (n === 1) return nums[0];

    // prev2 = dp[i-2], prev1 = dp[i-1]
    let prev2 = nums[0];
    let prev1 = Math.max(nums[0], nums[1]);

    for (let i = 2; i < n; i++) {
        const current = Math.max(prev1, prev2 + nums[i]);
        // Shift the window for the next iteration.
        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
}

console.log(robOptimized([2,7,9,3,1])); // Output: 12
```

### 2.5 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| Tabulation (Array) | O(n) | O(n) |
| Space Optimized | O(n) | O(1) |

### 2.6 Visual Representation

The decision process can be visualized as a state machine:

```
State: Max loot up to house i
Choice:
    - Rob i   → dp[i] = nums[i] + dp[i-2]
    - Skip i  → dp[i] = dp[i-1]
```

## 3. Problem 2: Best Time to Buy and Sell Stock

### 3.1 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the **maximum profit** you can achieve from this transaction. If no profit can be achieved, return `0`.

**Constraints:**
- `1 <= prices.length <= 10⁵`
- `0 <= prices[i] <= 10⁴`

**Example:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
```

### 3.2 Dynamic Programming Approach

This problem can be framed as finding the maximum difference `prices[j] - prices[i]` where `j > i`. A DP approach tracks the **minimum price seen so far** and computes the **maximum profit** achievable by selling on the current day.

Recurrence intuition:
- Let `minPrice` be the minimum price encountered up to day `i`.
- The profit if selling on day `i` is `prices[i] - minPrice`.
- The maximum profit overall is the maximum of these daily potential profits.

### 3.3 Implementation in JavaScript

```javascript
/**
 * Best Time to Buy and Sell Stock - Single Pass DP
 * Time Complexity: O(n) - Single iteration through the prices array.
 * Space Complexity: O(1) - Only two variables maintained.
 *
 * @param {number[]} prices - Array of stock prices in chronological order.
 * @return {number} - Maximum profit achievable; 0 if no profit possible.
 */
function maxProfit(prices) {
    // Initialize the minimum price to a very large value.
    // This ensures the first price will update it.
    let minPrice = Infinity;

    // Initialize maximum profit to 0 (no transaction if profit negative).
    let maxProfit = 0;

    // Iterate through each day's price.
    for (let price of prices) {
        // Step 1: Update the minimum price seen so far.
        // This represents the best day to buy up to the current day.
        if (price < minPrice) {
            minPrice = price;
        }

        // Step 2: Calculate the potential profit if selling at current price.
        const potentialProfit = price - minPrice;

        // Step 3: Update the maximum profit if this potential profit is larger.
        if (potentialProfit > maxProfit) {
            maxProfit = potentialProfit;
        }
    }

    return maxProfit;
}

// Example usage:
console.log(maxProfit([7,1,5,3,6,4])); // Output: 5
console.log(maxProfit([7,6,4,3,1]));   // Output: 0 (no profit possible)
```

### 3.4 Explanation of the DP State

Although the problem does not require a full DP table, it embodies the DP principle of **optimal substructure**:
- The optimal solution for the entire array depends on the optimal subproblem: the minimum price up to day `i`.
- The state `minPrice` is updated iteratively, and `maxProfit` accumulates the best result.

### 3.5 Complexity Analysis

| Metric | Value |
| :--- | :--- |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

### 3.6 Visual Representation

```
Day:       0   1   2   3   4   5
Price:     7   1   5   3   6   4
minPrice:  7   1   1   1   1   1
Profit:    0   0   4   2   5   3
MaxProfit: 0   0   4   4   5   5
```

## 4. Problem 3: Climbing Stairs

### 4.1 Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb **1** or **2** steps. In how many distinct ways can you climb to the top?

**Constraints:**
- `1 <= n <= 45`

**Example:**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### 4.2 Dynamic Programming Approach

This problem is a classic DP problem isomorphic to the **Fibonacci sequence**. To reach step `n`, the climber must have arrived from step `n-1` (taking 1 step) or from step `n-2` (taking 2 steps). Therefore, the number of ways to reach step `n` is the sum of the ways to reach the two preceding steps.

Recurrence relation:
```
ways(n) = ways(n-1) + ways(n-2)
```
Base cases:
- `ways(1) = 1`
- `ways(2) = 2`

### 4.3 Implementation in JavaScript

```javascript
/**
 * Climbing Stairs - Bottom-Up Dynamic Programming (Tabulation)
 * Time Complexity: O(n) - Single loop up to n.
 * Space Complexity: O(n) - DP array of size n+1.
 *
 * @param {number} n - Total number of steps to reach the top.
 * @return {number} - Number of distinct ways to climb to the top.
 */
function climbStairs(n) {
    // Handle base cases directly.
    if (n === 1) return 1;
    if (n === 2) return 2;

    // Create a DP array where dp[i] represents the number of ways to reach step i.
    // Index 0 is unused to maintain alignment with step numbers.
    const dp = new Array(n + 1);

    // Base cases:
    dp[1] = 1; // Only one way: one step.
    dp[2] = 2; // Two ways: (1+1) or (2).

    // Fill the table from step 3 up to n.
    for (let i = 3; i <= n; i++) {
        // Number of ways to reach step i is sum of ways to reach i-1 and i-2.
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

// Example usage:
console.log(climbStairs(3)); // Output: 3
console.log(climbStairs(5)); // Output: 8
```

### 4.4 Space-Optimized Implementation

Similar to Fibonacci, only the last two values are needed.

```javascript
/**
 * Climbing Stairs - Space Optimized (O(1) Space)
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 *
 * @param {number} n
 * @return {number}
 */
function climbStairsOptimized(n) {
    if (n === 1) return 1;
    if (n === 2) return 2;

    let prev2 = 1; // ways for (i-2)
    let prev1 = 2; // ways for (i-1)

    for (let i = 3; i <= n; i++) {
        const current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
}

console.log(climbStairsOptimized(5)); // Output: 8
```

### 4.5 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| Tabulation | O(n) | O(n) |
| Space Optimized | O(n) | O(1) |

## 5. Identifying the Common Pattern

The three problems discussed share a unifying DP pattern despite their different problem statements:

| Problem | Recurrence Relation | DP State |
| :--- | :--- | :--- |
| **House Robber** | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` | Max loot up to house `i` |
| **Best Time to Buy and Sell Stock** | `maxProfit = max(maxProfit, price - minPrice)` | Min price seen, max profit |
| **Climbing Stairs** | `dp[i] = dp[i-1] + dp[i-2]` | Ways to reach step `i` |

### 5.1 The DP Pattern Recognition Checklist

When approaching a new problem, ask the following questions to determine if DP is applicable:

1. **Optimal Substructure**: Can the problem be broken into smaller, similar subproblems whose solutions combine to yield the global optimum?
2. **Overlapping Subproblems**: Are the same subproblems solved multiple times in a naive recursive solution?
3. **State Definition**: Can a state be defined that captures all necessary information from previous decisions?
4. **Recurrence Relation**: Is there a mathematical relationship linking the state at index `i` to earlier states?

If the answers are affirmative, dynamic programming (top-down memoization or bottom-up tabulation) can dramatically improve efficiency.

### 5.2 Mermaid Diagram: General DP Workflow

```mermaid
graph TD
    A[Start] --> B{Identify Subproblems};
    B --> C[Define State dp[i]];
    C --> D[Establish Recurrence Relation];
    D --> E[Determine Base Cases];
    E --> F{Choose DP Approach};
    F --> G[Memoization - Top-Down];
    F --> H[Tabulation - Bottom-Up];
    G --> I[Implement with Cache];
    H --> I;
    I --> J[Analyze Time & Space Complexity];
    J --> K[Optimize Space if Possible];
```

## 6. Conclusion

Dynamic programming is a versatile technique for solving optimization and counting problems with overlapping subproblems. The three classic interview problems—**House Robber**, **Best Time to Buy and Sell Stock**, and **Climbing Stairs**—demonstrate the core principles of DP:

- **State definition** captures the essence of the subproblem.
- **Recurrence relation** mathematically expresses the optimal choice.
- **Iterative or recursive with caching** ensures linear time complexity.

Mastery of these patterns equips engineers to tackle a wide array of algorithmic challenges efficiently. Practice with these and similar problems solidifies the ability to recognize and apply dynamic programming in technical interviews and real-world software development.

> **Reference Links:**
> - House Robber: https://leetcode.com/problems/house-robber
> - Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
> - Climbing Stairs: https://leetcode.com/problems/climbing-stairs