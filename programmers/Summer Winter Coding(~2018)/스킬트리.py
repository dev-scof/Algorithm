def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        temp = ''.join([s for s in skill_tree if s in skill])
        if skill.startswith(temp):
            answer += 1
    return answer

if __name__ == '__main__':
    print(
        solution("CBD", ["BACDE", "CBADF", "AECB"]) # 2
    )