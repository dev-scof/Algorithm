def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a, b)

def solution(arr):
    answer = 0
    while len(arr) > 1:
        arr.append(lcm(arr.pop(), arr.pop()))
    answer = arr[0]
    return answer

if __name__ == "__main__":
    print(solution([2,6,8,14]))
    print(solution([1,2,3]))