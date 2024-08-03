## Introduction
Linear search is a fundamental algorithm used to find an element within an array. This note will explain the linear search algorithm, including its implementation, best and worst-case scenarios, and its time complexity.

## Index
1. Definition of Linear Search
2. Implementation of Linear Search
3. Best and Worst Case Scenarios
4. Time Complexity of Linear Search

## Definition of Linear Search

Linear search is a straightforward algorithm used to find a specific element in an array by checking each element sequentially from the start to the end of the array.

## Implementation of Linear Search

The linear search algorithm involves iterating through the array elements one by one until the desired element is found or the end of the array is reached. Here's the pseudocode:

```javascript
function linearSearch(array, target):
    for each element in array:
        if element == target:
            return true
    return false
```
### Example:

To find the number 9 in the array [11, 23, 35, 9, 42], the algorithm checks each element starting from 11, then 23, then 35, until it finds 9.

### Additional Example:

Searching for the number 7 in the array [3, 5, 7, 9, 11]:

1. Start with 3 (not 7), move to the next element.
2. Check 5 (not 7), move to the next element.
3. Check 7 (found 7), stop the search.

### Additional Example:

Searching for the number 8 in the array [2, 4, 6, 8, 10]:

1. Start with 2 (not 8), move to the next element.
2. Check 4 (not 8), move to the next element.
3. Check 6 (not 8), move to the next element.
4. Check 8 (found 8), stop the search.

## Best and Worst Case Scenarios

### Best Case Scenario
In the best case scenario, the target element we are searching for is located at the very beginning of the array. This means that the algorithm only needs to perform one comparison to find the element. The steps are as follows:

1. Start with the first element in the array.
2. Compare the first element with the target element.
3. If they are equal, the search is complete.

### Example:
Let's say we are searching for the number 5 in the array [5, 12, 7, 3, 9].

- The algorithm checks the first element (5).
- Since 5 is the target element, the search stops immediately.

### Best Case Time Complexity:

- The time complexity for the best case scenario is Ω(1), which means that the algorithm completes in constant time, regardless of the size of the array. This is because it only needs to check one element.

### Worst Case Scenario

In the worst case scenario, the target element is either at the very end of the array or not present in the array at all. This requires the algorithm to check every element in the array before concluding the search. The steps are as follows:

1. Start with the first element in the array.
2. Compare the current element with the target element.
3. If they are not equal, move to the next element.
4. Repeat steps 2 and 3 until either the target element is found or the end of the array is reached.

### Example 1:
Searching for the number 9 in the array [2, 4, 6, 8, 10, 12, 14, 16, 18, 9].

- The algorithm checks each element: 2, 4, 6, 8, 10, 12, 14, 16, 18.
- The last element (9) matches the target element, so the search stops.

### Example 2:
Searching for the number 50 in the array [1, 3, 5, 7, 9, 11, 13, 15].

- The algorithm checks each element: 1, 3, 5, 7, 9, 11, 13, 15.
- Since 50 is not in the array, the search concludes after checking all elements.

### Worst Case Time Complexity:

- The time complexity for the worst case scenario is O(n), where n is the number of elements in the array. This means that the runtime grows linearly with the size of the array, as each element must be checked.

## Time Complexity of Linear Search
Time complexity is a way to describe the efficiency of an algorithm in terms of the amount of time it takes to complete as a function of the size of the input.

### Worst Case Time Complexity: O(n)

- In the worst case, the algorithm needs to check every element in the array to find the target element or determine that it is not present.
- If the array has n elements, the algorithm performs n comparisons.
- Thus, the time complexity is O(n).

### Best Case Time Complexity: Ω(1)

- In the best case, the target element is found at the first position in the array.
- The algorithm only performs one comparison.
- Thus, the time complexity is Ω(1), indicating constant time.

### Average Case Time Complexity: Θ(n)
- On average, the target element might be expected to be somewhere in the middle of the array.
- Therefore, the average case time complexity is also linear, or Θ(n).

### Detailed Explanation of Time Complexity Notation:

- O(n): This Big-O notation describes an upper bound on the time complexity, indicating the maximum amount of time an algorithm can take. For linear search, in the worst case, this means iterating through all n elements.

- Ω(1): This Omega notation describes a lower bound on the time complexity, indicating the minimum amount of time an algorithm will take. For linear search, in the best case, this means finding the element immediately.

- Θ(n): This Theta notation describes a tight bound on the time complexity, indicating that the algorithm's time complexity is both upper and lower bounded by the same function. For linear search, this means that on average, the algorithm will take time proportional to the number of elements n.

## Summary

- Definition of Linear Search: Linear search is a method of finding an element in an array by checking each element sequentially.
- Implementation of Linear Search: Iterate through each element in the array until the target element is found or the end of the array is reached.
- Best and Worst Case Scenarios: Best case occurs when the target is at the start of the array, and the worst case occurs when the target is at the end or not present at all.
- Time Complexity of Linear Search: The worst case is O(n) and the best case is Ω(1).

By understanding these aspects of linear search, one can appreciate its simplicity and applicability in various scenarios despite its inefficiency in larger datasets.

