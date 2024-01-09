N = int(input())
con=[]
complete=[]
for _ in range(N):
    con.append(list(map(int, input().split())))
con.sort(key=lambda x:x[0]) # 시간순 정렬
for cur in con:
    if complete==[]:
        complete.append(cur)
    elif cur[0] >= complete[-1][1] or cur[1] <= complete[-1][0]:
        complete.append(cur)
    elif cur[0] >= complete[-1][0] and cur[1] <= complete[-1][1]:
        complete.pop()
        complete.append(cur)
print(len(complete))