answer = 0
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