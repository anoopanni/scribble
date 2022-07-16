arr = [5, 10, 4, 2, 1, 8]

# for i in range(len(arr)-1):

#     j = i

#     while j > 0:
#         if arr[j] > arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
#         j-=1
# print(arr)


# Important thing is the key which starts from i+1, Figure out the correct position in the sorted space for the key to be inserted. Keep moving the elements to the right until you find the right spot for the key.

for i in range(1, len(arr)):

    key = arr[i]

    j = i-1

    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print(arr)
