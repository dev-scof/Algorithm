from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
print('\n'.join(map(str, data)))
'''
스킬

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

를 추가함으로써 입출력 시간을 크게 줄일 수 있다.

'''