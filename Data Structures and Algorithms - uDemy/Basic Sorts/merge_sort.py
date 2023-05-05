#Made of merge and sort. Merge only merges two SORTED lists
#Break a list of length n into n 1 length lists (inherently sorted) and then merge them 2 at a time 
#Has a space of 0(n) complexity, time to break is O(logn) time to put back is O(n) therefore total time complexity is O(nlogn). Most efficient you can make a sorting algorithm

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    if i == len(list1):
        combined += list2[j:]
    else:
        combined += list1[i:]
    
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = len(my_list)//2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)



l1 = [7, 5, 3 ,1, 8, 6, 4, 2]


print(merge_sort(l1))

