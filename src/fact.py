def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError
    else:
        sum = 1
        for i in range(1, n + 1):
            sum *= i
            print(sum)
        return sum