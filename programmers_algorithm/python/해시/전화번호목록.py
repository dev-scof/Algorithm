def solution(phone_book):
    for i in phone_book:
        temp = phone_book.copy()
        temp.pop(temp.index(i))
        for j in temp:
            if i == j[:len(i)]:
                return False
    return True
print(solution(['12','123','1235','567','88']))