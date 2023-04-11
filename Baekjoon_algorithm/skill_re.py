import re
testRe = "12123+1111-2222/333*11"
print("+-/*으로 나누기 -> ", re.split('[+-/*]', testRe))

# 공백이 있을 경우의 구분
testRe2 = re.split("[+-/*]","12123 + 1111 - 2222 / 333 * 11".replace(" ", ""))
print(testRe2)