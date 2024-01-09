'''
https://claude-u.tistory.com/206
검색을 통해 LIS를 이용해야한다는 것을 알아내었다.

이 문제는 첫번째 전봇대에 대해 오름차순으로 정렬한 후,
두번째 전봇대에 대해 최대 증가하는 수열의 길이를 찾으면 그것이 꼬이지 않는 전선이 된다...
'''
N = int(input())
for _ in range(N):
    a, b = map(int, input())