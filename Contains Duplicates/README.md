# Contains Duplicates

A LeetCode problem walkthrough exploring two approaches to detecting duplicate values in an array: a sort-based approach and an optimized hash-set approach.

## Problem Description

![Problem Description](Images/Project%20Problem%20Image.png)

## Solutions

### Solution 1 — Sort + Adjacent Compare

File: [`Scripts/solution_1_contains_duplicates.py`](Scripts/solution_1_contains_duplicates.py)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
```

**How it works:**
Sorting the list groups any duplicate values next to each other. After sorting, a single pass through the list comparing each element to the one immediately after it (`nums[i]` vs. `nums[i + 1]`) is enough to catch any duplicates. If a match is found, return `True` immediately. If the loop finishes without finding one, return `False`.

- **Time complexity:** O(n log n) — dominated by the sort step.
- **Space complexity:** O(1) extra space, since Python's `list.sort()` sorts in place. Note that this approach mutates the input list.

### Solution 2 — Hash Set

File: [`Scripts/solution_2_contains_duplicates.py`](Scripts/solution_2_contains_duplicates.py)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
```

**How it works:**
A `set` called `seen` keeps track of every value already encountered. For each number `n`, check whether it's already in the set — if so, that's a duplicate and the function returns `True`. Otherwise, add it to the set and continue. The set is only ever grown, never re-scanned, because membership checks (`n in seen`) are O(1) on average for a hash set.

- **Time complexity:** O(n) — single pass through the array with O(1) average set lookups and inserts.
- **Space complexity:** O(n) — the set can grow to hold every element.

This is the optimal solution for the problem. It also short-circuits the moment a duplicate is found, so it returns early on inputs where duplicates appear near the front.

## Comparison

| Approach | Time | Space | Mutates Input |
|---|---|---|---|
| Sort + Adjacent Compare | O(n log n) | O(1) | Yes |
| Hash Set | **O(n)** | O(n) | No |

The hash-set approach trades extra memory for a faster runtime — a classic time-vs-space tradeoff worth recognizing in interviews.

## Repository Structure

```
Contains Duplicates/
├── Images/
│   └── Project Problem Image.png
├── Scripts/
│   ├── solution_1_contains_duplicates.py
│   └── solution_2_contains_duplicates.py
└── README.md
```
