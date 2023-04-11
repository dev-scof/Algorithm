def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    zero = lottos.count(0)
    lot = set(lottos)
    buy = set(win_nums)
    min_ = len(buy & lot)
    max_ = min_ + zero
    if min_ < 2:
        min_ = 6
    else:
        min_ = rank[min_]
    if max_ < 2:
        max_ = 6
    else:
        max_ = rank[max_]

    return [ max_, min_,]
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
'''
1->6
2
3
4
5
6

알수없는 번호를 0으로 표시

'''