def recur_fibo(n1, n2, n3):
    if n3<=1:
        return n3
    return n1 + recur_fibo(n2, n1+n2, n3-1)

print(recur_fibo(0, 1, int(input())))