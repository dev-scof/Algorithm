N, r, c = map(int, input().split())

def sol(N, r, c):
    print(f'현재 N={N}, r={r}, c={c}')
    print(f"더하는 값 : {2*(r%2)+(c%2)}")
    if N == 0:
        return 0
    
    return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))

print(sol(N, r, c))