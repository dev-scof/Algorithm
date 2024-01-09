import sys
N = int(sys.stdin.readline())
arr = list(sorted(map(int, sys.stdin.readline().split())))
print(arr[0]*arr[-1])
'''
sort하지말고 min과 max로 찾을 수 있는 문제였다;

import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(min(arr)*max(arr))
'''
