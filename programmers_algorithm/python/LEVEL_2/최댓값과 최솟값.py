def solution(s):
    numlist = list(map(int,s.split()))
    Mx = max(numlist)
    Mn = min(numlist)
    return "{} {}".format(Mn, Mx)
print(solution('1 2 3 4'))