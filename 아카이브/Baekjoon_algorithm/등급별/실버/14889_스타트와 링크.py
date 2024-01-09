'''
2023.03.08
- 25분 컷
'''
from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = set(range(N))
teams = list(combinations(range(N), N//2))
gap=1e9
def score(team):
    '''
    team에서 만들 수 있는 능력치
    '''
    pairs = list(combinations(team, 2))
    score=0
    for pair in pairs:
        score+=S[pair[0]][pair[1]]
        score+=S[pair[1]][pair[0]]
    return score
for t_i in range(len(teams)//2):
    team1 = teams[t_i]
    team2 = teams[len(teams)-t_i-1]
    if gap > abs(score(team1) - score(team2)):
        gap = abs(score(team1) - score(team2))
print(gap)