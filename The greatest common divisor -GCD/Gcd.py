def gcd(a , b):

    while b:
        a, b = b, a % b
        print( a , b)

gcd(2982,482)
            