n = int(input())
def recursive(depth, N):
    print(' '*(N-depth)+'*'*(2*(depth-1)+1))
    if depth==N:
        return
    recursive(depth+1, N)
    print(' '*(N-depth)+'*'*(2*(depth-1)+1))
recursive(1, n)