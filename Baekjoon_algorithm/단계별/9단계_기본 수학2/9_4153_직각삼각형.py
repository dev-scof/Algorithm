while True:
    t = sorted(map(int, input().split()))
    if sum(t) == 0:
        break
    print("right" if t[0]**2 + t[1]**2 == t[2]**2 else "wrong")
    