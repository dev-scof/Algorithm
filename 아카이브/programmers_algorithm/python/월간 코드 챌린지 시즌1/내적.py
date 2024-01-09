def solution(a, b):
    return sum(list(map(lambda x : x[0]*x[1], list(zip(a,b)))))
    
print(solution([1,2,3,4], [-3,-1,0,2]))
'''
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

코드해석)
zip(a, b)에 대해서 x*y연산을 수행하여 새로운 리스트를 생성한다.
그 리스트의 sum값을 반환한다.

zip()을 저렇게 접근할 수 있음을 알 수 있었다.
'''