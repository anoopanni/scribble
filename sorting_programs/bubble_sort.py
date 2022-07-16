arr = [1, 3, 2, 4, 5]
count = 0
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            count += 1
            print("swappping {} and {}".format(arr[j], arr[j+1]))
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
print("number of times swappped: ", count)
