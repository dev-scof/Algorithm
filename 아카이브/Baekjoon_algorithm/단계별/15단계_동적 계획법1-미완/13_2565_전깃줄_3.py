# 코드리뷰 중 1, 2번째 시도 모두 그리디를 이용했음을 발견했다.
# 어떻게 dp를 사용해야하지?
N = int(input())
lines = []
dp = []
answer = 0
for _ in range(N):
    line = list(map(int, input().split()))+[0]
    lines.append(line)