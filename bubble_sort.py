"""
Bubble sort
    - repeatedly steps through the input list element by element,
    comparing the current element with the one after it, swapping their values if needed

    Time complexity: O(n^2)
    Space complexity: O(1)
"""
def bubble_sort(arr, simulation=False):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    iteration = 0
    if simulation:
        print("Iteration", iteration, ":", *arr)

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                swap(i-1, i)
                swapped = True
                if simulation:
                    iteration += 1
                    print("Iteration", iteration, ":", *arr)
    return arr



print(bubble_sort([5, 3, 9, 1], simulation=True))
