from itertools import permutations
def solution(k, dungeons):
    answer = 0
    temp_k = k
    for per in list(permutations(range(len(dungeons)), len(dungeons))):
        cnt = 0
        k = temp_k

        for i in per:
            if k < dungeons[i][0]:
                continue
            else:
                k-=dungeons[i][1]
                cnt+=1
        if cnt > answer:
            answer=cnt        
    return answer

'''
dfs로 푼다면

def dfs(k, dungeons, cnt):
    global answer
    if k <= 0:
        return
    if cnt > answer:
        answer = cnt
    # 모든 던전에 대해 반복한다.
    for i in range(len(dungeons)):
        # 방문하지 않고, 최소 피로도가 k보다 작거나 같으면 방문하기
        if not dungeons[i][2] and k >= dungeons[i][0]:
            dungeons[i][2] = True
            dfs(k - dungeons[i][1], dungeons, cnt+1)
            # 방문한 것을 안한것으로 바꾼다.
            dungeons[i][2] = False

def solution(k, dungeons):
    for i in range(len(dungeons)):
        dungeons[i].append(False) # 방문 여부
    dfs(k, dungeons, 0)
    return answer

'''

print(solution(80, [[80,20],[50,40],[30,10]]))