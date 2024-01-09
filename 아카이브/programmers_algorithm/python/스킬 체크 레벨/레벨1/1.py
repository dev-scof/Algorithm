from collections import Counter
def solution(participant, completion):
    Part = Counter(participant)
    Comp = Counter(completion)
    for name, count in Comp.items():
        Part[name]-=count
        if Part[name] != 0:
            return name
    for name, count in Part.items():
        if count != 0:
            return name
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "mislav", "mislav"]))