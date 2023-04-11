ans=0
for _ in range(int(input())):
    group=set()
    cur_w=''
    flag=True
    for w in input():
        if w not in group:
            #그룹에 없으면
            group.add(w)
            cur_w=w
        else:
            # 그룹에 있으면
            if w==cur_w:
                pass
            else:
                flag=False
                break
    if flag:
        ans+=1
print(ans)