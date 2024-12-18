import time
import random

# Quick Sort using Lomuto partition
def quicksort_lomuto(arr, low, high):
    if low < high:
        p = lomuto_partition(arr, low, high)
        quicksort_lomuto(arr, low, p - 1)
        quicksort_lomuto(arr, p + 1, high)

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort using Hoare partition
def quicksort_hoare(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        quicksort_hoare(arr, low, p)
        quicksort_hoare(arr, p + 1, high)

def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

# Performance comparison
def compare_performance(array_size, num_tests):
    lomuto_times = []
    hoare_times = []

    for _ in range(num_tests):
        # Generate a random array
        arr = [random.randint(0, 10000) for _ in range(array_size)]

        # Test Lomuto partition
        arr_copy = arr[:]
        start = time.time()
        quicksort_lomuto(arr_copy, 0, len(arr_copy) - 1)
        end = time.time()
        lomuto_times.append(end - start)
        verify_sorted(arr_copy)

        # Test Hoare partition
        arr_copy = arr[:]
        start = time.time()
        quicksort_hoare(arr_copy, 0, len(arr_copy) - 1)
        end = time.time()
        hoare_times.append(end - start)
        verify_sorted(arr_copy)

    # Calculate average times
    avg_lomuto_time = sum(lomuto_times) / num_tests
    avg_hoare_time = sum(hoare_times) / num_tests

    avg_lomuto_time *= 1000  # Convert to milliseconds
    avg_hoare_time *= 1000    # Convert to milliseconds

    print(f"Array size: {array_size}, Tests: {num_tests}")
    print(f"Lomuto average time: {avg_lomuto_time:.6f} seconds")
    print(f"Hoare average time: {avg_hoare_time:.6f} seconds")

def verify_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print(f"Array is not sorted at index {i}")
            return False
    return True

# Example usage
if __name__ == "__main__":
    array_size = 10000  # Size of the array
    num_tests = 100     # Number of tests to average
    compare_performance(array_size, num_tests)
    

