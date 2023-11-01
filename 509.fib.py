def fib(n: int) -> int:
    f0, f1 = 0, 1
    if n == 0:
        return f0
    if n == 1:
        return f1
    for _ in range(1, n):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


print(fib(4))
