def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)


def fib(n):
    # 0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)
