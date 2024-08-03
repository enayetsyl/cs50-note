## Introduction

This lecture covers foundational concepts in computer science focusing on algorithms and data structures. It emphasizes thinking algorithmically, discussing different searching algorithms, and introduces the concept of structuring data efficiently using C programming language. Practical demonstrations illustrate how these concepts are implemented in real-world scenarios.

## Index

1. Thinking Algorithmically
2. Search Algorithms
  -  Linear Search
  - Binary Search
3. Data Structures
  - Arrays
  - Structs in C
4. Analyzing Algorithm Efficiency
  - Big O Notation
  - Omega and Theta Notations
5. Practical Implementation in C
  - Linear Search Implementation
  - String Comparison

## 1. Thinking Algorithmically

### Definition/Initial Summary:

Thinking algorithmically involves breaking down real-world problems into manageable steps that can be expressed through code.

### Explanation: 
The lecture introduces the idea of dividing and conquering problems. This method simplifies complex problems by breaking them into smaller, more manageable sub-problems. A classic example provided is the phone book problem, where different strategies for searching are discussed.

## 2. Search Algorithms

### Linear Search
### Definition/Initial Summary:

Linear search sequentially checks each element of a list until the desired element is found or the list ends.

### Explanation: 

Linear search is a straightforward algorithm that scans each element one by one. It's simple but can be inefficient for large datasets as it might require checking every single element.
Example:

```javascript
for (int i = 0; i < 7; i++) {
    if (numbers[i] == target) {
        printf("Found\n");
        return 0;
    }
}
printf("Not Found\n");
return 1;
```

### Binary Search

### Definition/Initial Summary:

Binary search is an efficient algorithm for finding an item from a sorted list of items by repeatedly dividing the search interval in half.

### Explanation: 
Binary search starts in the middle of a sorted array and eliminates half of the remaining elements each step. This drastically reduces the number of comparisons needed.

Example:

```javascript
int binary_search(int array[], int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (array[middle] == target) return middle;
        if (array[middle] < target) left = middle + 1;
        else right = middle - 1;
    }
    return -1;
}
```

### Additional Explanations and Examples:

Binary Search in a List of Dates:
Example:

```javascript
typedef struct {
    int day;
    int month;
    int year;
} Date;

int compare_dates(Date d1, Date d2) {
    if (d1.year != d2.year) return d1.year - d2.year;
    if (d1.month != d2.month) return d1.month - d2.month;
    return d1.day - d2.day;
}

int binary_search_dates(Date dates[], int size, Date target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        int comparison = compare_dates(dates[middle], target);
        if (comparison == 0) return middle;
        if (comparison < 0) left = middle + 1;
        else right = middle - 1;
    }
    return -1;
}
```

Binary Search in an Array of Sorted Temperatures:
Example:

```javascript
int binary_search_temperatures(float temps[], int size, float target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (temps[middle] == target) return middle;
        if (temps[middle] < target) left = middle + 1;
        else right = middle - 1;
    }
    return -1;
}
```

## 3. Data Structures

### Arrays

### Definition/Initial Summary:

Arrays are collections of elements identified by index or key, where each element is of the same data type.

### Explanation: 

Arrays store elements contiguously in memory, which allows efficient access to any element using its index.

Example:

```javascript
int numbers[5] = {10, 20, 30, 40, 50};
```

### Structs in C

### Definition/Initial Summary:

Structs (short for structures) are custom data types in C that group together different variables under one name.
Explanation: Structs can hold multiple data types, allowing more complex data models. For example, a `person` struct can contain both a name and a phone number.

Example:

```javascript
typedef struct {
    char *name;
    char *number;
} Person;

Person people[3];
people[0].name = "Alice";
people[0].number = "123-4567";
```

### Additional Explanations and Examples:

### Structs for Address Books:

Example:

```javascript
typedef struct {
    char *name;
    char *phone;
    char *address;
} AddressBookEntry;

AddressBookEntry contacts[100];
contacts[0].name = "Alice";
contacts[0].phone = "123-4567";
contacts[0].address = "123 Main St.";
```

### Structs for Inventory Items:

Example:

```javascript
typedef struct {
    char *itemName;
    int quantity;
    float price;
} InventoryItem;

InventoryItem inventory[50];
inventory[0].itemName = "Widget";
inventory[0].quantity = 100;
inventory[0].price = 2.99;
```

## 4. Analyzing Algorithm Efficiency

### Big O Notation

### Definition/Initial Summary:

Big O notation describes the upper bound of the time complexity of an algorithm, giving the worst-case scenario.

### Explanation: 

It provides a high-level understanding of an algorithm's efficiency, ignoring constant factors and lower-order terms.

Example: Linear search has a time complexity of O(n), where n is the number of elements.

### Additional Explanations and Examples:

### Big O of Bubble Sort:

### Explanation: 

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

Example:

```javascript
void bubble_sort(int array[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}
// Time complexity: O(n^2)
```

### Big O of Merge Sort:

### Explanation: 

Merge sort divides the array into halves, recursively sorts them, and then merges the sorted halves back together.

Example:

```javascript
void merge(int array[], int left, int middle, int right) {
    int n1 = middle - left + 1;
    int n2 = right - middle;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = array[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = array[middle + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            array[k] = L[i];
            i++;
        } else {
            array[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        array[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        array[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(int array[], int left, int right) {
    if (left < right) {
        int middle = left + (right - left) / 2;
        merge_sort(array, left, middle);
        merge_sort(array, middle + 1, right);
        merge(array, left, middle, right);
    }
}
// Time complexity: O(n log n)
```

### Omega and Theta Notations

### Definition/Initial Summary:

Omega notation describes the lower bound of the time complexity of an algorithm, while Theta notation describes the exact bound, combining both upper and lower bounds.
Explanation:

- Omega Notation (Ω): Provides the best-case scenario for an algorithm, representing the minimum number of steps required.
- Theta Notation (Θ): Provides a tight bound, indicating that the algorithm's time complexity is both upper and lower bounded by a specific function.
- Best case for linear search is Ω(1).
- Theta notation for binary search is Θ(log n).

### Additional Explanations and Examples:

- Omega of Insertion Sort: Best case Ω(n) when the array is already sorted.
- Theta of Quick Sort: Average case Θ(n log n), worst case Θ(n^2).

## 5. Practical Implementation in C

### Linear Search Implementation

### Definition/Initial Summary:

Demonstrates a practical implementation of linear search in C using arrays.
Example: See linear search example in section 2.

### String Comparison

### Definition/Initial Summary:

String comparison in C requires using the `strcmp` function instead of `==`.
Explanation: The `strcmp` function compares two strings and returns 0 if they are equal.

Example:

```javascript
if (strcmp(str1, str2) == 0) {
    printf("Strings are equal\n");
}
```

### Additional Explanations and Examples:

Comparing User Input to a List of Commands:

Example:

```javascript
char *commands[] = {"start", "stop", "pause", "resume"};
char *input = get_string("Enter command: ");
for (int i = 0; i < 4; i++) {
    if (strcmp(input, commands[i]) == 0) {
        printf("Command recognized: %s\n", input);
        break;
    }
}
```

### Case-Insensitive String Comparison Using `strcasecmp`:

Example:

```javascript
#include <strings.h>

char *commands[] = {"start", "stop", "pause", "resume"};
char *input = get_string("Enter command: ");
for (int i = 0; i < 4; i++) {
    if (strcasecmp(input, commands[i]) == 0) {
        printf("Command recognized: %s\n", input);
        break;
    }
}
```
## Summary

1. Thinking Algorithmically: Breaking down problems into smaller steps to map out a logical approach for solutions.

2. Search Algorithms:
  - Linear Search: Sequentially checks each element; O(n) time complexity.
  - Binary Search: Efficiently divides the search space in a sorted list; O(log n) time complexity.

3. Data Structures:
  - Arrays: Store elements contiguously; efficient indexing.
  - Structs in C: Custom data types grouping multiple variables.

4. Analyzing Algorithm Efficiency:
  - Big O Notation: Upper bound of time complexity.
  - Omega and Theta Notations: Lower bound and exact bound of time complexity.

5. Practical Implementation in C:
  - Linear search with arrays.
  - String comparison with strcmp.