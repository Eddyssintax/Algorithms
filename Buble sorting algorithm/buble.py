import random

def bubble(lst):
    loops = 0
    n = len(lst)
    
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if lst[j] > lst[j + 1]:
                loops += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return loops

lst = list(range(1, 25 *4))
random.shuffle(lst)

iterations = bubble(lst)
print("Total iterations:", iterations)

