import sys
def gcd(a, b):
    if a%b==0:
        return b
    return gcd(b, a%b)
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer=[]
rate=0
for i in range(len(nums)):
    if i == 0:
        first=nums[i]
    else: # n은 마지막으로 들어온값
        cur_up = first
        cur_down = nums[i]
        first=nums[i]
        if answer==[]:
            g = gcd(cur_up, cur_down)

            answer.append((cur_up//g, cur_down//g))
        else:
            a_up = answer[-1][0]*cur_up
            a_down = answer[-1][1]*cur_down
            g = gcd(a_up, a_down)
            answer.append((a_up//g, a_down//g))

for u, d in answer:
    print(str(u)+'/'+str(d))