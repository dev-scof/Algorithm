user=[]
for _ in range(int(input())):
    user.append(tuple(input().split()))
user.sort(key=lambda x:int(x[0]))
for us in user:
    print(' '.join(map(str, us)))