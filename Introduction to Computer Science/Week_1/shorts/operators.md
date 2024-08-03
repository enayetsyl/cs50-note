## Introduction

This note covers various operators in C programming, providing an overview of arithmetic, assignment, shorthand, and Boolean operators, including their use and examples. Understanding these operators is crucial for manipulating and comparing values in C programs.

## Index

1. Assignment Operator
2. Arithmetic Operators
3. Modulus Operator
4. Shorthand Operators
5. Increment and Decrement Operators
6. Boolean Expressions
7. Logical Operators
8. Relational Operators

## 1. Assignment Operator

### Definition:
The assignment operator in C, denoted by the single equal sign =, assigns a value to a variable.

### Explanation:
The assignment operator stores the value on the right side into the variable on the left side. For example:

```javascript
int y = 10;
int x = y + 1; // x is assigned the value 11
```

Additional Explanations and Examples:
1. `int a = 5; // a is assigned 5`
2. `float b = 3.14; // b is assigned 3.14`

## 2. Arithmetic Operators

### Definition:
Arithmetic operators perform basic mathematical operations. The common ones are addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).

### Explanation:

These operators allow for standard arithmetic calculations:

```javascript
int x = 10;
int y = x + 5; // y is 15
x = y - 3; // x is 12
x = x * 2; // x is 24
x = x / 4; // x is 6
```

Additional Explanations and Examples:

1. `int result = 20 + 30; // result is 50`
2. `double quotient = 10.0 / 3.0; // quotient is approximately 3.33`

## 3. Modulus Operator

### Definition:
The modulus operator (`%`) gives the remainder of the division of two integers.

### Explanation:
This operator is useful for operations requiring the remainder of a division:

```javascript
int m = 13 % 4; // m is 1, because 13 divided by 4 is 3 with a remainder of 1
```

Additional Explanations and Examples:
1. `int remainder = 9 % 2; // remainder is 1`
2. `int mod_result = 7 % 3; // mod_result is 1`

## 4. Shorthand Operators

### Definition:
Shorthand operators simplify operations by combining arithmetic and assignment into a single operation.

### Explanation:
Examples of shorthand operators include `+=`, `-=`, `*=`, `/=`, and `%=`:

```javascript
int x = 10;
x += 5; // x is now 15, same as x = x + 5
x *= 2; // x is now 30, same as x = x * 2
```

Additional Explanations and Examples:
1. `int a = 20; a -= 5; // a is 15`
2. `int b = 6; b /= 2; // b is 3`

## 5. Increment and Decrement Operators

### Definition:
Increment (`++`) and decrement (`--`) operators increase or decrease a variable's value by one.

### Explanation:
These operators provide a concise way to adjust a variable's value:

```javascript
int x = 10;
x++; // x is now 11
x--; // x is now 10
```

Additional Explanations and Examples:
1. `int a = 5; a++; // a is 6`
2. `int b = 3; b--; // b is 2`

## 6. Boolean Expressions

### Definition:
Boolean expressions evaluate to either `true` or `false` and are used for decision-making in code.

### Explanation:
In C, any non-zero value is considered `true`, and zero is `false`. Boolean expressions are crucial for control structures like `if` statements and loops.

Additional Explanations and Examples:

1. `int isTrue = 1; // non-zero value is true`
2. `int isFalse = 0; // zero value is false`

## 7. Logical Operators

### Definition:
Logical operators are used to perform logical operations, including AND (`&&`), OR (`||`), and NOT (`!`).

### Explanation:
These operators evaluate conditions to return `true` or `false`:

```javascript
int x = 1, y = 0;
int result = (x && y); // result is 0 (false)
result = (x || y); // result is 1 (true)
result = !x; // result is 0 (false)
```

Additional Explanations and Examples:
1. `int a = 5, b = 10; int c = (a < b && a > 0); // c is 1 (true)`
2. `int x = 0, y = 1; int z = !(x || y); // z is 0 (false)`

## 8. Relational Operators

### Definition:
Relational operators compare values, including `==`, `!=`, `<`, `<=`, `>`, and `>=`.

### Explanation:

These operators return `true` or `false` based on the comparison:

```javascript
int x = 10, y = 20;
int result = (x == y); // result is 0 (false)
result = (x != y); // result is 1 (true)
result = (x < y); // result is 1 (true)
```

Additional Explanations and Examples:
1. `int a = 5, b = 5; int c = (a <= b); // c is 1 (true)`
2. `int x = 15, y = 10; int z = (x >= y); // z is 1 (true)`

## Summary

This note provided an overview of operators in C, including:

1. Assignment Operator: Used to assign values to variables.
2. Arithmetic Operators: Perform basic mathematical operations.
3. Modulus Operator: Calculates the remainder of a division.
4. Shorthand Operators: Combine arithmetic and assignment operations.
5. Increment and Decrement Operators: Increase or decrease a variable's value by one.
6. Boolean Expressions: Evaluate to true or false.
7. Logical Operators: Perform logical operations like AND, OR, and NOT.
8. Relational Operators: Compare values and return true or false.