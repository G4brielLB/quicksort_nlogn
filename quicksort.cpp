#include <iostream>
#include <vector>

void quicksort_hoare(std::vector<int>& arr, int low, int high);
void quicksort_lamuto(std::vector<int>& arr, int low, int high);
int hoare(std::vector<int>& arr, int low, int high);
int lamuto(std::vector<int>& arr, int low, int high);

void quicksort_hoare(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivotIndex = hoare(arr, low, high);
        quicksort_hoare(arr, low, pivotIndex);
        quicksort_hoare(arr, pivotIndex + 1, high);
    }
}

int hoare(std::vector<int>& arr, int low, int high) {
    int pivot = arr[low];
    int i = low - 1;
    int j = high + 1;

    while (true) {
        do {
            i++;
        } while (arr[i] < pivot);

        do {
            j--;
        } while (arr[j] > pivot);

        if (i >= j) {
            return j;
        }

        std::swap(arr[i], arr[j]);
    }
}

void quicksort_lamuto(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivotIndex = lamuto(arr, low, high);
        quicksort_lamuto(arr, low, pivotIndex - 1);
        quicksort_lamuto(arr, pivotIndex + 1, high);
    }
}

int lamuto(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1);
    std::vector<int> R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapsort(std::vector<int>& arr) {
    int n = arr.size();

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        std::swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}


#include <fstream>
#include <chrono>
#include <numeric>
#include <cmath>

std::vector<int> read_numbers(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<int> numbers;
    int number;
    while (file >> number) {
        numbers.push_back(number);
    }
    return numbers;
}

double calculate_mean(const std::vector<double>& times) {
    return std::accumulate(times.begin(), times.end(), 0.0) / times.size();
}

double calculate_stddev(const std::vector<double>& times, double mean) {
    double sum = 0.0;
    for (double time : times) {
        sum += (time - mean) * (time - mean);
    }
    return std::sqrt(sum / times.size());
}

void print_results(const std::string& algorithm, const std::vector<double>& times) {
    double mean = calculate_mean(times);
    double stddev = calculate_stddev(times, mean);
    std::cout << algorithm << " - Mean time: " << mean << " ms, Stddev: " << stddev << " ms" << std::endl;
}

int main() {
    std::vector<int> numbers = read_numbers("/Users/gabriellopesbastos/Documents/Programming/quicksort_nlogn/lists/numbers200000.txt");
    std::vector<double> times;

    for (int i = 0; i < 5; ++i) {
        std::vector<int> arr = numbers;
        auto start = std::chrono::high_resolution_clock::now();
        quicksort_hoare(arr, 0, arr.size() - 1);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> duration = end - start;
        times.push_back(duration.count());
    }
    print_results("Quicksort Hoare", times);

    times.clear();
    for (int i = 0; i < 5; ++i) {
        std::vector<int> arr = numbers;
        auto start = std::chrono::high_resolution_clock::now();
        quicksort_lamuto(arr, 0, arr.size() - 1);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> duration = end - start;
        times.push_back(duration.count());
    }
    print_results("Quicksort Lamuto", times);

    times.clear();
    for (int i = 0; i < 5; ++i) {
        std::vector<int> arr = numbers;
        auto start = std::chrono::high_resolution_clock::now();
        merge_sort(arr, 0, arr.size() - 1);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> duration = end - start;
        times.push_back(duration.count());
    }
    print_results("Merge Sort", times);

    times.clear();
    for (int i = 0; i < 5; ++i) {
        std::vector<int> arr = numbers;
        auto start = std::chrono::high_resolution_clock::now();
        heapsort(arr);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> duration = end - start;
        times.push_back(duration.count());
    }
    print_results("Heap Sort", times);

    return 0;
}
