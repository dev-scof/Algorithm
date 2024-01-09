num1=input()
num2=input()
answer=0
for i in range(len(num2)):
    result=0
    for j in range(len(num1)):
        result*=10
        result+=int(num2[len(num2)-1-i]) * int(num1[j])
    answer+=result*10**i
    print(result)
print(answer)