def fib_num(num):
    lst = [0,1]

    for x in range(2 , num):
        y = lst[-1] + lst[-2]
        lst.append(y)

    return lst

print(fib_num(8))