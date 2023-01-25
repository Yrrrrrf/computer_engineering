import random
# Search Algorithms

def lineal_search(arr, target) -> bool:
    '''
    Lineal Search
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    for i in range(len(arr)):  # iterate over the array
        if arr[i] == target:  # if the element is in the array
            print(f'The element {target} is in the position {i}')
            return True
    return False


# Divide and Conquer Algorithms
# This method is really similar to the fixed point algorithm
def binary_search(arr, target) -> bool:
    '''
    Binary Search
    To execute this algorithm the array must be sorted. So we need to sort the array first.
    Time Complexity: O(log n)
    Space Complexity: O(n)
    '''
    left = 0  # left index
    right = len(arr) - 1  # right index
    if left > right:  return False  # if the left index is greater than the right index, the element is not in the array

    while left <= right:  # while the left index is less or equal to the right index
        # print(f'[{left}, {right}]')  # print the current range
        mid = (left + right) // 2  # middle index
        if arr[mid] == target:  # if the middle element is the target
            print(f'The element {target} is in the position {mid}')
            return True
        elif arr[mid] < target:  # if the middle element is less than the target
            left = mid + 1  # move the left index to the right
        else:
            right = mid - 1  # move the right index to the left
    return False  # if the element is not in the array


def jump_search(arr, target):
    '''
    Jump Search
    Time Complexity: O(√n)
    Space Complexity: O(1)
    '''
    pass


def interpolation_search(arr, target):
    pass

def exponential_search(arr, target):
    pass

def fibonacci_search(arr, target):
    pass

def ternary_search(arr, target):
    pass

def binary_search_tree(arr, target):
    pass

def red_black_tree(arr, target):
    pass

def b_tree(arr, target):
    pass

def b_plus_tree(arr, target):

    pass

def b_star_tree(arr, target):
    pass


if __name__ == '__main__':
    arr_size = 100
    arr = [random.randint(0, 100) for i in range(arr_size)]
    target = 8

    # Test lineal search
    # print(arr)
    # state = lineal_search(arr, target)
    # print(f'The element {target} {"is not" if not state else "is"} in the array')

    # Test binary search
    arr.sort()
    print(arr)
    state = binary_search(arr, target)
    print(f'The element {target} {"is not" if not state else "is"} in the array')

# Path: notebook\concepts\sorting_algorithms.py

# TODO: Implement fixed point algorithm