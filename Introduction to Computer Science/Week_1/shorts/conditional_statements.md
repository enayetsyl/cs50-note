## Introduction

In this note, we will explore the essential concept of conditional statements in programming. Conditional expressions allow programs to make decisions and follow different execution paths based on variable values or user inputs. This ability to branch the program flow is critical for creating dynamic and responsive software.

## Index
1. Basic If Statement
2. If-Else Statement
3. If-Else If-Else Chain
4. Non-Mutually Exclusive Branches
5. Switch Statement
6. Ternary Operator

## Basic If Statement

Definition: An `if` statement is a fundamental control structure that executes a block of code only if a specified Boolean expression evaluates to true.

## Explanation:
The `if` statement in C evaluates a Boolean expression within parentheses. If the expression is true, the code within the curly braces `{}` executes. If false, the block is skipped.

Example:

```javascript
if (x < 10) {
    printf("x is less than 10");
}
```

### Additional Examples:

Example 1:
```javascript
int age = 18;
if (age >= 18) {
    printf("You are eligible to vote.");
}
```

Example 2:
```javascript
int score = 75;
if (score > 50) {
    printf("You passed the test.");
}
```

### If-Else Statement
Definition: An `if-else` statement provides an alternative path of execution when the Boolean expression in the `if` statement evaluates to false.

### Explanation:
The `if-else` statement evaluates a Boolean expression. If true, the code within the first set of curly braces `{}` executes. If false, the code within the `else` block executes.

Example:
```javascript
if (x < 10) {
    printf("x is less than 10");
} else {
    printf("x is 10 or greater");
}
```

### Additional Examples:

Example 1:

```javascript
int age = 16;
if (age >= 18) {
    printf("You are an adult.");
} else {
    printf("You are a minor.");
}
```

Example 2:

```javascript
int temperature = 30;
if (temperature > 25) {
    printf("It's hot outside.");
} else {
    printf("The weather is cool.");
}
```

### If-Else If-Else Chain
Definition: An if-else if-else chain allows multiple conditions to be checked in sequence, executing the corresponding block of code for the first true condition.

### Explanation:
This structure checks each condition in order. Once a true condition is found, its block executes, and the rest are skipped.

Example:
```javascript
if (x < 10) {
    printf("x is less than 10");
} else if (x < 20) {
    printf("x is between 10 and 19");
} else {
    printf("x is 20 or greater");
}
```

### Additional Examples:

Example 1:

```javascript
int grade = 85;
if (grade >= 90) {
    printf("A");
} else if (grade >= 80) {
    printf("B");
} else if (grade >= 70) {
    printf("C");
} else {
    printf("F");
}
```

Example 2:
```javascript
int speed = 60;
if (speed > 100) {
    printf("Over speed limit");
} else if (speed > 80) {
    printf("Fast");
} else if (speed > 50) {
    printf("Moderate");
} else {
    printf("Slow");
}
```

### Non-Mutually Exclusive Branches
Definition: This involves creating conditions where multiple branches can be true and execute, not just one.

### Explanation:
Conditions are checked independently, allowing multiple true conditions to trigger multiple blocks of code.

Example:
```javascript
if (x > 0) {
    printf("x is positive");
}
if (x % 2 == 0) {
    printf("x is even");
}
```

### Additional Examples:

Example 1:
```javascript
if (temperature > 30) {
    printf("It's hot");
}
if (humidity > 70) {
    printf("It's humid");
}
```
Example 2
```javascript
if (score >= 50) {
    printf("Passed");
}
if (score > 80) {
    printf("With distinction");
}
```

### Switch Statement
Definition: A `switch` statement allows variable evaluation against a list of values (cases) and executes corresponding code blocks.

### Explanation:
The `switch` statement compares a variable against multiple cases. Each case ends with a `break` to prevent fall-through, unless intentional.

Example:
```javascript
int x = GetInt();
switch (x) {
    case 1:
        printf("One");
        break;
    case 2:
        printf("Two");
        break;
    default:
        printf("Other");
        break;
}
```

### Additional Examples:

Example 1:
```javascript
char grade = 'B';
switch (grade) {
    case 'A':
        printf("Excellent");
        break;
    case 'B':
        printf("Good");
        break;
    default:
        printf("Average");
        break;
}
```

Example 2:
```javascript
int day = 4;
switch (day) {
    case 1:
        printf("Monday");
        break;
    case 2:
        printf("Tuesday");
        break;
    default:
        printf("Other day");
        break;
}
```

### Ternary Operator
Definition: The ternary operator `?:` is a shorthand for `if-else` statements used to assign values based on a condition.

### Explanation:
This operator evaluates a condition and returns one value if true and another if false, all in one line of code.

Example:

```javascript
int x = (a > b) ? a : b;
```

Additional Examples:

Example 1:
```javascript
int max = (num1 > num2) ? num1 : num2;
```

Example 2:
```javascript
char grade = (score >= 90) ? 'A' : 'B';
```

## Summary
1. Basic If Statement: Executes a block of code if a Boolean expression is true.
2. If-Else Statement: Executes one block if a condition is true, another if false.
3. If-Else If-Else Chain: Checks multiple conditions in sequence, executing the block for the first true condition.
4. Non-Mutually Exclusive Branches: Allows multiple true conditions to execute their respective blocks independently.
5. Switch Statement: Evaluates a variable against multiple cases, executing the corresponding block.
6. Ternary Operator: A concise way to assign values based on a condition.
