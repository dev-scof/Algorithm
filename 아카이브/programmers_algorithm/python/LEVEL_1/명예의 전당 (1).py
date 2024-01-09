'''
매일 출연한 가수의 점수가 / 지금까지 출연한 가수들의 점수 중 상위 k번째 이내이면, 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념한다.
즉, 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오릐게 된다.
k일 이후부터는 출연한 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 점수보다

이 프로그램에서는 매일 명예의 전당의 최하위 점수를 발표한다. 
예를 들어 k=3이고 7일동안 진행된 가수의 점수가 10, 100, 20, 150, 1, 100, 200이면, 
명예의 전당에서 발표된 점수는 아래의 그림과 같이 10, 10, 10, 10, 20, 20, 100, 100이다

'''
import heapq
def solution(k, scores):
    answer = []
    rank = []
    for score in scores:
        if len(rank)<k:
            heapq.heappush(rank, score)
        else:
            heapq.heappush(rank, score)
            heapq.heappop(rank)
        answer.append(rank[0])

    return answer
# print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))