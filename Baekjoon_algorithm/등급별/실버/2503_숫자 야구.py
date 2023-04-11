from itertools import permutations
p_list = list(permutations(['1','2','3','4','5','6','7','8','9'], 3))
for _ in range(int(input())):
    n, s, b = input().split()
    for p_num in p_list[:]:
        p_s=p_b=0
        for i in range(3):
            if n[i]==p_num[i]:
                p_s+=1
            elif n[i] in p_num:
                p_b+=1
        if p_s != int(s) or p_b != int(b):
            p_list.remove(p_num)
print(len(p_list))