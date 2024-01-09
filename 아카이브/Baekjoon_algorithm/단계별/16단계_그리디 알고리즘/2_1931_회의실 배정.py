# 사용표
# 겹치지 않으면서의 회의할 수 있는 최대 개수
N = int(input())
con=[]
complete=[]
for _ in range(N):
    con.append(list(map(int, input().split())))
for m in sorted(con, key=lambda x:x[0]):
    if complete==[]:
        complete.append(m)
    elif m[1]<=complete[-1][0] or m[0]>=complete[-1][1]: # 안겹치는 경우
        # end가 start보다 작아 or start가 end보다 커
        complete.append(m)
    elif m[1]<=complete[-1][1] and m[0]>= complete[-1][0]:
        # end가 end보다 작거나 같은데, start가 start보다 크거나 같아
        complete.pop()
        complete.append(m)
print(len(complete))
'''
처음 접근방법
- gap이 작은 순서대로 정렬 후 비어있는 시간에 넣는 방법
-> 겹치는지 확인하기 위해 complete된 모든 회의를 돌아야하는 논리 오류발생
-> flag 등을 활용했지만 앞에서부터 확인을 하는 것은 해결되지 않았다.

두번째 접근 방법
- 시간순으로 정렬 후 비어있는 시간에 넣는 방법
-> 시간순(시작시간)으로 정렬했기에 
빨리 끝나는 회의가 있는 경우 pop을 통해 지운 후, append하는 방법 사용
-> complete[-1]에는 최근에 넣은 가장 빠른 시간의 미팅을 의미함
-> 겹치는 부분에 대해 탐욕적으로 접근함


'''