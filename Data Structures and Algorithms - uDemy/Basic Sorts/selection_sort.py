#Selection sort is similar to bubble sort, but puts the lowest value from an index j into the current index i
def selection_sort(list_):
    for i in range(len(list_) - 1):
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j
        if i != min_index:        
            list_[i], list_[min_index] = list_[min_index], list_[i]

    return list_


ex_list = [5, 4, 7, 0, 1, 2, 3, 6]
print(ex_list)
print(selection_sort(ex_list))