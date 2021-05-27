def insertion_sort(arr):
    # Θ(n^2)
    for i in range(1, len(arr)):
        pointer = arr[i]
        j = i - 1
        while j >= 0 and pointer < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = pointer
