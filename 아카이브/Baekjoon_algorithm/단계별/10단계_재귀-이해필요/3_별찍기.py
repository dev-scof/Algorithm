import sys
def append_star(l):
    if l == 1:
        return ['*']
    Stars = append_star(l//3)
    L = []

    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S + ' '*(l//3) + S)
    for S in Stars:
        L.append(S*3)
    return L

N = int(sys.stdin.readline().strip())
print('\n'.join(append_star(N)))