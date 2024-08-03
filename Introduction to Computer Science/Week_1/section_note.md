## Introduction

This note is derived from a lecture transcript of the first section of CS50, an introductory computer science course. The section is led by Carter Zenke and aims to bridge the gap between lectures and problem sets. The main focus is on transitioning from Scratch to the C programming language, covering topics such as variables, types, user input, output, functions, loops, and conditionals.

## Index
1. Variables and Types
2. User Input and Output
3. Functions
4. Loops and Conditionals
5. Practical Example: Hello World Program
6. Practical Example: Contacts Application
7. Practical Example: Mario Pyramid

## 1. Variables and Types

Definition: A variable is a way to store information in a computer, such as a number or a character. Types define the kind of value a variable can hold, such as integers or characters.

### Explanation:

- Variables are containers for values that can change over time.
- Types specify the kind of value a variable can store (e.g., int for integers, char for characters).
- Example: `int calls = 3;` declares an integer variable named calls with a value of 3.
Assignment operator (`=`) is used to assign values to variables.

Code Example:

```javascript
int calls = 3;
```

### Additional Explanations:

- Type declaration ensures appropriate memory allocation.
- Variables must be declared before use.

### Additional Code Examples:
```javascript
char grade = 'A';
float price = 9.99;
```

## 2. User Input and Output

Definition: User input is the data provided by the user during the program's execution, and output is the information presented to the user.

### Explanation:

- Use functions like `get_int()` and `printf()` for input and output.
- Input function `get_int()` prompts the user to enter an integer.
- Output function `printf()` formats and prints data to the console.
- Format specifiers (`%i`, `%s`, `%f`, `%c`) in `printf()` help format output.

Code Example:

```javascript
int age = get_int("What is your age? ");
printf("You are %i years old\n", age);
```

### Explanation of Format Specifiers:

- `%i`: Used to format integers. For example, if `age` is 20, `printf("You are %i years old\n", age);` will output "You are 20 years old".
- `%s`: Used to format strings. For example, if name is "Alice", `printf("Hello, %s!\n", name);` will output "Hello, Alice!".
- `%f`: Used to format floating-point numbers. For example, if `price` is 9.99, `printf("The price is %f\n", price);` will output "The price is 9.990000".
- `%c`: Used to format single characters. For example, if `grade` is 'A', `printf("Your grade is %c\n", grade);` will output "Your grade is A".

### Additional Code Examples:

```javascript
string name = get_string("What is your name? ");
printf("Hello, %s!\n", name);

float price = 9.99;
printf("The price is %.2f\n", price);
```

## 3. Functions

Definition: Functions are blocks of code designed to perform specific tasks, and they can be reused throughout a program.

### Explanation:

- Functions encapsulate code for reusability and organization.
- Functions can take inputs (parameters) and return outputs.
- Function prototypes declare functions before their use.
- Functions can return values or be void.

Code Example:

```javascript
void print_greeting(string name) {
    printf("Hello, %s!\n", name);
}

int add(int a, int b) {
    return a + b;
}
```

### Explanation of Function Prototypes:

- Function prototypes provide a declaration of a function that specifies its return type, name, and parameters, allowing the function to be used before its actual definition.
- Example of a function prototype:

```javascript
void print_greeting(string name);
int add(int a, int b);
```

### Additional Explanations:

- Function prototypes are usually placed at the beginning of the file, after the `#include` statements.
- The `void` keyword indicates that the function does not return a value.

Additional Code Examples:
```javascript
// Function prototype
float calculate_area(float radius);

// Main function
int main(void) {
    float area = calculate_area(5.0);
    printf("The area is %.2f\n", area);
    return 0;
}

// Function definition
float calculate_area(float radius) {
    return 3.14159 * radius * radius;
}
```

## 4. Loops and Conditionals
Definition: Loops execute a block of code repeatedly, and conditionals execute code based on certain conditions.

### Explanation:

- `for` and `while` loops iterate over code blocks.
- Conditionals like `if`, `else if`, and `else` control the flow based on conditions.

Code Example:

```javascript
for (int i = 0; i < 5; i++) {
    printf("%i\n", i);
}
if (x > 0) {
    printf("Positive\n");
} else {
    printf("Non-positive\n");
}
```

### Additional Explanations:

Loops help in repetitive tasks.
Conditionals make decisions based on conditions.

### Additional Code Examples:

```javascript
while (n > 0) {
    printf("%i\n", n);
    n--;
}
```

## 5. Practical Example: Hello World Program
Definition: A simple program that prints "Hello, World!" to the console.

### Explanation:

- A basic example to understand syntax and structure.
- Includes library headers, main function, and print statement.

Code Example:

```javascript
#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

### Additional Explanations:

- The main function is the entry point of C programs.
- `printf` is used to print text to the console.

### Additional Code Examples:

```javascript
#include <stdio.h>

int main(void) {
    printf("Welcome to CS50!\n");
    return 0;
}
```

## 6. Practical Example: Contacts Application
Definition: A program that collects and displays a user's contact information.

### Explanation:

- Demonstrates variable declaration, user input, and formatted output.
- Uses `get_string` and `get_int` for user input.

Code Example:

```javascript
#include <stdio.h>
#include <cs50.h>

int main(void) {
    string name = get_string("What is your name? ");
    int age = get_int("What is your age? ");
    string number = get_string("What is your phone number? ");
    
    printf("Name: %s\nAge: %i\nPhone: %s\n", name, age, number);
    return 0;
}
```

### Additional Explanations:

- Input validation can be added for robustness.
- Data can be stored in arrays or structures for multiple contacts.

### Additional Code Examples:

```javascript
string email = get_string("What is your email? ");
printf("Email: %s\n", email);
```

## 7. Practical Example: Mario Pyramid

Definition: A program that prints a pyramid of hashes similar to the game Mario.

### Explanation:

- Uses loops to create rows and columns of hashes.
- Demonstrates nested loops for complex patterns.

### Detailed Explanation:

- The goal is to print a pyramid of hashes, where the height is specified by the user.
- The bottom row of the pyramid will have the same number of hashes as the height.
- Each row above the bottom row will have one less hash than the row below it.
- This example uses nested loops to achieve the desired pattern.

Code Example:

```javascript
#include <stdio.h>
#include <cs50.h>

int main(void) {
    int height = get_int("Height: ");
    for (int i = 0; i < height; i++) {
        for (int j = 0; j <= i; j++) {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
```

### Explanation:

- The outer loop `(for (int i = 0; i < height; i++))` runs height times to create the rows.
- The inner loop `(for (int j = 0; j <= i; j++))` runs `i+1` times to print the appropriate number of hashes for each row.
- `printf("\n")` moves the cursor to the next line after printing each row of hashes.

### Advanced Mario Pyramid Example:

- A more complex version of the pyramid might include spaces to align the pyramid to the right.

### Advanced Code Example:

```javascript
#include <stdio.h>
#include <cs50.h>

int main(void) {
    int height = get_int("Height: ");
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < height - i - 1; j++) {
            printf(" ");
        }
        for (int k = 0; k <= i; k++) {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
```

### Explanation:

- The first inner loop `(for (int j = 0; j < height - i - 1; j++))` prints spaces to align the hashes to the right.
- The second inner loop `(for (int k = 0; k <= i; k++))` prints the hashes for each row.

### Summary

1. Variables and Types: Variables store data, and types define the kind of data stored.
2. User Input and Output: Functions like get_int and printf handle user input and output, using format specifiers to format the output.
3. Functions: Functions encapsulate code for reusability, taking inputs and returning outputs. Function prototypes declare functions before their use.
4. Loops and Conditionals: Loops repeat code, and conditionals execute code based on conditions.
5. Practical Example: Hello World Program: A simple program to print a greeting message.
6. Practical Example: Contacts Application: Collects and displays user contact information.
7. Practical Example: Mario Pyramid: Prints a pyramid pattern using nested loops, demonstrating complex patterns with advanced formatting.
