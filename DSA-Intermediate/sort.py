my_list = [10,5,9,4,8,3,7,2,6,1]

# print(sorted(my_list))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(f"Step {i + 1}.{j + 1}: {arr}")


bubble_sort(my_list)
print("Bubble Sort:", my_list)




def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

my_list = [10, 5, 9, 4, 8, 3, 7, 2, 6, 1]
selection_sort(my_list)
print("Selection Sort:", my_list)




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_list = [10, 5, 9, 4, 8, 3, 7, 2, 6, 1]
insertion_sort(my_list)
print("Insertion Sort:", my_list)





def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

my_list = [10, 5, 9, 4, 8, 3, 7, 2, 6, 1]
merge_sort(my_list)
print("Merge Sort:", my_list)



