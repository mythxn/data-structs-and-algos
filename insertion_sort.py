def insertion_sort(arr):
    """ Insertion Sort (stable/in-place)
            Complexity: O(n^2)
    """
    # start from 2nd element so we have a prev
    for i in range(1, len(arr)):
        cur_p = arr[i]
        prev = i - 1

        # shift prev bigger values right one step
        while prev >= 0 and cur_p < arr[prev]:
            arr[prev + 1] = arr[prev]
            prev = prev - 1

        # then place cur_p right before bigger vals start
        arr[prev + 1] = cur_p
