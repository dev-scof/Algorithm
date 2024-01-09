words = input().split('-')
num_list = []
for sub in words:
    sub_num = 0
    for num in sub.split('+'):
        sub_num+=int(num)
    num_list.append(sub_num)
answer=0
for i in range(len(num_list)):
    if i==0:
        answer=num_list[0]
    else:
        answer-=num_list[i]
print(answer)