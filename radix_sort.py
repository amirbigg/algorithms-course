"""
Radix sort
    [121, 432, 564, 23, 1, 45, 788] => [1, 23, 45, 121, 432, 564, 788]
    Complexity: O(nk + n) -- n is the size of input list and k is the digit length of the number
"""

def radix_search(array, simulation=False):
    position = 1
    max_number = max(array)
    iteration = 0
    if simulation:
        print('Iteration', iteration, ':', *array)

    while position <= max_number:
        queue_list = [list() for _ in range(10)]

        for num in array:
            digit_number = num // position % 10
            queue_list[digit_number].append(num)

        index = 0
        for numbers in queue_list:
            for num in numbers:
                array[index] = num
                index += 1

        if simulation:
            iteration += 1
            print('Iteration', iteration, ':', *array)

        position *= 10
    return array


print(radix_search([121, 432, 564, 23, 1, 45, 788], simulation=True))
