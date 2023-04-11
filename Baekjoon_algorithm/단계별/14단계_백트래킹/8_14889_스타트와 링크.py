# N은 짝수 
# S(i,j)는 i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치
# 팀 능력치 : 팀에 속한 모든 쌍의 능력치(Sij)의 합
from sys import stdin
from itertools import combinations
N = int(stdin.readline())
S = [list(map(int, input().split())) for _ in range(N)]
mixed = list(combinations(range(N), N//2))
start = mixed[:len(mixed)//2]
link = sorted(mixed[len(mixed)//2:], reverse=True)
gap = []
def cal_scores(team):
    score=0
    for i in team:
        for j in team:
            if i==j:
                continue
            score+=S[i][j]
    return score

for s, l in zip(start, link):
    s_score = cal_scores(s)
    l_score = cal_scores(l)
    gap.append(abs(s_score-l_score))
print(min(gap))