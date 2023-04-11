'''
사용할 수 있는 곡괭이중 아무거나 하나 선택해서 광물을 캔다.
한번 사용하기 시작한 곡괭이는 사용할 수 없을때까지 사용한다.
광물은 주어진 순서대로만 캘 수 있다.
광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 캔다


풀이)
5개씩 각 광물에 대한 가중치(비용)을 계산하여 저장한다.


'''
def solution(picks, minerals):
    tired_list = {
        # '광물'을 캘 때, 각각 드는 비용 // 
        # 0: 다이아몬드 곡괭이로 캘 때 드는 피로도, 
        # 1: 철 곡괭이로 캘 때 드는 피로도, 
        # 2: 돌 곡괭이로 캘 때 드는 피로도
        "diamond":[1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }
    greedy = []
    tired = [0]*3
    for i in range(len(minerals)):
        # 5개씩 끊어서 greedy 리스트에 누적 피로도를 저장한다.
        if i!=0 and i%5==0:
            greedy.append((i//5, tired))
            tired=[0]*3
        cur_mineral = tired_list[minerals[i]]
        tired[0] += cur_mineral[0]
        tired[1] += cur_mineral[1]
        tired[2] += cur_mineral[2]

        
            
    else:
        greedy.append((i//5+1, tired))

    indexes=dict() # 5개씩 어떤 곡괭이를 써야하는지 저장

    # 다이아 곡괭이 정하기
    greedy.sort(key=lambda x:x[1][2])
    # print(greedy)
    for i in range(picks[0]):
        if greedy==[]:
            break
        cur = greedy.pop()
        indexes[cur[0]-1] = 'diamond'

    # 철 곡괭이 정하기
    greedy.sort(key=lambda x:x[1][1])
    for i in range(picks[1]):
        if greedy==[]:
            break
        cur = greedy.pop()
        indexes[cur[0]-1] = 'iron'

    # 돌 곡괭이 정하기
    greedy.sort(key=lambda x:x[1][0])
    for i in range(picks[2]):
        if greedy==[]:
            break
        cur = greedy.pop()
        indexes[cur[0]-1] = 'stone'

    answer = 0
    tired_list = {
        "diamond":[1, 1, 1],
        "iron": [5, 1, 1],
        "stone": [25, 5, 1]
    }
    matching = {
        'diamond':0,
        'iron':1,
        'stone':2
    }
    for i in range(len(minerals)):
        if i>=sum(picks)*5:
            break
        
        if i//5 not in indexes:
            cur_pick = indexes[i//5+1]
        else:
            cur_pick = indexes[i//5] # 현재 곡괭이
        # print("현재 곡괭이 = ", cur_pick, "i = ", i, i//5)
        answer += tired_list[cur_pick][matching[minerals[i]]]
    
    return answer

# print(solution([1,1,0], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron"]))
# print(solution([1,3,2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
# print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
# print(solution([1,1,0], ["iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond"]))
# print(solution([0,1,0], ['stone', 'stone', 'stone', 'stone', 'stone']))
print(solution([1,1,0], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone","iron", "iron", "diamond","diamond"]))