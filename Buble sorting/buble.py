import time
import random

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.monotonic()
        retval = func(*args, **kwargs)
        after = time.monotonic()- before
        print(f"Function {func.__name__}: {after:05f} seconds")
        return retval
    return wrapper

@timer
def bubble(lst):
    loops = 0
    n = len(lst)
    
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if lst[j] > lst[j + 1]:
                loops += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return loops

lst = list(range(1, 25 *507))
random.shuffle(lst)

iterations = bubble(lst)
print("Total iterations:", iterations)

