def recursion(string, l, r, cnt):
    if(l >= r): return 1, cnt
    elif (string[l] != string[r]): return 0, cnt
    else: return recursion(string, l+1, r-1, cnt+1)

def isPalindrome(string):
    return recursion(string, 0, len(string)-1, 1)

for _ in range(int(input())):
    result, cnt = isPalindrome(input())
    print(result, cnt)

