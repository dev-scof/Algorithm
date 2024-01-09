# 상수
num1, num2 = map(''.join, (map(reversed, input().split())))
print(num1 if num1>num2 else num2)