import sys
while True:
    N1, N2 = map(int, sys.stdin.readline().split())
    if N1 == N2 == 0:
        break
    if not N1 % N2:
        print('multiple')
    elif not N2 % N1:
        print('factor')
    else:
        print('neither')