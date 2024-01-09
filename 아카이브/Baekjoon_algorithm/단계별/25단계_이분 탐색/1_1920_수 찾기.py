import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().rstrip().split()))

M = int(input())
for i in map(int, input().rstrip().split()):
    if i in arr:
        print(1)
    else:
        print(0)
'''
import sys
input = sys.stdin.readline

def binary_search(setA, i, start, end):
    if start > end:
        return 0
    mid = (end+start) // 2 # 중간지점
    if setA[mid] == i: # 타겟이 맞을경우
        return 1
    elif setA[mid] < i: # 타겟이 중간지점보다 클 경우
        return binary_search(setA, i, mid+1, end)
    else:
        return binary_search(setA, i, start, mid-1)
 
N = int(input())
setA = list(sorted(map(int, input().rstrip().split())))

M = int(input())
for i in list(map(int, input().rstrip().split())):
    print(binary_search(setA, i, 0, len(setA)-1))
'''