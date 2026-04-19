## How to Approach Big O Calculation

1. **Identify the input size** – Typically denoted as `n`. Look for arrays, strings, or any data structure that grows.

2. **Look for loops**:
   - A single loop iterating over `n` elements → **O(n)**
   - Nested loops iterating over the same `n` → **O(n²)**
   - A loop that divides the input in half each time (binary search style) → **O(log n)**

3. **Analyze operations in sequence** – Add complexities: O(n) + O(n) = O(2n) → simplify to **O(n)**
   (Drop constants)

4. **Nested operations** – Multiply complexities: O(n) * O(n) = **O(n²)**

5. **Check for recursion** – Draw the recursion tree. Each level may have branching factors.

6. **Ignore non-dominant terms** – O(n² + n) simplifies to **O(n²)**

7. **Consider space complexity** – Are you creating new arrays, objects, or recursion stacks? Each allocation may add O(n) space.

### Common Mistakes to Avoid

- Assuming all loops are O(n) – watch for loops that stop early or change the input variable (e.g., `i = i * 2` creates O(log n))
- Forgetting to simplify – O(5n) is O(n)
- Ignoring hidden costs – array methods like `.shift()` or `.splice()` can be O(n) internally

