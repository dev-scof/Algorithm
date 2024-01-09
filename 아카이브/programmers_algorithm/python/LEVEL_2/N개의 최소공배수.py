def GCD(a, b):
    while True:
        r = a%b
        if r==0:
            return b
        a = b
        b = r
def LCM(a, b):
    return a*b // GCD(a,b)

def solution(arr):
    arr.sort()
    while True:
        arr.append(LCM(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

print(solution([12,36,48,84]))