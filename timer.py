import time


def timer(func):
    def inner(*args, **kwargs):
        before_time = time.time()
        func(*args, **kwargs)
        after_time = time.time()
        print(f"{func.__name__} took {after_time - before_time} sec")
    return inner


@timer
def fibo_2(n):
    """
    fibonacci number caliculate
    :param n: fibonacci number of n th
    :return: fibonacci number
    """
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0

        for i in range(n-1):
            result = n_1 + n_2
            n_2 = n_1
            n_1 = result

        return result


if __name__ == "__main__":
    fibo = fibo_2(50)
    print(fibo)
