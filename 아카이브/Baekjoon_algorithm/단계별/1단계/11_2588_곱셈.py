n1 = int(input())
n2 = int(input())

temp = n2
for i in range(3):
    mod = temp % 10
    temp= int(temp/10)
    print(mod*n1)

print(n1*n2)