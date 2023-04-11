from collections import defaultdict
N = int(input())
lines = []
answer = 0
graph = defaultdict(list)
for _ in range(N):
    line = list(map(int, input().split()))+[0]
    lines.append(line)
for i in range(len(lines)):
    for j in range(len(lines)):
        if i==j:
            continue
        
        if lines[i][0]<lines[j][0] and lines[i][1]>lines[j][1]:
            graph[(lines[i][0], lines[i][1])].append((lines[j][0], lines[j][1]))
        if lines[i][0]>lines[j][0] and lines[i][1]<lines[j][1]:
            graph[(lines[i][0], lines[i][1])].append((lines[j][0], lines[j][1]))

sorted_dict = sorted(graph.items(), key=lambda x:len(x[1]))
while sorted_dict:
    cnt=0
    for key, value in sorted_dict:
        if value==[]:
            cnt+=1
    if cnt==len(sorted_dict):
        break
    
    key, value = sorted_dict.pop()
    for k in sorted_dict:
        if k[0] in value:
            k[1].remove(key)
    answer+=1
print(answer)
# lines.sort(key=lambda x:x[2])
# count = list(map(lambda x:x[2], lines))

# while count:
#     count.pop()
#     count = list(map(lambda x:x-1, count))
#     answer+=1
#     if max(count)<=0:
#         break
# print(answer)
# print(lines)
