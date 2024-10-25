def merge_two_list(a, b):
    c = [] 
    i = j = 0 
    while i < len(a) and j < len(b):
        if a[i] < b[j]: 
            c.append(a[i])
            i += 1 
        else:
            c.append(b[j]) 
            j += 1

    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]

    return c 

def merge_sort(array1):
    if len(array1) == 1: 
        return array1
    middle = len(array1) // 2 
    left = merge_sort(array1[:middle]) 
    right = merge_sort(array1[middle:]) 
    return merge_two_list(left, right) 


list1 = [4, 2, 9, 1, 5, 8, 3, 6, 9]
list2 = [5, 3, 8, 2, 1, 5, 7, 6, 9]
list3 = [1, 2, 3, 4, 5, 3, 5, 6, 25]
list4 = [8, 7, 6, 5, 4, 3, 2, 1, 0]
list5 = [1, 2, 3, 4, 5, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print("Дейкало Владислав, П-31, варіант 8, ЛР4")

print(merge_sort(list1))
print(merge_sort(list2))
print(merge_sort(list3))
print(merge_sort(list4))
print(merge_sort(list5))



