from collections import Counter
in_ = input()
counter=Counter(in_)
odd_chr_cnt = len(list(filter(lambda x:x%2==1 ,counter.values())))
if odd_chr_cnt>=2 or (len(in_)%2==1 and odd_chr_cnt%2==0) or (len(in_)%2==0 and odd_chr_cnt%2==1):
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 만들 수 있음
    sorted_in_ = list(sorted(map(list, (counter.items())), key=lambda x:x[0]))
    answer=''
    if len(in_)%2==1:
        # 홀수길이일 경우 -> 홀수 값을 중앙으로 위치시킨다.
        odd_chr = list(filter(lambda x:x[1]%2==1, sorted_in_))[0]
        answer+=odd_chr[0]
        sorted_in_[sorted_in_.index(odd_chr)][1]-=1
    while sorted_in_:
        char, num = sorted_in_.pop()
        answer = char*(num//2)+answer+char*(num//2)
    print(answer)