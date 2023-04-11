def solution(name):
    print(ord('A'), ord('Z'))
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]    # 위 또는 아래로 움직이는 횟수
        make_name[idx] = 0          # A를 만들어줬으므로 0으로 초기화
        if sum(make_name) ==0:      # 모두 A로 만들어줬을 경우(조작완료) -> break
            break
        left, right = 1, 1          # 왼쪽, 오른쪽의 거리를 확인하기 위한 변수
        while make_name[idx - left] ==0:
            left +=1
        while make_name[idx + right] ==0:
            right +=1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer
         
print(solution("BBC"))
