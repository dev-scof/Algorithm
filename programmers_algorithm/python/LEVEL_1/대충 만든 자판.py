def solution(keymap, targets):
    count={}
    all_keys=''.join(keymap)
    for k in set(all_keys):
        for key in keymap:
            if k in key:
                if k not in count:
                    count[k]=key.index(k)
                else:
                    count[k]=min(count[k], key.index(k))
    
    answer = []
    for target in targets:
        cnt=0
        flag=True
        for k in target:
            if k not in count:
                flag=False
                break
            cnt+=count[k]+1
        
        if flag:
            answer.append(cnt)
        else:
            answer.append(-1)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
'''
def make_keymap(keymap):
    dic = {}
    for k in keymap:
        for i in range(len(k)):
            if k[i] not in dic:
                dic[k[i]]=i
            else:
                dic[k[i]]=min(i,dic[k[i]])

    return dic

def solution(keymap, targets):
    key_map = make_keymap(keymap)
    ans = []
    for target in targets:
        cnt = 0
        for t in target:
            if t in key_map:
                cnt+=key_map[t]+1
            else:
                ans.append(-1)
                break
        else:    
            ans.append(cnt)

    return ans
'''