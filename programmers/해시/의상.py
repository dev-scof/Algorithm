def solution(clothes):
    # 의상 종류별 개수 저장
    cloth = {}
    for c in clothes:
        if c[1] in cloth:
            cloth[c[1]] += 1
        else:
            cloth[c[1]] = 1

    answer = 1
    for count in cloth.values():
        answer *= (count + 1)
    answer -= 1

    return answer

if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"]]))
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))