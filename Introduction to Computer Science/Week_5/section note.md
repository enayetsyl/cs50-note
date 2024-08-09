## Introduction

This note covers the key concepts and code implementations related to data structures, specifically focusing on linked lists and hash tables as discussed in a CS50 section. The note explains the structure and operations of linked lists, the fundamentals of hash tables, and the implementation of hash functions. Additionally, it touches on the efficiency trade-offs between time and memory in different data structures.

## Index

1. Linked Lists
  - Definition and Structure
  - Insertion and Deletion
  - Memory Management (Malloc and Free)
  - Practical Coding Example
2. Hash Tables
  - Definition and Structure
  - Hash Functions
  - Trade-offs Between Time and Memory
  - Practical Coding Example

## Linked Lists

### Definition and Structure

A linked list is a data structure consisting of a sequence of nodes where each node contains data and a reference (or pointer) to the next node in the sequence.

### Explanation: 

Linked lists are used when the number of elements is unknown and you want to avoid the overhead of dynamic array resizing. Each node in a linked list stores a data element (e.g., a string) and a pointer to the next node. The list ends with a node pointing to null.

### Example from Transcript:

```javascript
typedef struct node {
    char *phrase;
    struct node *next;
} node;
```

### Additional Explanation: 

Linked lists allow efficient insertion and deletion from any position in the list but have a linear time complexity for access.

### Additional Example:

```javascript
node *n = malloc(sizeof(node));
if (n == NULL) {
    return 1; // Memory allocation failed
}
n->phrase = "Hello";
n->next = NULL;
```

### Insertion and Deletion

Insertion and deletion in a linked list involve manipulating pointers to ensure that the nodes are correctly linked or unlinked.

### Explanation: 

To insert a new node, allocate memory, set the data, and adjust pointers to include the new node in the list. Deletion requires ensuring that the list's integrity is maintained by properly linking surrounding nodes.

### Example from Transcript:

```javascript
n->next = list;
list = n;
```

### Additional Explanation: 

Properly managing the next pointer is crucial during insertion and deletion to maintain the structure of the list.

### Additional Example:

```javascript
if (list != NULL) {
    node *temp = list->next;
    free(list);
    list = temp;
}
```

### Memory Management (Malloc and Free)

Memory management is crucial in linked lists to avoid memory leaks. Every malloc should eventually have a corresponding free.

### Explanation: 

In C, dynamic memory allocation is done using malloc, and it must be freed using free to avoid memory leaks.

### Example from Transcript:

```javascript
node *n = malloc(sizeof(node));
if (n == NULL) {
    return 1;
}
// Use the node...
free(n);
```

### Additional Explanation: 

Forgetting to free memory can lead to memory leaks, which in long-running programs can cause excessive memory usage.

### Additional Example:

```javascript
node *current = list;
while (current != NULL) {
    node *temp = current->next;
    free(current);
    current = temp;
}
```

## Hash Tables

### Definition and Structure

A hash table is a data structure that maps keys to values for efficient look-up using a hash function.

### Explanation: 

Hash tables use an array of linked lists where each index corresponds to a hashed key. The linked list at each index stores elements that hash to the same value.

### Example from Transcript:

```javascript
int hash_function(char *phrase) {
    return toupper(phrase[0]) - 'A';
}
```

### Additional Explanation: 

The effectiveness of a hash table depends on the hash function's ability to distribute keys uniformly across the array.

### Additional Example:

```javascript
int hash_function(char *key) {
    int hash = 0;
    while (*key) {
        hash = (hash + *key) % TABLE_SIZE;
        key++;
    }
    return hash;
}
```

### Hash Functions

A hash function is used to convert a key into an index in the hash table's array.

### Explanation: 

A good hash function minimizes collisions and ensures an even distribution of keys.

### Example from Transcript:

```javascript
int hash = toupper(key[0]) - 'A';
```

### Additional Explanation: 

Hash functions are crucial for performance. Poor hash functions can lead to clustering, reducing the efficiency of lookups.

### Additional Example:

```javascript
int simple_hash(char *str) {
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        sum += str[i];
    }
    return sum % TABLE_SIZE;
}
```

### Trade-offs Between Time and Memory

Using a hash table involves trade-offs between time complexity and memory usage.

### Explanation: 

Hash tables offer constant time complexity for insertions and lookups but require extra memory to store the array and linked lists.

### Example from Transcript: 

When implementing Speller, different solutions balance between speed and memory usage.

### Additional Explanation: 

Choosing the right data structure depends on the specific needs of the application, such as whether faster lookups or lower memory usage is prioritized.

### Additional Example:

```javascript
if (use_hash_table) {
    // Faster lookups, more memory usage
} else {
    // Slower lookups, less memory usage
}
```

## Summary

### Linked Lists: 

A linked list is a sequence of nodes where each node points to the next. Insertion and deletion require careful pointer manipulation, and memory management is crucial to avoid leaks.

### Hash Tables: 

A hash table is an array of linked lists where keys are mapped to values using a hash function. Efficient hash functions distribute keys evenly across the table, balancing time complexity and memory usage.


