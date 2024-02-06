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

#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

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

#merge sort
def merge_Sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge_Sort(L)
        merge_Sort(R)
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

#heap sort 1/2
def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
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

#heap sort 2/2
def heapSort(arr):
    N = len(arr)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    
    return arr

#counting sort
def countingSort(array, place):
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

# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
    return array

#bucket sort
def bucketSort(array):
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


#generate a randomized array of size between 20-50, with integers between 1-1000
def generate_randomized_array():
    size = random.randint(20, 50)
    random_array = [random.randint(1, 1000) for _ in range(size)]
    return random_array

def main():
    try:
        arr = generate_randomized_array()
        arr2, arr3, arr4, arr5, arr6, arr7, arr8 = [arr.copy() for _ in range(7)]

        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        total_time_bubble = end_time - start_time

        start_time = time.time()
        quick_sort(arr2, 0, len(arr2) - 1)
        end_time = time.time()
        total_time_quick = end_time - start_time

        start_time = time.time()
        insertion_sort(arr3)
        end_time = time.time()
        total_time_insertion = end_time - start_time

        start_time = time.time()
        merge_Sort(arr4)
        end_time = time.time()
        total_time_merge = end_time - start_time

        start_time = time.time()
        heapSort(arr5)
        end_time = time.time()
        total_time_heap = end_time - start_time

        start_time = time.time()
        countingSort(arr6, 1)
        end_time = time.time()
        total_time_counting = end_time - start_time

        start_time = time.time()
        radixSort(arr7)
        end_time = time.time()
        total_time_radix = end_time - start_time

        start_time = time.time()
        bucketSort(arr8)
        end_time = time.time()
        total_time_bucket = end_time - start_time

        print(f"Average Time taken for Bubble Sort: {1000000 * total_time_bubble:.4f} microseconds")
        print("Bubble Sorted Array:", bubble_sort(arr))

        print(f"\nAverage Time taken for Quick Sort: {1000000 * total_time_quick:.4f} microseconds")
        print("Quick Sorted Array:", quick_sort(arr2, 0, len(arr2) - 1))

        print(f"\nAverage Time taken for Insertion Sort: {1000000 * total_time_insertion:.4f} microseconds")
        print("Insertion Sorted Array:", insertion_sort(arr3))

        print(f"\nAverage Time taken for Merge Sort: {1000000 * total_time_merge:.4f} microseconds")
        print("Merge Sorted Array:", merge_Sort(arr4))

        print(f"\nAverage Time taken for Heap Sort: {1000000 * total_time_heap:.4f} microseconds")
        print("Heap Sorted Array:", heapSort(arr5))

        print(f"\nAverage Time taken for Counting Sort: {1000000 * total_time_counting:.4f} microseconds")
        print("Counting Sorted Array:", countingSort(arr6, 1))

        print(f"\nAverage Time taken for Radix Sort: {1000000 * total_time_radix:.4f} microseconds")
        print("Radix Sorted Array:", radixSort(arr7))

        print(f"\nAverage Time taken for Bucket Sort: {1000000 * total_time_bucket:.4f} microseconds")
        print("Bucket Sorted Array:", bucketSort(arr8))


    except ValueError:
        print("Invalid Entry")

if __name__ == "__main__":
    main()
