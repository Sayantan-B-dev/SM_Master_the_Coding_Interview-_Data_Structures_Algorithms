## Big O Calculation – Exercise 2

Determine the time and space complexity for each of the following code snippets. Assume all inputs are valid and the code runs to completion.

---

### Problem 1

```python
def func1(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            total += arr[i] * arr[j]
    return total
```

---

### Problem 2

```python
def func2(n):
    if n <= 0:
        return 0
    return n + func2(n - 1)
```

---

### Problem 3

```python
def func3(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result.append(arr[i] + arr[j])
    return result
```

---

### Problem 4

```python
def func4(arr):
    i = 1
    count = 0
    while i < len(arr):
        count += 1
        i = i * 2
    return count
```

---

### Problem 5

```python
def func5(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    for j in range(len(arr)):
        total += arr[j] * 2
    return total
```

---

### Problem 6

```python
def func6(matrix):
    # matrix is n x n
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j]
    return total
```

---

### Problem 7

```python
def func7(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return sum(left) + sum(right)
```

---

### Problem 8

```python
def func8(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                pairs.append((arr[i], arr[j]))
    return pairs
```

---

## Answer Key

| Problem | Time Complexity | Space Complexity | Explanation |
| :--- | :--- | :--- | :--- |
| 1 | O(n²) | O(1) | Nested loops over the full array length. No extra space proportional to n. |
| 2 | O(n) | O(n) | Recurses n times, but each call adds to the call stack (space). |
| 3 | O(n²) | O(n²) | Outer loop runs n times, inner loop runs roughly n/2 times on average → O(n²). The result list contains about n²/2 elements. |
| 4 | O(log n) | O(1) | i doubles each iteration → logarithmic growth. |
| 5 | O(n) | O(1) | Two separate loops, each O(n) → O(2n) simplifies to O(n). |
| 6 | O(n²) | O(1) | Nested loops over an n x n matrix. |
| 7 | O(n) | O(n) | Slicing creates copies of the array (O(n) space and time for the slice). Summing also O(n). |
| 8 | O(n²) | O(n²) | Nested loops over all pairs, excludes self-pairs but still O(n²). Output list has n*(n-1) elements. |

---
