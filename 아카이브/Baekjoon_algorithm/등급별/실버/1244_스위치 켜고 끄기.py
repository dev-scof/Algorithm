n = int(input())
switches = list(map(int, input().split()))
for _ in range(int(input())):
    gender, num = map(int, input().split())
    if gender==1:
        for i in range(len(switches)):
            if (i+1)%num==0:
                switches[i] = (switches[i]+1)%2
    else:
        l_idx=r_idx=num-1
        while l_idx>0 and r_idx<len(switches)-1:
            if switches[l_idx-1]==switches[r_idx+1]:
                l_idx-=1
                r_idx+=1
            else:
                break
        for i in range(l_idx, r_idx+1):
            switches[i] = (switches[i]+1)%2

for i in range(1, n+1):
    print(switches[i-1], end = " ")
    if i % 20 == 0 :
        print()