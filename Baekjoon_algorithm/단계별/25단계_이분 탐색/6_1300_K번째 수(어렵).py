import sys
input = sys.stdin.readline
N = int(input())
K = int(input())

# N = 3 일 때
def bin_(target, s, e):
    print('bin 시작')
    if s>e:
        return s
    
    mid = (s + e) // 2 # 5
    
    # cnt : 몇번째 수 인지 체크
    cnt = 0
    for i in range(1, N+1): # 1 ~ 3
        # 왜 min(mid//i, N) 인가
        '''
        [1, 2, 3]
        [2, 4, 6]
        [3, 6, 9]
        - 첫번째 줄은 1단, 두번째 줄은 2단, 세번째 줄은 3단이다.
        - mid//i는 1단, 2단, 3단에 대한 개수를 의미한다.
        예를들어, mid가 5일 경우 
        -> 1단에서 5보다 작은 수 1, 2, 3
        -> 2단에서 5보다 작은수 2, 4
        -> 3단에서 5보다 작은수 3
        으로 mid//i를 통해 개수를 구할 수 있다.

        '''
        value = min(mid//i, N) # 5, 3! / 2!, 3 / 1!, 3
        print('value = ', value)
        cnt += value
    print('mid = ', mid, '는 ', cnt, '번째 수 입니다.', 's = ', s, 'e = ', e)

    if cnt < target:
        return bin_(target, mid+1, e)
    else:
        return bin_(target, s, mid-1)

print(bin_(K, 1, N*N))
'''
[
    [1, 2, 3]
    [2, 4, 6]
    [3, 6, 9]

    [1, 2, 2, 3, 3, 4, 6, 6, 9]
]

'''