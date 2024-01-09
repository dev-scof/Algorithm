'''
실패 요인
- 왼쪽에 추 하나만을 다는 줄 알고 있었다. -> 여러개를 달 수 있었다.
- 음수의 경우 절대값을 붙여 계산했다. -> 음수의 경우는 포함시키면 안된다.
'''
from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
chu = list(map(int,input().rstrip().split()))
S = sum(chu)
ans = set(chu)

def cal_weight(chu_list):
    right = sum(chu_list)
    ans.add(right) # 오른쪽에 추를 전부 달 경우
    
    for chu_num in range(1, len(chu_list)+1):
        for chu_sub in combinations(chu_list, chu_num):
            # chu_sub : 왼쪽에 달릴 추 리스트
            left = sum(chu_sub) # 왼쪽에 달릴 추 무게
            if right - left*2 > 0: # left*2를 한 이유 : right에서 이미 더해졌기 때문
                # 양수의 경우에 대해서만 추가한다.
                # 음수의 경우 그릇에 물건을 달 수 없기 때문이다.
                ans.add(right - left*2)

# 추의 개수에 대해 반복
for chu_num in range(1, len(chu)+1):
    # 개수에 따른 조합 계산
    for chu_comb in combinations(chu, chu_num):
        cal_weight(chu_comb)

cnt = 0
for i in range(1, S+1):
    if i not in ans:
        cnt+=1
print(cnt)