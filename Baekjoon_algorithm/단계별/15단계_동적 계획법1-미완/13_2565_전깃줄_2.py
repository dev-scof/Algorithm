# 이전의 코드에서 많이 겹치는 것을 먼저 제거하는 방향으로
# 풀이를 진행했으나, 실패
# 이번 코드에서는 많이 등장하는 전깃줄을 제거하는 방향으로
# 풀이해 본다.


from collections import defaultdict, Counter
N = int(input())
lines = []
answer = 0
graph = defaultdict(list)
counter = Counter()
for _ in range(N):
    line = list(map(int, input().split()))+[0]
    lines.append(line)
for i in range(len(lines)):
    for j in range(len(lines)):
        if i==j:
            continue
        if lines[i][0]<lines[j][0] and lines[i][1]>lines[j][1]:
            graph[(lines[i][0], lines[i][1])].append((lines[j][0], lines[j][1]))
            counter[(lines[i][0], lines[i][1])] += 1
        if lines[i][0]>lines[j][0] and lines[i][1]<lines[j][1]:
            graph[(lines[i][0], lines[i][1])].append((lines[j][0], lines[j][1]))
            counter[(lines[i][0], lines[i][1])] += 1
# print('counter = ', counter.items())
remove_list = sorted(counter.items(), key=lambda x:x[1])
# print('removelist = ', remove_list)
while remove_list:
    # print('*'*40)
    cnt=0
    for key, value in graph.items():
        # print('현재 그래프의 key = ', key, 'value = ', value)
        if value==[]:
            cnt+=1
    if cnt==len(graph):
        break
    
    key, value = remove_list.pop() # key : 삭제할 키
    # print('삭제할 키 = ', key)
    graph.pop(key)
    for k, l in graph.items():
        if key in l:
            graph[k].remove(key)
    
    answer+=1
print(answer)
