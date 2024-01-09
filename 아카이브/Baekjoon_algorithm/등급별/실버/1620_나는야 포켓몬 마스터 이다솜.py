N, M = map(int, input().split())
name_to_number={}
number_to_name={}
for i in range(N):
    name = input()
    name_to_number[name] = i
    number_to_name[i] = name
for _ in range(M):
    number_or_name = input()
    if number_or_name.isdigit():
        print(number_to_name[int(number_or_name)-1])
    else:
        print(name_to_number[number_or_name]+1)