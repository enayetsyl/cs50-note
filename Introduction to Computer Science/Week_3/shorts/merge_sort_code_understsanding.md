`[5, 2, 4, 6, 1, 3]`
`[2,5,4,6,1,3]`
`[2,4,5,6,1,3]`
`[2,4,5,6,1,3]`
### Code 
```javascript
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([12, 11, 13, 5, 6]))
```


# Step 1

```javascript
for 1 in (1, 6)
    key = 2
    j = 1-1 = 0
    while 0 >= 0 and 2 < 5
    array (0+1 = 1) index = 5
    j -=1 0-1 = -1 
    array (-1 + 1 = 0 index ) = 2
    arr is [2,5,4,6,1,3]
```

# Step 2

```javascript
    for 2 in rang (1,6)
        key = 4
        j = 2-1 = 1
        while 1 >=0 and 4 < 5
        arr (1+1 = 2) index  = 5
        j = 1-1 = 0
        arr ( 0 +1 = 1) index = 4
        arr is [2,4,5,6,1,3]
```

# Step 3 

```javascript
    for 3 in range (1,6)
        key = 6
        j = 3-1 = 2
        while 2 >=0 any 6 < 5
    arr is [2,4,5,6,1,3]
``` 

# Step 4

```javascript
for 4 in range (1,6)
    key = 1
    j = 4-1=3
    while 3 >=0  and 1 is < 6
        arr 3+1=4  index = 6
        j = 3-1 = 2
        arr 2+1=3 index = 1
    arr [2,4,5,1,6,3]
    while 2 >= 0 and 1 < 5
        arr 2+1 = 3 index = 5
        j 2-1 = 1
        arr 1+1 = 2 index = 1
    arr [2,4,1,5,6,3]
    while 1 >=0 and 1 < 4
        arr 1+1 = 2 index = 4
        j = 1-1 = 0
        arr 0+1= 1 index = 1
    arr [2,1,4,5,6,3]
    while 0 >= 0 and 1 < 2
        arr 0+1 = 1 index = 2
        j 0-1= -1 
        arr -1 + 1 = 0 index = 1
    arr [1,2,4,5,6,3]
    while -1 >= 0 loop break

```



grades = [85, 92, 78, 88, 90]
print(insertion_sort(grades))

def insertion_sort(array)
  for i in range(1, len(array))
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
  return array




merge sort array [12, 11, 13, 5, 6, 7]
  step 1 = [12,11,13]             [5,6,7]
  step 2 = [12] [11,13]           [5] [6,7]
  step 3 = [12] [11] [13]         [5] [6] [7] 
  step 4 = [12] [11,13]           [5] [6,7]
  step 5 = [12] [11] [13]         [5] [6] [7]
  step 6 = [12] [11,13]           [5] [6,7]
  step 7 = [11,12,13]             [5,6,7]
  step 8 = [5,6,7,11,12,13]
  step 6 = 
      while 0 < 1 and 0 < 1
        if 11 < 13
          array index 0 = 13
          j = 1
        k = 1
      while 0 < 1 and 1 < 1 false and loop break 