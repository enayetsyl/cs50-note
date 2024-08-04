def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        print(f'Splitting: {arr}')
        print(f'mid: {mid}')
        print(f'left_half: {left_half}')
        print(f'right_half: {right_half}')
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            print(f'While loop: i={i}, j={j}, k={k}')
            print(f'Comparing: left_half[i]={left_half[i]} < right_half[j]={right_half[j]}')
            print(f'arr before if condition execute: {arr}')
            if left_half[i] < right_half[j]:
                print(f'Condition is True. Setting arr[{k}] = {left_half[i]}')
                arr[k] = left_half[i]
                i += 1
            else:
                print(f'Condition is False. Setting arr[{k}] = {right_half[j]}')
                arr[k] = right_half[j]
                j += 1
            k += 1
            print(f'Array after iteration: {arr}')

        while i < len(left_half):
            print(f'Copying remaining left_half: Setting arr[{k}] = {left_half[i]}')
            print(f'arr before setting new code: {arr}')
            arr[k] = left_half[i]
            i += 1
            k += 1
            print(f'Array after copying left_half: {arr}')

        while j < len(right_half):
            print(f'Copying remaining right_half: Setting arr[{k}] = {right_half[j]}')
            print(f'arr before setting new code: {arr}')
            arr[k] = right_half[j]
            j += 1
            k += 1
            print(f'Array after copying right_half: {arr}')

        print(f'Merged: {arr}')

# Example array
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
