def solution(dirs):
    answer = 0
    visit = set()
    cur_place = [0,0]
    for d in dirs:
        if d == "U":
            if cur_place[0]+1 > 5:
                continue
            next_place = [cur_place[0]+1, cur_place[1]]
        elif d == "D":
            if cur_place[0]-1 < -5:
                continue
            next_place = [cur_place[0]-1, cur_place[1]]
        elif d == "R":
            if cur_place[1]+1 > 5:
                continue
            next_place = [cur_place[0], cur_place[1]+1]
        elif d == "L":
            if cur_place[1]-1 < -5:
                continue
            next_place = [cur_place[0], cur_place[1]-1]
        
        visit.add(tuple(cur_place+next_place)) # 가는방향 1,
        visit.add(tuple(next_place+cur_place)) # 반대방향 1
        cur_place = next_place
    return int(len(visit)/2)

print(solution("LULLLLLLU"))