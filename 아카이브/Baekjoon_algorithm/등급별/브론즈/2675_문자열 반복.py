for _ in range(int(input())):
    cnt, word = input().split()
    for w in word:
        print(w*int(cnt), end='')
    print()