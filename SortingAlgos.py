import time
import random

def bubble_sort(arr):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def merge_sort(arr):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def quick_sort(arr):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def heap_sort(arr):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def counting_sort(arr):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def radix_sort(arr):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def bucket_sort(arr):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay 

def quick_select(arr, kth):
    arr.sort() # TODO Replace with real algo"""
    time.sleep(random.randint(1,100)/1000) # a sleep timer to simulate algo delay
    return  arr[kth] #the kth element # TODO this result should come from the quick_select algo itself


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




    