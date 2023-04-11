import sys
input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split())

def solve(A, B):
    if B==1:
        return A % C
    
    temp = solve(A, B//2)
    
    
    if B%2:
        return temp * temp * A % C

        
    else:
        return temp * temp % C
    
print(solve(A, B))
