## Introduction

This note covers the contents of Lecture 1 from CS50, focusing on the basics of the C programming language. The lecture introduces fundamental concepts such as variables, functions, conditionals, loops, and the process of compiling and running C programs. It also emphasizes the transition from Scratch, a graphical programming language, to C, a more traditional and text-based language.

## Index
1. Introduction to C
2. Writing and Running C Programs
3. Variables and Data Types
4. Functions and Libraries
5. Conditionals and Control Flow
6. Compiling and Debugging
7. Summary

## 1. Introduction to C

### Definition/Initial Summary:

C is a traditional programming language that provides a foundation for learning other languages. It is more complex than Scratch but offers greater control and efficiency in programming.

### Explanation:

The lecture begins by emphasizing the transition from Scratch to C. While Scratch is a visual programming language aimed at beginners, C is a more powerful and versatile language used in many real-world applications. The primary goal of the lecture is to introduce students to the basics of C, including its syntax and structure.

## 2. Writing and Running C Programs

### Definition/Initial Summary:

Writing and running C programs involves creating source code, compiling it into machine code, and executing the resulting program.

### Explanation:

- Source Code: This is the human-readable code written by programmers using a text editor. Source code in C is typically saved with a .c file extension.

- Machine Code: This is the binary code that the computer can execute directly. It is generated from the source code through a process called compilation.

- Compiler: A compiler is a tool that translates the source code into machine code. Commonly used compilers for C include GCC (GNU Compiler Collection).

### Steps to Run a C Program:

1. Write the Code: Write the source code in a text editor and save it with a .c extension.
2. Compile the Code: Use a compiler to convert the source code into machine code.
3. Run the Compiled Program: Execute the machine code to run the program.

Example:

```javascript
#include <stdio.h>

int main(void) {
    printf("Hello, world!\n");
    return 0;
}

```

### Additional Explanation:

1. Syntax Highlighting: Modern text editors like VS Code provide syntax highlighting, which uses colors to differentiate between various parts of the code, making it easier to read and debug.
2. Errors: When compiling, the compiler checks the code for errors. If errors are found, it provides error messages to help the programmer identify and fix them.

### Additional Examples:

1. Program that prints a user-provided message:

```javascript
#include <stdio.h>

int main(void) {
    char message[100];
    printf("Enter a message: ");
    fgets(message, sizeof(message), stdin);
    printf("You entered: %s", message);
    return 0;
}

```

2. Program that adds two numbers and displays the result:

```javascript
#include <stdio.h>

int main(void) {
    int num1, num2, sum;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);
    sum = num1 + num2;
    printf("Sum: %d\n", sum);
    return 0;
}
```

## 3. Variables and Data Types

### Definition/Initial Summary:

Variables are used to store data, and data types define the kind of data a variable can hold.

### Explanation:

- Variable Declaration: This specifies the type and name of the variable. For example, `int age;` declares a variable named `age` of type `int`.
- Data Types: C provides several data types to handle different kinds of data. Common data types include:
  - int: Used for integers.
  - float: Used for floating-point numbers.
  - char: Used for single characters.
  - string (usually implemented as arrays of characters in C): Used for sequences of characters.

Example:

```javascript
int age = 25;
float gpa = 3.8;
char initial = 'A';
char name[] = "Alice";
```

### Additional Explanation:

1. Type Casting: Sometimes it is necessary to convert a variable from one type to another. This process is called type casting. For example, converting a `float` to an `int`:

```javascript
float num = 5.7;
int rounded = (int) num; // rounded will be 5
```
2. Constants: These are variables whose values do not change. They are defined using the const keyword.

```javascript
const int DAYS_IN_WEEK = 7;
```

### Additional Examples:

1. Program that calculates the area of a circle given its radius:

```javascript
#include <stdio.h>
#define PI 3.14159

int main(void) {
    float radius, area;
    printf("Enter radius: ");
    scanf("%f", &radius);
    area = PI * radius * radius;
    printf("Area of the circle: %.2f\n", area);
    return 0;
}
```
2. Program that converts temperature from Celsius to Fahrenheit:
```javascript
#include <stdio.h>

int main(void) {
    float celsius, fahrenheit;
    printf("Enter temperature in Celsius: ");
    scanf("%f", &celsius);
    fahrenheit = (celsius * 9 / 5) + 32;
    printf("Temperature in Fahrenheit: %.2f\n", fahrenheit);
    return 0;
}
```

## 4. Functions and Libraries

### Definition/Initial Summary:
Functions are reusable blocks of code that perform specific tasks. Libraries are collections of pre-written functions that can be used in programs.

### Explanation:

- Function Definition: This specifies what the function does. A function usually has a name, a return type, and parameters.
- Function Call: This is when a function is executed. The function name is followed by parentheses, which may contain arguments.
- Libraries: Libraries contain pre-written functions that simplify programming. The standard library in C includes headers like stdio.h for input and output operations.

Example:
```javascript
#include <stdio.h>

void greet(void) {
    printf("Hello, world!\n");
}

int main(void) {
    greet();
    return 0;
}
```
### Additional Explanation:

1. Parameters and Return Values: Functions can take inputs, known as parameters, and can return a value. For example:

```javascript
int add(int a, int b) {
    return a + b;
}

int main(void) {
    int result = add(5, 3);
    printf("Result: %d\n", result);
    return 0;
}
```

2. Standard Libraries: Libraries provide common functions that make programming easier. For instance, the math.h library provides mathematical functions like sqrt and pow.

### Additional Examples:

1. Function that calculates the factorial of a number:

```javascript
#include <stdio.h>

int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main(void) {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Factorial of %d is %d\n", num, factorial(num));
    return 0;
}
```

2. Function that checks if a number is prime:

```javascript
#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main(void) {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    if (is_prime(num)) {
        printf("%d is a prime number.\n", num);
    } else {
        printf("%d is not a prime number.\n", num);
    }
    return 0;
}
```

## 5. Conditionals and Control Flow

### Definition/Initial Summary:
Conditionals are used to execute different code based on certain conditions. Control flow determines the order in which code executes.

### Explanation:

- If Statements: These execute code if a specified condition is true.
```javascript
if (condition) {
    // code to execute if condition is true
}
```
- Else and Else If Statements: These provide alternative code paths if the initial condition is false.

```javascript
if (condition1) {
    // code to execute if condition1 is true
} else if (condition2) {
    // code to execute if condition1 is false and condition2 is true
} else {
    // code to execute if both condition1 and condition2 are false
}
```
- Loops: These repeat code multiple times.
  - For Loop: Repeats code a specified number of times.
```javascript
for (int i = 0; i < 10; i++) {
    // code to repeat
}
```
  - While Loop: Repeats code while a condition is true
```javascript
while (condition) {
    // code to repeat
}
```
  - Do-While Loop: Repeats code at least once and then while a condition is true.
```javascript
do {
    // code to repeat
} while (condition);
```

Example:

```javascript
#include <stdio.h>

int main(void) {
    int x = 10;
    if (x > 0) {
        printf("x is positive\n");
    } else {
        printf("x is non-positive\n");
    }
    return 0;
}
```

### Additional Explanation:

1. Boolean Expressions: These are conditions that evaluate to true or false.

```javascript
int a = 5, b = 10;
if (a < b) {
    printf("a is less than b\n");
}
```

2. Logical Operators: These are used to combine multiple conditions.
- `&&` (logical AND): True if both conditions are true.
- `||` (logical OR): True if at least one condition is true.
- `!` (logical NOT): Inverts the truth value of a condition.

### Additional Examples:

1. Program that finds the maximum of three numbers:
```javascript
#include <stdio.h>

int main(void) {
    int a, b, c;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a >= b && a >= c) {
        printf("%d is the largest number.\n", a);
    } else if (b >= a && b >= c) {
        printf("%d is the largest number.\n", b);
    } else {
        printf("%d is the largest number.\n", c);
    }
    return 0;
}
```

2. Loop that prints the first 10 Fibonacci numbers:
```javascript
#include <stdio.h>

int main(void) {
    int n1 = 0, n2 = 1, n3;
    printf("%d %d ", n1, n2);

    for (int i = 2; i < 10; ++i) {
        n3 = n1 + n2;
        printf("%d ", n3);
        n1 = n2;
        n2 = n3;
    }
    printf("\n");
    return 0;
}
```

## 6. Compiling and Debugging

### Definition/Initial Summary:
Compiling converts source code into executable code. Debugging involves identifying and fixing errors in the code.

### Explanation:

  - Compiler Errors: These are syntax or semantic errors detected during compilation. They must be fixed before the program can be run.
```javascript
gcc -o hello hello.c
```

  - Runtime Errors: These errors occur while the program is running. They can cause the program to crash or produce incorrect results.
  
  - Debugging Tools: These help identify and fix issues in the code. Common tools include `gdb` (GNU Debugger) and debugging features in IDEs (Integrated Development Environments).
```javascript
# Compilation
gcc -o hello hello.c
# Running the program
./hello
```
## Summary

This lecture introduced the basics of C programming, emphasizing the transition from Scratch to C. Key topics included variables, functions, conditionals, and the process of compiling and running C programs.

### Index Summary:

1. Introduction to C: Overview of the transition from Scratch to C.
2. Writing and Running C Programs: Steps to write, compile, and run a C program.
3. Variables and Data Types: Explanation of variables and common data types in C.
4. Functions and Libraries: Introduction to functions and the use of libraries in C.
5. Conditionals and Control Flow: Using conditionals and loops to control program flow.
6. Compiling and Debugging: Compiling code and debugging common errors.