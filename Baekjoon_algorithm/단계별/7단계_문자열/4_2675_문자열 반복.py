# 문자열 반복
T = int(input())
for i in range(T):
    result = ""
    R, String = input().split()
    for j in String:
        result += j * int(R)
    print(result)
