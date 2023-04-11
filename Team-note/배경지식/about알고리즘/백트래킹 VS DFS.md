# Goal
- 백트래킹에 대해 설명할 수 있다.
- DFS와 백트래킹을 설명할 수 있다.

## 백트래킹(backtracking)이란?
- 솔루션을 찾는 과정에서, 유망(promising)하지 않은 후보해에 대해 대해 빠르게 포기하고 이전 단계로 되돌아(back track)가 다른 후보해를 찾는 알고리즘 기법

## DFS와 Backtracking
- DFS : 완전 탐색을 기본으로 하는 그래프 순회 기법으로, 모든 노드를 방문하는 것을 목표로 한다.
- Back-tracking : 불필요한 탐색을 하지 않고, 이전 단계로 돌아와 다른 후보해를 탐색해 나가는 방법
    - => 일단 가보고 후보해가 될 수 없으면 다음 단계로 진행하지 않고 되돌아 나온다.

 
#### DFS와 Back-tracking 둘다 재귀 호출 형태로 자주 구현이 되기 때문에 헷갈린다.


## 두 알고리즘은 사용 목적에 차이가 있다.
- DFS : 깊이 우선 탐색하여 모든 노드를 방문하는 것을 목표로 한다.
- Backtracking : 불필요한 탐색을 하지 않기 위해, 유망하지 않은 경우의 수를 줄이는 것을 목표로 한다.

> DFS는 완전 탐색을 목표로 하는 알고리즘이기 때문에 자원 소모가 굉장히 심하다. 그래서 어떤 제약 조건에 맞는 해답을 찾기 위해서 DFS와 Back-tracking 기법을 혼용해서 사용한다.

=> 가지 치기를 통해서 얻은 그래프에 대해서 다시 DFS 탐색을 하면서 불필요한 탐색을 줄여 나간다.

<br>

## 다음 그림은 DFS와 Back tracking을 이용해서 'AIR' 라는 단어를 찾는 과정을 나타낸 것이다.
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FEiXFJ%2FbtqFpzIQhZl%2FmvEkJ0wAyzyABLuFXxry91%2Fimg.jpg">

1. 현재 트리에 대해 DFS를 수행 (단어가 일치하거나, 모든 노드를 방문할때까지 진행)
2. 가지 치기(pruning)를 통해 적합하지 않은 부분 제거 (위 그림에서는 AN, AIM)
3. 가지 치기한 결과 트리에 대해 1과정 다시 진행

DFS 문제 : 단지 번호 붙이기 - https://www.acmicpc.net/problem/2667

back tracking 문제 : 스도쿠 - https://www.acmicpc.net/problem/2239


# Backtracking vs Branch-&-Bound
### 공통점
- 불필요한 탐색 부분을 제거 하는 방법
### 차이점
- Backtracking : 가보고 더 이상 진행이 되지 않으면 돌아온다
- Branch-&-Bound : 최적해를 찾을 가능성이 없으면 분기는 하지 않는다

## 출처
- https://gamedevlog.tistory.com/49