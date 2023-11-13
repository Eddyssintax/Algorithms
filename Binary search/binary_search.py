#lst must be sorted!
def bin(lst, y):
    low = 0
    high = len(lst) - 1

    while low < high: # updating low n high after every iteration while 0 < 9
        mid = (low + high) // 2 # mid = 4
        if lst[mid] < y:  # lst[4] < y = 8
            low = mid + 1  # lst[4+1]..
        elif mid > y:  # lst[4] > y = 8
            high = mid - 1  # lst[4 - 1]
        else:
            return mid  # mid == y
    return None  # y not in lst


print(bin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
