from itertools import permutations
def solution(k, dungeons):
    answer = -1
    # 던전을 도는 모든 순서
    dungeons_per = list(permutations(range(len(dungeons)), len(dungeons)))
    for dungeon_prog in dungeons_per:
        cur_p = k
        cnt = 0
        for dungeon_idx in dungeon_prog:
            if dungeons[dungeon_idx][0] <= cur_p:
                cnt+=1
                cur_p-=dungeons[dungeon_idx][1]
        if answer < cnt:
            answer=cnt

                
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))