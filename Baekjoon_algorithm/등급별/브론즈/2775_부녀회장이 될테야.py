'''
수학으로 풀려다가 당한 문제
'''
for _ in range(int(input())):
    floor = int(input())
    num = int(input())
    f = list(range(1, num+1))
    # 층수로 따지기
    for _ in range(floor):
        for i in range(1, num):
           f[i]+=f[i-1]
    print(f[-1])