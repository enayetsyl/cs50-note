## Introduction

This note provides an overview of four fundamental data structures discussed in the CS50 course: arrays, linked lists, hash tables, and tries. It explores the pros and cons of each structure, particularly focusing on their performance in terms of insertion, deletion, lookup, and sorting. The goal is to help decide which data structure is best suited for different scenarios based on the type of data and the operations needed.

## Index

- Arrays
- Linked Lists
- Hash Tables
- Tries

## 1. Arrays

### Definition:

Arrays are a fundamental data structure where elements are stored in contiguous memory locations. They allow random access, meaning any element can be accessed directly if its index is known.

### Explanation:

Arrays are efficient for lookup operations due to their ability to access elements in constant time. However, inserting or deleting elements, especially in the middle of an array, is inefficient as it requires shifting elements to maintain order. Arrays are fixed in size, which means resizing requires creating a new array and copying elements over. Despite these limitations, arrays are space-efficient and easy to sort, making them ideal for scenarios where data size is known in advance and random access is required.

### Additional Explanation:

Dynamic Arrays: In languages like Python or Java, arrays can be dynamically resized using structures like ArrayList. This involves doubling the size of the array when it becomes full, which can mitigate the fixed size issue.
Multi-dimensional Arrays: Arrays can also be multi-dimensional, like matrices, where each element is accessed using multiple indices.
Examples:

Example 1: Fixed-size array in C: int arr[10];
Example 2: Dynamic array in Python: arr = [], followed by arr.append(value) to add elements.

### 1. Inserting Elements

### Inserting at the Front

```javascript
#include <stdio.h>

void insertAtFront(int arr[], int* size, int element) {
    for (int i = *size; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = element;
    (*size)++;
}

int main() {
    int arr[10] = {2, 3, 4, 5};
    int size = 4;
    int element = 1;

    insertAtFront(arr, &size, element);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

### Inserting at the Back

```javascript
#include <stdio.h>

void insertAtBack(int arr[], int* size, int element) {
    arr[*size] = element;
    (*size)++;
}

int main() {
    int arr[10] = {1, 2, 3, 4};
    int size = 4;
    int element = 5;

    insertAtBack(arr, &size, element);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

### Inserting in the Middle

```javascript
#include <stdio.h>

void insertAtMiddle(int arr[], int* size, int element, int position) {
    for (int i = *size; i > position; i--) {
        arr[i] = arr[i - 1];
    }
    arr[position] = element;
    (*size)++;
}

int main() {
    int arr[10] = {1, 2, 4, 5};
    int size = 4;
    int element = 3;
    int position = 2;

    insertAtMiddle(arr, &size, element, position);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

### 2. Deleting Elements

### Deleting from the Front

```javascript
#include <stdio.h>

void deleteFromFront(int arr[], int* size) {
    for (int i = 0; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*size)--;
}

int main() {
    int arr[10] = {1, 2, 3, 4, 5};
    int size = 5;

    deleteFromFront(arr, &size);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

### Deleting from the Back

```javascript
#include <stdio.h>

void deleteFromBack(int arr[], int* size) {
    (*size)--;
}

int main() {
    int arr[10] = {1, 2, 3, 4, 5};
    int size = 5;

    deleteFromBack(arr, &size);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

### Deleting from the Middle

```javascript
#include <stdio.h>

void deleteFromMiddle(int arr[], int* size, int position) {
    for (int i = position; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*size)--;
}

int main() {
    int arr[10] = {1, 2, 3, 4, 5};
    int size = 5;
    int position = 2;

    deleteFromMiddle(arr, &size, position);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

## 2. Linked Lists

### Definition:

A linked list is a data structure where each element (node) contains a value and a pointer to the next node in the sequence. There are variations like singly linked lists and doubly linked lists.

### Explanation:

Linked lists excel in scenarios where dynamic resizing is needed, as elements can be easily inserted or deleted without shifting other elements. However, they lack efficient random access since elements must be traversed sequentially. This makes them less suitable for tasks that require frequent searches or sorting. Linked lists are also relatively small in size, but they introduce overhead due to the storage of pointers.

### Additional Explanation:

Circular Linked Lists: In a circular linked list, the last node points back to the first, creating a loop. This can be useful in applications like round-robin scheduling.
Skip Lists: A skip list is a variation that allows faster search within a linked list by maintaining multiple layers of linked lists that skip over elements.
Examples:

### Example 1: Singly linked list in C

```javascript
struct Node {
    int data;
    struct Node* next;
};
```

### Example 2: Doubly linked list in C:

```javascript
struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};
```

## 3. Hash Tables

### Definition:

A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

### Explanation:

Hash tables offer average-case constant time complexity for insertion, deletion, and lookup operations, making them highly efficient for large datasets. However, the efficiency depends on the quality of the hash function and the handling of collisions. Hash tables are not suitable for tasks that require sorted data, and their size can vary greatly depending on the number of elements and the chosen load factor.

### Additional Explanation:

Open Addressing: This method handles collisions by finding another open slot within the array. Techniques include linear probing, quadratic probing, and double hashing.
Separate Chaining: This method handles collisions by maintaining a linked list at each array index, storing all elements that hash to the same index.

### Examples:

Example 1: Hash table in Python using dictionaries:

```javascript
hash_table = {"key1": "value1", "key2": "value2"}

```

Example 2: Hash table with separate chaining in C

```javascript
struct HashNode {
    int key;
    int value;
    struct HashNode* next;
};
```

## 4. Tries

### Definition:

A trie is a tree-like data structure that stores a dynamic set of strings, where the keys are usually strings. Each node represents a character of a string, and the path from the root to a node represents a prefix of the strings in the trie.

### Explanation:

Tries are efficient for tasks that involve prefix searches, such as autocomplete features. They allow fast insertion, deletion, and lookup operations based on the length of the key. However, tries can become very large, especially when storing large sets of strings, due to the number of pointers each node must maintain. Despite their space complexity, tries naturally store data in a sorted manner by key prefix.

### Additional Explanation:

Compressed Tries: These are a space-optimized version where nodes with a single child are merged to reduce the trie size.
Radix Trees: A variation of the trie where nodes can store multiple characters, further reducing the size and improving efficiency.
Examples:

### Example 1: Simple trie node in C

```javascript
struct TrieNode {
    struct TrieNode* children[26];
    bool isEndOfWord;
};
```

### Example 2: Using a trie for autocomplete


```javascript
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
```

### Summary

- Arrays: Efficient for lookup and small memory footprint but lack flexibility in size and efficient insertion/deletion.
- Linked Lists: Flexible with dynamic resizing and easy insertion/deletion, but poor at random access and sorting.
- Hash Tables: Offer fast average-case operations for insertion, deletion, and lookup but depend on a good hash function and are not space-efficient.
- Tries: Ideal for prefix-based searches with fast operations but can become very large and complex.

