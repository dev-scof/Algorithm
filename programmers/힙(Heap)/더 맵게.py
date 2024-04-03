from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville) # 최소 힙 생성
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        ind1 = heappop(scoville)
        ind2 = heappop(scoville)
        heappush(scoville, ind1+ind2*2) # 새로운 음식 생성 및 힙에 추가
        answer += 1 # 섞은 횟수 증가
    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))  # 2