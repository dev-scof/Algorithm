T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dis = y-x
    mov = 1
    cur_pos = cnt = 0
    while cur_pos < dis:
        cnt+=1
        cur_pos += mov
        if cnt % 2 == 0:
            mov +=1

    print(cnt)