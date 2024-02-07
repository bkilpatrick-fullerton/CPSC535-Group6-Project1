import time
import random

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i <len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j+= 1
            k += 1
        while i<len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j<len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

# quick sort 1/2
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

#quick sort 2/2
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi +1, high)
    return arr
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

# heap sort 1/2
def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)


# heap sort 2/2
def heap_sort(arr):
    N = len(arr)

    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # One by one extract elements
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10  # Assuming decimal digits (0-9)

    # Calculate count of elements at the specified place
    for i in range(size):
        index = (array[i] // place) % 10
        count[index] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = (array[i] // place) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back into the original array
    for i in range(size):
        array[i] = output[i]

    return array
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def radix_sort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10
    return array
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def bucket_sort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(j / 100)  # Adjusted for a range of 1-1000
        if index_b >= len(bucket):
            index_b = len(bucket) - 1
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1

    return array
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay

def partition(a, left, right):
    # This gets an index, not a value:
    pivotindex = random.randint(left, right)  # allow right to be selected
    pivot = a[pivotindex]  # this is the pivot value
    # move the value out of the way
    a[right], a[pivotindex] = a[pivotindex], a[right]
    i = left - 1
    for j in range(left, right):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[right] = a[right], a[i+1]
    return i + 1

def quick_select(a, k, left, right):
    if left == right:
        return a[left]
    q = partition(a, left, right)
    i = q - left + 1
    if k == i:
        return a[q]  # this is the element you want to return
    if k < i:
        return quick_select(a, k, left, q - 1)
    else:
        return quick_select(a, k - i, q + 1, right)
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay



def main():
    """example of creating building a uint test into a module (Note this function wont run if imported by another file (like the GUI))"""
    TEST_LIST = [30, 59, 3, 28, 99, 4]
    print("Reference List:")
    print(f"{TEST_LIST}\n")

    input_list = TEST_LIST[:]
    exec_time = bubble_sort(input_list)
    print("bubble_sort")
    print(f"{input_list}")
    print(f"exec_time: {exec_time}ms\n")

    input_list = TEST_LIST[:]
    exec_time = merge_sort(input_list)
    print("merge_sort")
    print(f"{input_list}")
    print(f"exec_time: {exec_time}ms\n")

if __name__ == "__main__":
    main()




    
