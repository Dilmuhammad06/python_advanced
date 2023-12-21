import random


rand = random.randint(1, 10)
def binary_search(mylist, value):
    start_index = 0
    end_index = len(mylist) - 1
    counter = 0

    while start_index <= end_index:
        mid_point = start_index + (end_index - start_index) // 2
        mid_point_value = mylist[mid_point]
        counter += 1

        if mid_point_value == value:
            return mid_point, mid_point_value, counter
        elif value < mid_point_value:
            end_index = mid_point - 1
        else:
            start_index = mid_point + 1  # Fix here

    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], rand))
