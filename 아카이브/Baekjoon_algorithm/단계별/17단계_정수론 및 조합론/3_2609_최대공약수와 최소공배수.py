import sys
def gcd_recursive(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_recursive(b, a % b)
n1, n2 = map(int, sys.stdin.readline().split())
gcd = gcd_recursive(n1, n2)
print(str(gcd)+'\n'+ str(n1 * (n2//gcd)))
