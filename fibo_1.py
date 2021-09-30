def fibo_1(n):
    if n < 2:
        return n
    else:
        return fibo_1(n-2) + fibo_1(n-1)


print(fibo_1(6))
