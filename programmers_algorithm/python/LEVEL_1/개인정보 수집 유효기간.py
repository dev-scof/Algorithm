def make_terms(term):
    terms = {}
    for t in term:
        tp, mon = t.split()
        terms[tp]=int(mon)
    return terms

def make_expire_date(date, month):
    date[1]+=month # add month
    # month가 12가 넘어가면
    if date[1]>12:
        date[0]+=date[1]//12 # year 갱신
        date[1]%=12 # month 갱신
        if date[1]==0: # 만약 month가 12의 배수이면
            date[1]=12 # month를 12로 지정
            date[0]-=1 # year 갱신
        
    date[2]-=1 # day 갱신
    if date[2]==0: # day가 0이면
        date[2]=28 # day 28로 갱신
        date[1]-=1 # month 갱신
        if date[1]==0: # month가 0이면
            date[1]=12 # month를 12로 갱신
            date[0]-=1 # year 갱신
    return date
def check_expire(expire_date, today_date):
    # 연도 비교
    if expire_date[0] < today_date[0]:
        return False
    elif expire_date[0] == today_date[0]:
        # 연도가 같으면, 월 비교
        if expire_date[1] < today_date[1]:
            return False
        elif expire_date[1] == today_date[1]:
            # 월도 같으면 일 비교
            if expire_date[2] < today_date[2]:
                return False
    return True

def solution(today, terms, privacies):
    answer = []
    terms = make_terms(terms)
    today = list(map(int, today.split('.'))) # 0:year, 1:month, 2:day
    
    for i, privacy in enumerate(privacies):
        date, typ = privacy.split()
        date = list(map(int, date.split('.'))) # 0:year, 1:month, 2:day
        make_expire_date(date, terms[typ]) # add term day

        if not check_expire(date, today):
            answer.append(i+1)    
    return answer
            

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2021.12.08", ["A 18"], ["2020.06.08 A"]))