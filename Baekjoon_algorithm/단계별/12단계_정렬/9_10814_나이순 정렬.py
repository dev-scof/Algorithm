from sys import stdin
N=int(stdin.readline())
client=[]
for i in range(N):
    client.append(tuple(input().split()))
for age, name in sorted(client, key=lambda x:int(x[0])):
    print(age, name)

