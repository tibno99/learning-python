#Bubble sort compares values and switches them if the value later on is lower
def bubble_sort(list_):
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_

ex_list = [5, 4, 7, 0, 1, 2, 3, 6]
print(bubble_sort(ex_list))