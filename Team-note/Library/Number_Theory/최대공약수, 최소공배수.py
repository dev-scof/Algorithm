# 최대공약수, 재귀 - 유클리드 호제법
def gcd_recursive(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_recursive(b, a % b)

# 최소 공배수
def LCM(a, b):
    return a*b // gcd_recursive(a,b)

if __name__ == '__main__':
    print(gcd_recursive(78696, 19332))
    print(LCM(12, 3))