def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        stack = []
        #print(skill_tree)
        #print(skill_tree)
        for i in skill_tree:
            if i in skill:
                stack.append(i)
                #print(i)
        error = False
        for i, value in enumerate(stack): 
            # 이부분을 if skill[:len(stack)]==stack로 하면 되겠네
            # 그러면 error 변수도 필요없고...
            if value != skill[i]:
                error = True
                break
        if not error:
            answer+=1
        #print(stack)
    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))