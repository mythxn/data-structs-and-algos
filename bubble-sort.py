def bubble_sort(arr):
    size = len(arr)

    # Θ(n^2)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                swapped = True
        if not swapped:
            break
