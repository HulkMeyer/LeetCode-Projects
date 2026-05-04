# Two Sum

A LeetCode problem walkthrough with two different approaches: a brute-force solution and an optimized hash-map (find complement) solution.

## Problem Description

![Problem Description](Images/Problem%20Description.png)

## Solutions

### Solution 1 — Brute Force

File: [`solution_1_brute_force.py`](solution_1_brute_force.py)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                total = nums[a] + nums[b]
                if total == target:
                    return [a, b]
```

**How it works:**
The outer loop picks an index `a`, and the inner loop picks every index `b` that comes after it. For each pair, the two values are added together and compared to `target`. As soon as a matching pair is found, the indices are returned. Starting `b` at `a + 1` avoids re-checking pairs and prevents using the same element twice.

- **Time complexity:** O(n²) — every element is compared against every other element.
- **Space complexity:** O(1) — no extra data structures.

Simple and easy to reason about, but it scales poorly for large inputs.

### Solution 2 — Find Complement (Hash Map)

File: [`solution_2_find_complement.py`](solution_2_find_complement.py)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i, x in enumerate(nums):
            need = target - x
            if need in checked:
                return [checked[need], i]
            checked[x] = i
```

**How it works:**
A dictionary called `checked` stores numbers we've already seen, mapped to their index. For each number `x`, we calculate the complement (`need = target - x`) — the value that would have to pair with `x` to hit the target. If that complement is already in the dictionary, we've found our answer and return the stored index along with the current one. Otherwise, we store `x` and its index and continue. Every number is checked against everything that came before it in a single pass.

- **Time complexity:** O(n) — single pass through the array, with O(1) average hash-map lookups.
- **Space complexity:** O(n) — the hash map can hold up to `n` entries in the worst case.

This is the optimal solution and the one typically expected in interviews.

## Repository Structure

```
Two Sums Problem/
├── Images/
│   └── Problem Description.png
├── solution_1_brute_force.py
├── solution_2_find_complement.py
└── README.md
```
