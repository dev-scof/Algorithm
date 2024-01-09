def solution(table, languages, preference):
    answer = {}
    for i in table:
        rows = i.split()
        score = 0
        for match in rows:
            if match in languages:
                #print("rows = ", rows)
                #print("매칭 = ", match)
                #print("매칭 = ", rows.index(match))
                table_score = 6-rows.index(match)
                prefer_score = preference[languages.index(match)]
                #print("table_score = ", table_score)
                #print("prefer_score", prefer_score)
                score += table_score*prefer_score
        answer[rows[0]] = score
        #print()
    
    for key, value in sorted(answer.items(), key=lambda x:x[0], reverse=False):
        if value == max(answer.values()):
            return key

print(
    solution(
        ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
        ["JAVA", "JAVASCRIPT"], 
        [7, 5])
)

