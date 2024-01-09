N = int(input())
lines=[]
for _ in range(N):
    lines.append(list(map(int, input().split())))
for line_idx in range(len(lines)):
    if line_idx==0:
        continue
    for l_idx in range(len(lines[line_idx])):
        if l_idx==0:
            lines[line_idx][0]+=lines[line_idx-1][0]
        elif l_idx==len(lines[line_idx])-1:
            lines[line_idx][-1]+=lines[line_idx-1][-1]
        else:
            lines[line_idx][l_idx]+=max(lines[line_idx-1][l_idx-1], lines[line_idx-1][l_idx])

print(max(lines[-1]))
'''
pass
'''