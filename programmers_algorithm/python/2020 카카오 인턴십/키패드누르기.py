def solution(numbers, hand):
    '''
    hand : left / right
    1,4,7 왼쪽 엄지
    3, 6, 9 오른쪽 엄지
    2, 5, 8, 0은 두 엄지손가락의 위치에서 가장 가까운 손 / 같은 경우 hand에 따라
    '''
    answer = []
    one = [0,0]
    two = [0,1]
    three = [0,2]
    four = [1,0]
    five = [1,1]
    six = [1,2]
    seven = [2,0]
    eight = [2,1]
    nine = [2,2]
    zero = [3,1]
    keypad = [one, two, three, four, five, six, seven, eight, nine, zero]
    # print(keypad)
    left = [3, 0]
    right = [3,2]
    for i in numbers:
        if i == 1 or i == 4 or i==7:
            left = keypad[i-1]
            answer.append('L')
        elif i == 3 or i == 6 or i==9:
            right = keypad[i-1]
            answer.append('R')
        else: # 2 5 8 0
            left_distance = abs(left[0] - keypad[i-1][0]) + abs(left[1] - keypad[i-1][1])
            right_distance = abs(right[0] - keypad[i-1][0]) + abs(right[1] - keypad[i-1][1])
            if left_distance < right_distance:
                left = keypad[i-1]
                answer.append('L')
            elif left_distance > right_distance:
                right = keypad[i-1]
                answer.append('R')
            else:
                if hand == "right":
                    right = keypad[i-1]
                    answer.append('R')
                else:
                    left = keypad[i-1]
                    answer.append('L')
    answer = ''.join(answer)
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))