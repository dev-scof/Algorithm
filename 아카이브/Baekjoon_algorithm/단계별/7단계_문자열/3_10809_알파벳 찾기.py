# 알파벳 찾기
String = input()
result = ""
for i in range(ord('a'), ord('z')+1):
    result += str(String.find(chr(i)))+' '
print(result)