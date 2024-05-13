def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x < pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# 示例使用
array_to_sort = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(array_to_sort)
print(sorted_array)