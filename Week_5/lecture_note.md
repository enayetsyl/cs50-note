### Introduction

This note focuses on the concepts of various data structures, including abstract data types, stacks, queues, and linked lists, as discussed in Lecture 5 of CS50. It also touches upon advanced structures like binary search trees, dictionaries, hashing, and tries, emphasizing the importance of memory management and efficient problem-solving.

### Index
1. Abstract Data Types (ADT)
2. Queues
  - Enqueue and Dequeue
  - FIFO
  - Use Case
  - Push & Pop
  - Implementation
3. Stacks
  - LIFO
  - Push and Pop
  - Use Case
4. Problem with Fixed-Sized Array
5. Array Limitations
6. Linked Lists
  - Definition
  - Explanation
  - Appending
  - Prepending
  - Sorted Linked List
  - Implementation
7. Trees
  - Definition
  - Explanation
  - Binary Search Trees
  - Implementation
8. Dictionaries
9. Hashing
10. Tries
11. Memory Allocation in C

## Abstract Data Types (ADT)

### Definition:

Abstract Data Types (ADTs) are data structures that provide specific properties and characteristics. The implementation details of these structures are hidden from the user, allowing for flexibility in how they are realized in code.

### Explanation:

ADTs include structures like queues and stacks. They define the behavior and properties of the data structures without specifying how they are implemented. This abstraction allows programmers to choose the most efficient implementation method based on their specific needs and constraints.

### Additional Explanations and Examples:

1. Example: A list ADT may define operations like add, remove, and search, without specifying if the list is implemented as an array or linked list.
2. Example: The queue ADT defines enqueue and dequeue operations, leaving the choice of using an array or linked list to the programmer.

## Queues

### Definition:

A queue is a data structure that follows the First-In-First-Out (FIFO) principle, where the first element added is the first one to be removed.

### Explanation:

Queues are used in scenarios where order of processing is important, such as task scheduling and breadth-first search algorithms. They support operations like enqueue (adding an element) and dequeue (removing an element).

### Enqueue and Dequeue:

  - Enqueue: Adding an element to the end of the queue.
  - Dequeue: Removing an element from the front of the queue.

### FIFO:

Queues follow the First-In-First-Out (FIFO) principle, where the first element added is the first one to be removed.

### Use Case:

Queues are used in scenarios where order of processing is important, such as task scheduling and breadth-first search algorithms.

### Push & Pop:

In the context of stacks, push and pop are analogous to enqueue and dequeue in queues but follow LIFO order.

### Implementation:

```javascript
typedef struct {
    int data[50];
    int front;
    int rear;
    int size;
} Queue;

void enqueue(Queue *q, int value) {
    if (q->size < 50) {
        q->data[q->rear++] = value;
        q->size++;
    }
}

int dequeue(Queue *q) {
    if (q->size > 0) {
        int value = q->data[q->front++];
        q->size--;
        return value;
    }
    return -1; // Queue is empty
}
```

### Additional Explanations and Examples:

1. Real-World Example: People standing in line at a store. The first person in line is the first to be served.
2. Alternative Implementation: Implementing a queue using a linked list for dynamic sizing.

## Stacks

### Definition:

A stack is a data structure that follows the Last-In-First-Out (LIFO) principle, where the last element added is the first one to be removed.

### Explanation:

Stacks are used in scenarios requiring reverse processing order, such as function call management and depth-first search algorithms. They support operations like push (adding an element) and pop (removing an element).

### Push and Pop:

Stacks support two main operations:
- Push: Adding an element to the top of the stack.
- Pop: Removing an element from the top of the stack.

### LIFO:

Stacks follow the Last-In-First-Out (LIFO) principle, where the last element added is the first one to be removed.

### Use Case:

Stacks are used in scenarios requiring reverse processing order, such as function call management and depth-first search algorithms.

### Implementation:

```javascript
typedef struct {
    int data[50];
    int top;
} Stack;

void push(Stack *s, int value) {
    if (s->top < 50) {
        s->data[s->top++] = value;
    }
}

int pop(Stack *s) {
    if (s->top > 0) {
        return s->data[--s->top];
    }
    return -1; // Stack is empty
}
```

### Additional Explanations and Examples:

1. Real-World Example: Plates stacked in a cafeteria. The last plate placed on the stack is the first one to be taken.
2. Alternative Implementation: Implementing a stack using a linked list to handle dynamic resizing.

## Problem with Fixed-Sized Array

### Explanation:

Arrays have a fixed size, which can be limiting when the number of elements exceeds the allocated capacity. Resizing an array involves creating a new, larger array and copying existing elements, which is inefficient.

### Example Problem:

If an array of size 3 needs to store a fourth element, it requires creating a new array of size 4 and copying the existing elements, leading to performance overhead.

## Array Limitations

### Definition:

Arrays are a fixed-size, contiguous memory data structure for storing elements of the same type.

### Explanation:

While arrays are simple and efficient for indexing, their fixed size can be limiting. When the array's capacity is exceeded, a new larger array must be allocated and existing elements copied over, which is time-consuming and inefficient.

### Code Example:

```javascript
int* resizeArray(int *array, int oldSize, int newSize) {
    int *newArray = (int*)malloc(newSize * sizeof(int));
    for (int i = 0; i < oldSize; i++) {
        newArray[i] = array[i];
    }
    free(array);
    return newArray;
}
```

### Additional Explanations and Examples:

1. Dynamic Arrays: Arrays that automatically resize themselves when the capacity is exceeded, such as std::vector in C++.
2. Memory Overhead: Allocating more memory than needed can lead to wasted space, while allocating too little requires frequent resizing.

## Linked Lists

### Definition:

A linked list is a data structure consisting of nodes, where each node contains a value and a pointer to the next node in the sequence.

### Explanation:

Linked lists allow for dynamic memory allocation, making it easier to manage collections of elements where the size can vary. They can be singly linked (pointing to the next node) or doubly linked (pointing to both the next and previous nodes).

### Appending:

Adding a new node to the end of the linked list.

```javascript
void append(Node **head, int value) {
    Node *newNode = createNode(value);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}
```

### Prepending:

Adding a new node to the beginning of the linked list.

```javascript
void prepend(Node **head, int value) {
    Node *newNode = createNode(value);
    newNode->next = *head;
    *head = newNode;
}
```

### Sorted Linked List:

Maintaining the linked list in sorted order, adding new elements at the correct position.

```javascript
void insertSorted(Node **head, int value) {
    Node *newNode = createNode(value);
    if (*head == NULL || (*head)->data >= value) {
        newNode->next = *head;
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while (temp->next != NULL && temp->next->data < value) {
        temp = temp->next;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}
```

### Implementation:

```javascript
typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node* createNode(int value) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

void append(Node **head, int value) {
    Node *newNode = createNode(value);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

void prepend(Node **head, int value) {
    Node *newNode = createNode(value);
    newNode->next = *head;
    *head = newNode;
}

void insertSorted(Node **head, int value) {
    Node *newNode = createNode(value);
    if (*head == NULL || (*head)->data >= value) {
        newNode->next = *head;
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while (temp->next != NULL && temp->next->data < value) {
        temp = temp->next;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}
```

## Trees

### Definition:

A tree is a hierarchical data structure consisting of nodes, with a single root node and zero or more child nodes. Each node contains a value and pointers to its child nodes.

### Explanation:

Trees are used to represent hierarchical relationships and are commonly used in scenarios like file systems and organizational structures. A special type of tree, the binary search tree (BST), allows for efficient searching, insertion, and deletion of elements.

### Binary Search Trees (BST):

A tree data structure where each node has at most two children, referred to as the left child and the right child. In a BST, for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater.

### Implementation:

```javascript
typedef struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

TreeNode* createTreeNode(int value) {
    TreeNode *newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

TreeNode* insert(TreeNode *root, int value) {
    if (root == NULL) {
        return createTreeNode(value);
    }
    if (value < root->data) {
        root->left = insert(root->left, value);
    } else {
        root->right = insert(root->right, value);
    }
    return root;
}
```

## Dictionaries

### Definition:

Dictionaries are data structures that store key-value pairs, allowing efficient retrieval, insertion, and deletion of values based on their keys.

### Explanation:

Dictionaries use a hash function to map keys to indices in an array, enabling quick access to the values associated with those keys.

### Example:

In Python, dictionaries are implemented using hash tables, providing average-case O(1) time complexity for lookup, insertion, and deletion.

## Hashing

### Definition:

Hashing is the process of converting a key into a fixed-size integer, which is used as an index in a hash table.

### Explanation:

A good hash function distributes keys uniformly across the hash table, minimizing collisions and ensuring efficient data retrieval.

### Example:

A simple hash function for strings:

```javascript
unsigned int hash(const char *str) {
    unsigned int hash = 0;
    while (*str) {
        hash = (hash << 5) + *str++;
    }
    return hash % TABLE_SIZE;
}
```

## Tries

### Definition:

A trie, also known as a prefix tree, is a tree-like data structure used to store a dynamic set of strings where the keys are usually strings.

### Explanation:

Tries are used for tasks like autocomplete and spell checking, where quick access to words with common prefixes is essential.

### Example:

```javascript
typedef struct TrieNode {
    struct TrieNode *children[26];
    bool isEndOfWord;
} TrieNode;

TrieNode* createTrieNode() {
    TrieNode *node = (TrieNode*)malloc(sizeof(TrieNode));
    node->isEndOfWord = false;
    for (int i = 0; i < 26; i++) {
        node->children[i] = NULL;
    }
    return node;
}

void insert(TrieNode *root, const char *key) {
    TrieNode *node = root;
    while (*key) {
        if (node->children[*key - 'a'] == NULL) {
            node->children[*key - 'a'] = createTrieNode();
        }
        node = node->children[*key - 'a'];
        key++;
    }
    node->isEndOfWord = true;
}
```

## Memory Allocation in C

### Definition:

Memory allocation in C involves dynamically requesting and freeing memory during program execution using functions like malloc, calloc, and free.

### Explanation:

Dynamic memory allocation allows for flexible memory management, especially for data structures whose size may change during execution. Proper memory management is crucial to prevent leaks and ensure efficient use of resources.

### Code Example:

```javascript
int* allocateMemory(int size) {
    int *array = (int*)malloc(size * sizeof(int));
    if (array == NULL) {
        // Handle memory allocation failure
        exit(1);
    }
    return array;
}

void freeMemory(int *array) {
    free(array);
}
```

### Additional Explanations and Examples:

1. Memory Leaks: Occur when dynamically allocated memory is not freed, leading to wasted memory resources.
2. Double Free Error: Occurs when the same memory is freed multiple times, potentially causing program crashes and undefined behavior.

## Summary

1. Abstract Data Types (ADT): Define the behavior and properties of data structures without specifying implementation details.
2. Queues: FIFO data structure used in scenarios requiring order processing, with operations like enqueue and dequeue.
3. Stacks: LIFO data structure used in scenarios requiring reverse order processing, with operations like push and pop.
4. Problem with Fixed-Sized Array: Fixed size can lead to inefficiencies and the need for resizing.
5. Array Limitations: Fixed size and inefficiency in resizing when capacity is exceeded.
6. Linked Lists: Dynamic data structure consisting of nodes, allowing flexible memory allocation and management.
7. Trees (Binary Search Trees): Tree data structure for efficient searching, insertion, and deletion of elements.
8. Dictionaries: Store key-value pairs for efficient retrieval and management.
9. Hashing: Process of converting keys to fixed-size integers for efficient indexing in hash tables.
10. Tries: Tree-like data structure for efficient storage and retrieval of strings with common prefixes.
11. Memory Allocation in C: Essential for dynamic memory management, preventing leaks and ensuring efficient resource use.