import time

cache = dict()  # [n, fib(n)]

def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

def fibc(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if not n in cache:
        tmp = fibc(n - 1) + fibc(n - 2)
        cache[n] = tmp
        return tmp

    return cache[n]

x = 25

start = time.time()
fib(x)
print('{:.7f} secs cache'.format(round(time.time() - start, 10)))

start = time.time()
fibc(x)
print('{:.7f} secs cache'.format(round(time.time() - start, 10)))