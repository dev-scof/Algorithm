from collections import Counter

def check(counter, items):
    for item in items:
        c = counter.get(item)
        if not c or items[item] - c > 0:
            return False
    return True

def solution(want, number, discount):
    answer = 0
    items = {x: y for x, y in zip(want, number)}
    f = len(discount) - 10
    for i in range(f+1):
        counter = Counter(discount[i:i+10])
        items_copy = items.copy()
        if check(counter, items_copy):
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution(
        ["banana", "apple", "rice", "pork", "pot"],
        [3, 2, 2, 2, 1],
        ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
    ))
    print(solution(
        ["apple"],
        [10],
        ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
    ))



