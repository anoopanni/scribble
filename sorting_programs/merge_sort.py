
def merge(arr, l, m, r):

    n1, n2 = m-l+1, r-m

    L = []
    R = []

    for i in range(n1):
        L.append(arr[i+l])

    for i in range(n2):
        R.append(arr[i+m+1])

    i, j, k = 0, 0, l

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def split(arr, l, r):

    if l < r:
        mid = (l + r) // 2

        split(arr, l, mid)
        split(arr, mid+1, r)

        merge(arr, l, mid, r)


arr = [4, 60, 20, 100, 50]


split(arr, 0, len(arr)-1)


print(arr)
