# Time Complexity

Time Complexity is the amount of time an algorithm takes to execute as the input size increases.

It helps us measure the efficiency of a program.

> Time Complexity does not measure the actual time in seconds.  
> It measures how the execution time grows with input size.

---

# Space Complexity

Space Complexity is the amount of additional memory or space used by an algorithm to execute a task.

It includes:

- Temporary variables
- Data structures
- Function call stack
- Extra memory allocation

---

# Ways to Represent Complexity

There are mainly three ways to represent the complexity of an algorithm:

| Notation | Meaning | Represents |
|----------|----------|-------------|
| `O` | Big O Notation | Worst Case |
| `Θ` | Theta Notation | Average Case |
| `Ω` | Omega Notation | Best Case |

---

# 1. Big O Notation — `O`

Big O Notation represents the **Worst Case Scenario** or **Upper Bound** of an algorithm.

It tells us the maximum time an algorithm can take for a given input size.

## Examples

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)