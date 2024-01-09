# https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=occidere&logNo=220787441430
'''
N-2의 경우의 수들엔 "맨 뒤에" 00을 붙이고, N-1의 경우의 수들엔 "맨 앞에" 1을 붙이는 규칙
[출처] [백준] 1904 - 01타일|작성자 occidere
- 오류 : 중복이 생기는 오류가 있다
- 수정 : 규칙이 
n-2 일때 뒤에 00
n - 1 일때 뒤에 1을 
붙이는것같습니다 그러면 중복없네요
[출처] [백준] 1904 - 01타일|작성자 occidere

'''
n = int(input())
dp = [0,1,2]
for i in range(3, n+1):
    dp.append(dp[i-2]+dp[i-1])
    dp[i]%=15746
print(dp[n])