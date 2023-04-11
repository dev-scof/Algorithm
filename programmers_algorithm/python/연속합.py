n = int(input())
numbers = list(map(int, input().split(' ')))
for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i-1] + numbers[i])
print(max(numbers))

'''
for startindex in range(len(arr)):
    number = arr[startindex]
    for i in range(startindex+1, len(arr)):
        number += arr[i]
        if number<max_:
            continue
        else:
            max_ = number
    startindex+=1
print(max_)

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i-1] + numbers[i])
    '''