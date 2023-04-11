from sys import stdin, stdout
'''
fibo = [(1,0), (0,1)]
for _ in range(int(stdin.readline())):
    num = int(stdin.readline())
    while len(fibo) <= num:
        elem = (fibo[-1][0]+fibo[-2][0], fibo[-1][1]+fibo[-2][1])
        fibo.append(elem)
    stdout.write(str(fibo[num][0])+' '+str(fibo[num][1])+'\n')
'''
dp = [0]*100
def fibo(x):
    if x==1 or x==2:
        return 1
    if dp[x] != 0: #이미 계산되었다면
        return dp[x]
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]