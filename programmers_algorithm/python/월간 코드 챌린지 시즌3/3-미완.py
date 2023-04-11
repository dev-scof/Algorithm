def solution(a, b, g, s, w, t):
    #a, b가 있어야 도시를 지음
    # i번 도시에는 금 g[i], s[i], 트럭한대가 존재
    answer = [0]*len(t)
    time = 1
    totalG = 0
    totalS = 0
    while True:
        if totalG>=a and totalS>=b:
            break
        print("*"*10)
        for i in t:
            if time%i == 0:
                index = t.index(i)
                answer[index]+=time
                truck = [0,0] # 금/은
                if totalG < a and totalS >= b: # 금만 부족할 경우
                    if w[index] <= g[index]: # 금을 작업량만큼 실을 수 있을 경우
                        if totalG + w[index] > a: # 작업량을 실을 때 최대를 넘어갈경우 
                            truck[0] += a-totalG
                            totalG += a-totalG
                            g[index] -= a-totalG
                        else: # 작업량을 실을 때 최대를 넘지 않을 경우 -> 작업량
                            truck[0] += w[index]
                            totalG += w[index]
                            g[index] -= w[index]
                    else: # 나머지 금을 실을 수 있을 경우
                        if a >= totalG + g[index]: # 나머지 금 모두 싣는 경우
                            truck[0] += w[index]
                            totalG += w[index]
                            g[index] = 0
                        else: # 나머지 금을 실을 때 a보다 커질 경우
                            truck[0] += a-totalG
                            totalG += a-totalG
                            g[index] -= a-totalG

                if totalS < b and totalG >= a: #은만 부족할 경우
                    if w[index] <= s[index]: # 금을 작업량만큼 실을 수 있을 경우
                        if totalS + w[index] > b: # 작업량을 실을 때 최대를 넘어갈경우 
                            truck[1] += b-totalS
                            totalS += b-totalS
                            s[index] -= b-totalS
                        else: # 작업량을 실을 때 최대를 넘지 않을 경우 -> 작업량
                            truck[1] += w[index]
                            totalS += w[index]
                            s[index] -= w[index]
                    else: # 나머지 금을 실을 수 있을 경우
                        if b >= totalS + w[index]: # 나머지 금 모두 싣는 경우
                            truck[1] += w[index]
                            totalS += w[index]
                            s[index] = 0
                        else: # 나머지 금을 실을 때 a보다 커질 경우
                            truck[1] += b-totalS
                            totalS += b-totalS
                            s[index] -= b-totalS

                if totalG < a and totalS < b: # 둘다 부족할 경우
                    if w[index] <= g[index]: # 금을 작업량만큼 실은 경우
                        # 작업량 만큼 실음
                        if totalG + w[index] > a: #작업량을 실을때 최대를 넘어갈경우
                            truck[0] += a-totalG
                            totalG += a-totalG
                            g[index] -= a-totalG
                        else:
                            truck[0] += w[index]
                            totalG += w[index]
                            g[index] -= w[index]
                    else: # 가지고있는 금이 조금일경우
                        # 나머지 금 모두 실음
                        if totalG + g[index] > a: #남은 금을 실을때 최대를 넘어갈경우
                            truck[0] += a-totalG
                            totalG += a-totalG
                            g[index] -= a-totalG
                        else:
                            truck[0] += w[index]
                            totalG += w[index]
                            g[index] -= w[index]

                    if w[index] <= s[index]: # 은을 작업량만큼 실은 경우
                        # 작업량 만큼 실음
                        if totalS + w[index] > b: #작업량을 실을때 최대를 넘어갈경우
                            truck[1] += b-totalS
                            totalS += b-totalS
                            s[index] -= b-totalS
                        else:
                            truck[1] += w[index]
                            totalS += w[index]
                            s[index] -= w[index]
                    else: # 가지고있는 금이 조금일경우
                        # 나머지 금 모두 실음
                        if totalS + s[index] > b: #남은 금을 실을때 최대를 넘어갈경우
                            truck[1] += b-totalS
                            totalS += b-totalS
                            s[index] -= b-totalS
                        else:
                            truck[1] += w[index]
                            totalS += w[index]
                            s[index] -= w[index]
                        answer[index] += i
        
                        print("시간 = ", time)
                        print("index = ", index)
                        print("answer = ", answer)
                        print("totalG = ", totalG)
                        print("totalS = ", totalS)
                        print("truck = ", truck)
                        print("g = ", g)
                        print("s = ", s)

        time+=1
    print("final totalG = ", totalG)
    print("final totalS = ", totalS)
    print("answer = ", answer)
    return time

    
print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))