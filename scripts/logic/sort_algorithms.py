from algorithm_complexity import performance

# Sort Algorithms


# @performance
def bubble_sort(arr):
    '''
    Bubble Sort
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for _ in range(len(arr)):  # compare n times
        for j in range(len(arr) - 1):  # iterate over the array
            # if the element is greater than the next element, swap them
            if arr[j] > arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# @performance
def selection_sort(arr):
    '''
    Selection Sort
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for i in range(len(arr)):  # iterate over the array
        min_index = i  # set the minimum index to the current index
        for j in range(i + 1, len(arr)):  # [lowest_sorted_index, arr_length]
            # if the element is smaller than the current minimum element, set the minimum index to the current index
            if arr[j] < arr[min_index]: min_index = j
        # swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# @performance
def insertion_sort(arr):
    '''
    Insertion Sort
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for i in range(1, len(arr)):  # iterate over the array
        current = arr[i]  # set the current element to the current index
        j = i - 1  # set the previous index
        while j >= 0 and arr[j] > current:  # while the previous index is greater than or equal to 0 and the previous element is greater than the current element
            arr[j + 1] = arr[j]  # set the next element to the previous element
            j -= 1  # decrement the previous index
        arr[j + 1] = current  # set the next element to the current element
    return arr


# ? Devide and Conquer Algorithms ---------------------------------------------------------------------------------------------


# @performance
def merge_sort(arr):
    '''
    Merge Sort
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    '''
    if len(arr) > 1:  # base case
        mid = len(arr) // 2  # find the middle of the array
        left = arr[:mid]  # divide the array elements into 2 halves
        right = arr[mid:]  # divide the array elements into 2 halves
        # sort the 2 halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0  # iterators for the left, right and main arrays
        while i < len(left) and j < len(right):  # while there are still elements in the left and right arrays
            if left[i] < right[j]:  # if the left element is smaller than the right element
                arr[k] = left[i]  # add the left element to the main array
                i += 1  # increment the left iterator
            else:  # if the right element is smaller than the left element
                arr[k] = right[j]  # add the right element to the main array
                j += 1  # increment the right iterator
            k += 1  # increment the main array iterator

        while i < len(left):  # if there are still elements in the left array
            arr[k] = left[i]  # add the left element to the main array
            i += 1  # increment the left iterator
            k += 1  # increment the main array iterator

        while j < len(right):  # if there are still elements in the right array
            arr[k] = right[j]  # add the right element to the main array
            j += 1  # increment the right iterator
            k += 1  # increment the main array iterator

    return arr  # return the sorted array


# @performance
def quick_sort(arr):
    '''
    Quick Sort
    Time Complexity: O(n log n)
    Space Complexity: O(log n)
    '''
    if len(arr) > 1:  # base case
        pivot = arr[0]  # set the pivot to the first element
        left = []  # list for the elements smaller than the pivot
        right = []  # list for the elements greater than the pivot
        for i in range(1, len(arr)):  # iterate over the array
            if arr[i] < pivot:  # if the element is smaller than the pivot
                left.append(arr[i])  # add the element to the left list
            else:  # if the element is greater than the pivot
                right.append(arr[i])  # add the element to the right list
        # sort the left and right lists
        left = quick_sort(left)
        right = quick_sort(right)
        # combine the sorted left, pivot and right lists
        arr = left + [pivot] + right
    return arr


# @performance
def shell_sort(arr):
    '''
    Shell Sort
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    '''
    gap = len(arr) // 2  # find the gap
    while gap > 0:  # while the gap is greater than 0
        for i in range(gap, len(arr)):  # iterate over the array
            current = arr[i]  # set the current element to the current index
            j = i  # set the previous index
            while j >= gap and arr[j - gap] > current:  # while the previous index is greater than or equal to the gap and the previous element is greater than the current element
                arr[j] = arr[j - gap]  # set the next element to the previous element
                j -= gap  # decrement the previous index
            arr[j] = current  # set the next element to the current element
        gap //= 2  # decrement the gap
    return arr


# @performance
def heap_sort(arr):
    '''
    Heap Sort
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    '''


# @performance
def radix_sort(arr):
    '''
    Radix Sort
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    '''
    pass


#! TODO: Dijkstra's, Kruskal's, Prim's, Bellman-Ford, Floyd-Warshall, A* algorithms...


if __name__ == '__main__':
    import random
    rand_list = [random.randint(0, 100) for _ in range(100)]
    print(rand_list,'\n')

    # print('Bubble Sort:', bubble_sort(rand_list))
    print('Selection Sort:', selection_sort(rand_list))
    # print('Insertion Sort:', insertion_sort(rand_list))
    # print('Merge Sort:', merge_sort(rand_list))
    # print('Quick Sort:', quick_sort(rand_list))
    # print('Shell Sort:', shell_sort(rand_list))
