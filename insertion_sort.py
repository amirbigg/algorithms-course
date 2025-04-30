"""
Insertion sort
    - The Insertion Sort algorithm uses one part of the array to hold the sorted values,
    and the other part of the array to hold values that are not sorted yet.
"""

def insertion_sort(arr, simulation=False):
    iteration = 0
    if simulation:
        print('Iteration', iteration, ':', *arr)

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = cursor

        if simulation:
            iteration += 1
            print('Iteration', iteration, ':', *arr)

    return arr



print(insertion_sort([12, 8, 20, 14, 1], simulation=True))
