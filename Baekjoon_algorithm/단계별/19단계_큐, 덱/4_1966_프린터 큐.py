from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    answer = []
    document = deque()
    N, M = map(int, input().split())
    document = deque(zip(list(range(N)), list(map(int, input().split()))))
    
    while len(document) != 0:
        flag = True
        first_imp = document[0][1]
        # 우선순위 확인
        for n, imp in document:
            if imp > first_imp:
                flag = False
                break
        if flag:
            # 현재 우선순위가 먼저일 경우
            answer.append(document.popleft())

            # 마지막에 들어온 값이 M인경우
            if answer[-1][0]==M:
                print(len(answer))
                break
        else:
            # 현재 우선순위가 후위일 경우
            document.append(document.popleft())