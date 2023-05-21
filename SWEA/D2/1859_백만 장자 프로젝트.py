# 22분
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    temp_max = arr[-1]
    answer = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < temp_max:
            answer += temp_max
            answer -= arr[i]
        else:
            temp_max = arr[i]
    
    print(f'#{test_case} {answer}')