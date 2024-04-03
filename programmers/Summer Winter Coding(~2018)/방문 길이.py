def solution(dirs):
    dir_dict = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    visited = set()
    cur_pos = (0, 0)
    for dir in dirs:
        next_pos = (cur_pos[0] + dir_dict[dir][0], cur_pos[1] + dir_dict[dir][1])
        # 범위에 있을 때만 방문
        if -5 <= next_pos[0] <= 5 and -5 <= next_pos[1] <= 5:
            visited.add((cur_pos, next_pos))
            visited.add((next_pos, cur_pos))
            cur_pos = next_pos
    return len(visited) // 2

if __name__ == '__main__':
    print(solution("ULURRDLLU"))  # 7
    print(solution("LULLLLLLU"))  # 7
    print(solution("LRLRL"))  # 1
    print(solution("UDUDUDUD"))  # 1