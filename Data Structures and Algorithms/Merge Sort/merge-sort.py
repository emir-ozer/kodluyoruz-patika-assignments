def merge_sort(input_array):
    if len(input_array) > 1:
        left_array = input_array[:len(input_array)//2]
        right_array = input_array[len(input_array)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                input_array[k] = left_array[i]
                i += 1
            else:
                input_array[k] = right_array[j]
                j += 1
            k += 1 
        while i < len(left_array):
            input_array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            input_array[k] = right_array[j]
            j += 1
            k += 1
    return input_array

print (merge_sort([16,21,11,8,12,22]))