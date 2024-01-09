'''
이진트리 기반의 최소 힙 자료구조
'''
import heapq
heap = []
# heappush : 원소 삽입
heapq.heappush(heap, (2, '지은'))
heapq.heappush(heap, (6, '동아'))
heapq.heappush(heap, (8, '소희'))
heapq.heappush(heap, (7, '서림'))
heapq.heappush(heap, (5, '유진'))
heapq.heappush(heap, (9, '민아'))
print(heap)
# heappop() : 원소 삭제
print(heapq.heappop(heap))
print(heap)
# heapify : 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)

# 최대힙 만들기
import heapq
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1