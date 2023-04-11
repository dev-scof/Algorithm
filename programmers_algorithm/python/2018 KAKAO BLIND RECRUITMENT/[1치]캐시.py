def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = list(map(lambda x:x.lower(), cities))
    if cacheSize == 0:
        return len(cities)*5
    for cite in cities:
        if cite in cache:
            cache.remove(cite)
            cache.insert(0, cite)
            answer+=1
        else:
            if len(cache) >= cacheSize:
                cache.pop()
            cache.insert(0,cite)
            answer+=5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))