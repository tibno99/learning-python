#Selection sort goes through value by value and only moves the value down if the item before it is higher than it
#O(n^2)
#Best case is sorted or mostly sorted lists its basically O(n)

def insertion_sort(list_):
    for i in range(1, len(list_)):
        j = i - 1
        temp = list_[i]
        while temp < list_[j] and j > -1:
            list_[j + 1] = list_[j]
            list_[j] = temp
            j -= 1
    return list_


ex_list = [5, 4, 7, 0, 1, 2, 3, 6]
print(ex_list)
print(insertion_sort(ex_list))