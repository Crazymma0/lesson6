def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

target_element = 25
index = binary_search(sorted_list, target_element)
if index != -1:
    print(f"Элемент {target_element} найен: {index}.")
else:
    print(f"Элемент {target_element} не найден.")