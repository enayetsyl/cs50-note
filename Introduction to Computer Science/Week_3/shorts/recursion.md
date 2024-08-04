## Introduction

This note delves into the beauty and elegance of recursive programming, with an emphasis on understanding recursion through examples like factorial calculation, Fibonacci sequence, and the Collatz conjecture. The goal is to appreciate how recursion can lead to more concise, readable, and aesthetically pleasing code while effectively solving complex problems.

## Index

1. Definition and Beauty of Recursion
2. Recursive Functions: Base Case and Recursive Case
3. Example: Factorial Function
4. Comparing Recursive and Iterative Solutions
5. Multiple Base Cases: Fibonacci Sequence
6. Multiple Recursive Cases: Collatz Conjecture

## 1. Definition and Beauty of Recursion

### Definition:

Recursion is a programming technique where a function calls itself to solve a problem.

### Explanation:
Code isn't just a tool to accomplish tasks; it can be beautiful and elegant. Recursion exemplifies this beauty by solving problems in concise, interesting, and visually appealing ways. Recursive functions are defined as functions that call themselves during execution, breaking problems down into smaller, more manageable parts.

## 2. Recursive Functions: Base Case and Recursive Case

### Definition:

A recursive function typically consists of two main parts: the base case and the recursive case.

### Explanation:

- Base Case: The condition under which the recursion stops. It prevents the function from calling itself indefinitely, avoiding infinite loops and potential program crashes.
- Recursive Case: The part of the function where it calls itself, usually with a smaller or simpler input, moving towards the base case.

## 3. Example: Factorial Function

### Definition:

The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.

### Explanation:

The factorial can be defined recursively:

- Base Case:fact(1)=1
- Recursive Case: fact(n)=n×fact(n−1)

Code Example:

```javascript
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
```

### Execution Examples:
- `fact(5)`

### Step-by-Step Execution:

1. `fact(5)` calls `fact(4)`
2. `fact(4)` calls `fact(3)`
3. `fact(3)` calls `fact(2)`
4. `fact(2)` calls `fact(1)`
5. `fact(1)` returns 1
6. `fact(2)` returns `2 * 1 = 2`
7. `fact(3)` returns `3 * 2 = 6`
8. `fact(4)` returns `4 * 6 = 24`
9. `fact(5)` returns `5 * 24 = 120`

Result: `fact(5) = 120`

### Additional Explanations:

1. Recursive functions break down complex problems into simpler sub-problems.
2. The function stack unwinds once the base case is reached, computing the final result step-by-step.

### Additional Examples:

1. Sum of First N Natural Numbers:
```javascript
def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)
```
Try to find out step-by-step execution by yourself.

2. Power Function:

```javascript
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
```

Try to find out step-by-step execution by yourself.


## 4. Comparing Recursive and Iterative Solutions

### Explanation:

Recursion can often replace iterative loops. For example, calculating factorial iteratively involves using a loop to multiply the numbers, while recursion does this by calling the function repeatedly.

### Code Comparison:

- Recursive Factorial:
```javascript
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
```
- Iterative Factorial:
```javascript
def fact_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### Execution Examples:
- fact_iterative(5)

### Step-by-Step Execution:
1. Initialize result = 1
2. Loop from 1 to 5:
  - `result = 1 * 1 = 1`
  - `result = 1 * 2 = 2`
  - `result = 2 * 3 = 6`
  - `result = 6 * 4 = 24`
  - `result = 24 * 5 = 120`
Result: `fact_iterative(5) = 120`

## 5. Multiple Base Cases: Fibonacci Sequence

### Definition:

The Fibonacci sequence is a series where each number is the sum of the two preceding ones, starting from 0 and 1.

### Explanation:
- Base Cases: fib(1)=0, fib(2)=1
- Recursive Case: fib(n) = fib(n−1) + fib(n−2)

### Code Example:
```javascript
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

### Execution Examples:
- `fib(5)`

### Step-by-Step Execution:

1. `fib(5)` calls `fib(4)` and `fib(3)`
2. `fib(4)` calls `fib(3)` and `fib(2)`
3. `fib(3)` calls `fib(2)` and `fib(1)`
4. `fib(2)` returns 1
5. `fib(1)` returns 0
6. `fib(3)` returns `1 + 0 = 1`
7. `fib(2)` returns 1
8. `fib(4)` returns `1 + 1 = 2`
9. `fib(3)` calls `fib(2)` and `fib(1)`
10. `fib(2)` returns 1
11. `fib(1)` returns 0
12. `fib(3)` returns `1 + 0 = 1`
13. `fib(5)` returns `2 + 1 = 3`
Result: `fib(5) = 3`

### Additional Explanations:
1. Multiple base cases cater to the initial conditions of the sequence.
2. Recursive calls build the sequence by aggregating previous results.

### Additional Examples:

1. Tribonacci Sequence (Three Base Cases):
```javascript
def trib(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return trib(n - 1) + trib(n - 2) + trib(n - 3)
```
- Try to do step by step execution by yourself.

2. Padovan Sequence
```javascript
def padovan(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return padovan(n - 2) + padovan(n - 3)
```
- Try to do step by step execution by yourself.

## 6. Multiple Recursive Cases: Collatz Conjecture

### Definition:

The Collatz conjecture posits that starting with any positive integer n, repeating the process of dividing by 2 if even or multiplying by 3 and adding 1 if odd, will eventually reach 1.

### Explanation:
- Base Case: n=1
- Recursive Cases:
  - If n is even: collatz(n)=1+collatz(n/2)
  - If n is odd: collatz(n)=1+collatz(3n+1)

Code Example:
```javascript
def collatz(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3 * n + 1)
```
### Execution Examples:
- `collatz(6)`

### Step-by-Step Execution:
1. `collatz(6)` calls `collatz(3)`
2. `collatz(3)` calls `collatz(10)`
3. `collatz(10)` calls `collatz(5)`
4. `collatz(5)` calls `collatz(16)`
5. `collatz(16)` calls `collatz(8)`
6. `collatz(8)` calls `collatz(4)`
7. `collatz(4)` calls `collatz(2)`
8. `collatz(2)` calls `collatz(1)`
9. `collatz(1)` returns 0
10. `collatz(2)` returns `1 + 0 = 1`
11. `collatz(4)` returns `1 + 1 = 2`
12. `collatz(8)` returns `1 + 2 = 3`
13. `collatz(16)` returns `1 + 3 = 4`
14. `collatz(5)` returns `1 + 4 = 5`
15. `collatz(10)` returns `1 + 5 = 6`
16. `collatz(3)` returns `1 + 6 = 7`
17. `collatz(6)` returns `1 + 7 = 8`
Result: `collatz(6) = 8`

### Additional Explanations:

1. Two recursive cases handle even and odd values differently.
2. The function keeps reducing n until it reaches 1.

### Additional Examples:

1. Hailstone Sequence:
```javascript
def hailstone(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + hailstone(n // 2)
    else:
        return [n] + hailstone(3 * n + 1)
```
2. Syracuse Sequence:
```javascript
def syracuse(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + syracuse(n // 2)
    else:
        return 1 + syracuse(3 * n + 1)

```

## Summary

1. Definition and Beauty of Recursion: Recursion simplifies complex problems and enhances code elegance.
2. Recursive Functions: Base Case and Recursive Case: Base cases prevent infinite recursion, while recursive cases handle the core logic.
3. Example: Factorial Function: A classic example of recursion that simplifies multiplication of sequences.
4. Comparing Recursive and Iterative Solutions: Recursive solutions can replace loops, offering more concise and readable code.
5. Multiple Base Cases: Fibonacci Sequence: Demonstrates recursion with multiple initial conditions.
6. Multiple Recursive Cases: Collatz Conjecture: Shows how recursion handles different scenarios within the same function.

These topics collectively illustrate the power and elegance of recursion in programming, highlighting its efficiency and simplicity in solving complex problems.

