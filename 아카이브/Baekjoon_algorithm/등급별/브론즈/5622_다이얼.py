a={
    'ABC':3,
    'DEF':4,
    'GHI':5,
    'JKL':6,
    'MNO':7,
    'PQRS':8,
    'TUV':9,
    'WXYZ':10
}
answer=0
for c in input():
    for k, v in a.items():
        if c in k:
            answer+=v
print(answer)