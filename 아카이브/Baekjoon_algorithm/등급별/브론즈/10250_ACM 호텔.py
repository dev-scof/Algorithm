'''
w개의 방이 있는 h층 건물
엘리베이터는 가장 왼쪽
'''
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n%h == 0:
        height = h
        width = n//h
    else:
        height = n%h
        width = n//h+1
    print(f'{height}{str(width).zfill(2)}')