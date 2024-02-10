def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in map(lambda x: x.upper(), cities):
        # hit
        if city in cache:
            answer += 1
            cache.insert(0, cache.pop(cache.index(city)))
        # miss
        elif cacheSize == 0:
            answer += 5
        elif len(cache) >= cacheSize:
            cache.pop()
            cache.insert(0, city)
            answer += 5
        else:
            cache.insert(0, city)
            answer += 5
    return answer

if __name__ == '__main__':
    # print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    # print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    # print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16