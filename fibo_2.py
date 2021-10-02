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


if __name__ == '__main__':
    n = int(input("何番目のフィボナッチ数までを計算しますか？"))
    for _ in range(n+1):
        print(fibo_2(_))
