def recursive_fibo(a, b, n):
    if n==0:
        return a
    t = a
    a = b
    b = b+t
    return recursive_fibo(a, b, n-1)
n = int(input())
print(recursive_fibo(0, 1, n))
