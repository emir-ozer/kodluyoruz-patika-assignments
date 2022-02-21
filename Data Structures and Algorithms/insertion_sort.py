from operator import index


def insertion_sort(input_list):
    index = range(1, len(input_list))
    for i in index:
        sorting = input_list[i]

        while input_list[i-1] > sorting and i>0:
            input_list[i], input_list[i-1] = input_list[i-1], input_list[i]
            i = i -1
    return input_list

print(insertion_sort([22,27,16,2,18,6]))      
