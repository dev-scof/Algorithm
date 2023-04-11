
def solution(wallpaper):
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=='#':
                if answer==[]:
                    answer+=[i,j,i+1,j+1]
                else:
                    # 시작 열 갱신 // 시작행은 갱신할 필요없음
                    answer[1] = min(answer[1], j)
                    # 끝 행 갱신
                    answer[2] = i+1
                    # 끝 열 갱신
                    answer[3] = max(answer[3], j+1)
    return answer


solution([".#...", "..#..", "...#."])
solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
solution(["..", "#."])
'''
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]
'''