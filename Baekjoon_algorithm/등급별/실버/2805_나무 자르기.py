N, M = map(int, input().split())
Trees = list(map(int, input().split()))
def answer(s, l):
    if s>l:
        return l
    m = (s+l) // 2
    cnt=0
    for tree in Trees:
        cut = (tree-m)
        if cut >= 0:
            cnt += cut
    if cnt>=M:
        return answer(m+1, l)
    else:
        return answer(s, m-1)
print(answer(1, max(Trees)))