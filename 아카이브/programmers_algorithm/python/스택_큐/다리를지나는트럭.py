def solution1(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer

def solution2(bridge_length, weight, truck_weights):
    # 통과 못함
    answer = 0
    cur_truck_cnt = 0
    cur_weight = 0
    while truck_weights:
        answer += 1
        cur_truck_cnt += 1
        cur_weight += truck_weights[0]
        # 트럭을 보내야하는 경우
        if (cur_truck_cnt > bridge_length) or (cur_weight > weight):
            cur_truck_cnt -= 1
            cur_weight -= truck_weights.pop(0)
            continue

        # 트럭을 보내지 않아도 되는 경우
        truck_weights.pop(0)

    return answer + bridge_length

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    bridge = [0] * bridge_length
    while truck_weights:
        answer += 1

        if bridge[0]:
            cur_weight -= bridge[0]
        bridge.pop(0)
        bridge.append(0)
        if cur_weight + truck_weights[0] <= weight:
            w = truck_weights.pop(0)
            bridge[-1] = w
            cur_weight += w

    return answer + bridge_length


print(solution(2, 10 ,[7,4,5,6]))
print("*"*10)
print(solution(100, 100 ,[10]))