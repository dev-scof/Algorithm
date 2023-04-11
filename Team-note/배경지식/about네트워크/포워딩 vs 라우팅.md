# 포워딩(Forwarding)과 라우팅(Routing)의 차이점
## 교재
1. Forwarding
  - local action: move arriving packets from router's input link to appropriate router output link
   - 로컬 작업: 라우터의 입력 링크에서 도착한 패킷을 적절한 라우터 출력 링크로 이동시키는 것
2. Routing
  - global action: determine source destination paths taken by packets
  - 글로벌 작업: 패킷이 취하는 소스 목적지를 결정하는 것

## 블로그
[출처](https://nenunena.tistory.com/52)
* Forwarding Table과 Routing Table의 개념을 알아야 한다.
1. Forwarding
- 포워딩 테이블에 적힌 목적지 주소에 대응된 출력 포트로 패킷을 이동시키는 작업
2. Routing
- 라우팅 알고리즘을 이용하여 포워딩 테이블을 만드는 작업