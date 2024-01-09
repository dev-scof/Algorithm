def fib(n):
    global recur_cnt
    if (n == 1 or n == 2):
        recur_cnt+=1
        return 1;  # 코드1
    else:
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global dp_cnt
    f = [0]*(n+1)
    f[1]=f[2]=1
    for i in range(3, n+1):
        f[i] = f[i - 1] + f[i - 2];  # 코드2
        dp_cnt+=1
    return f[n]


n = int(input())
recur_cnt=0
dp_cnt=0
fib(n)
fibonacci(n)
print(recur_cnt, dp_cnt)