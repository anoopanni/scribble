arr = [1, 3, 2, 4, 5]

# Find the minimum element in the array and swap it with the first element of the array. The array keeps shrinking by 1 index until every element is sorted  

for i in range(len(arr)):

    min_i = i

    for j in range(i, len(arr)):
        if arr[j] < arr[min_i]:
            min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]

print(arr)
