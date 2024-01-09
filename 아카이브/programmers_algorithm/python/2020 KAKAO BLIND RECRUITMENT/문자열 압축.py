def solution(s):
    temp = []
    if len(s) == 1:
        return len(s)
    for i in range(1, int(len(s)/2)+1):
        # i개 만큼 자름
        pre_word = s[0:i]
        #print("첫 단어 : ", pre_word)
        s_index=i
        l_index=i*2
        count=0
        new_str = ""
        for j in range(1, int(len(s)/i)):
            word = s[s_index:l_index] 
            #print("현재 단어 : ", word)
            if pre_word == word:
                count+=1
            else: # 다른 경우
                if count == 0 : # count=0이면, 1을 붙이지 않는다.
                    new_str += pre_word
                else: # count가 0이 아닌경우
                    new_str += (str(count+1) + pre_word)
                count=0
            pre_word = word
            s_index=l_index
            l_index=l_index+i
        if s_index < len(s): # 전체 끝까지 안갔을경우
            word = s[s_index:]
            #print("끝까지 안감",word)
            new_str += word
        
        if count==0:
            #print("check = ", pre_word)
            new_str += pre_word
        else:
            new_str += (str(count+1) + pre_word)
        temp.append(new_str)
        #print('s_index = ', s_index)
        #print("new str = ", new_str)
    return min(map(len, temp))
print(solution("a"))