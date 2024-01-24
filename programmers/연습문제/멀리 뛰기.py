def solution(n):
    if n == 1 or n == 0:
        return 1
    a, b = 1, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b % 1234567

'''
1,1,1,1,1,1 -> 1개
1,1,2,1 -> 4개
2,2,1 -> 3개
0 -> 1
1 -> 1
2 -> 2
3 -> 3
4 -> 5
5 -> 8
6 -> 13
'''



if __name__ == '__main__':
    print(solution(4))
    print(solution(5))