'''
***
* *
***

만들고 Map에 복사하는 방법

'''
def print_map(n): # 코드 이해를 위한 함수
    for i in range(n):
        for j in range(n):
            print(Map[i][j], end=' ')
        print()

def draw_star(n) : # 재귀함수
    global Map
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        # 첫 번째 행의 1~3열과 세 번째 행의 1~3열은
        # [1] (별이 있다는 뜻) 이 3개 들어간 형태
        # [1] * 3 을 해줄 경우 [1, 1, 1]의 행이 만들어짐!
        Map[1][:3] = [1, 0, 1]
        return
    a = n//3 # 복사할 길이
    draw_star(n//3) # 재귀 반복
    for i in range(3) :
        for j in range(3) :
            print('i = ', i, 'j = ', j)
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어
            print_map(n)
N = int(input())      
# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]
draw_star(N)
for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()