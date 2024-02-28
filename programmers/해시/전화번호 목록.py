def solution_1(phone_book):
    phone_book.sort(key=lambda x: len(x))
    N = len(phone_book)
    for i in range(N):
        for j in range(i+1, N):
            if (
                phone_book[i] in phone_book[j]
                and phone_book[j].find(phone_book[i]) == 0
            ):
                return False
    return True


def solution2(phone_book):
    phone_book.sort(key=lambda x: len(x))
    N = len(phone_book)
    for i in range(N):
        for j in range(i+1, N):
            if len(phone_book[i]) > len(phone_book[j]):
                break
            if (
                phone_book[i] in phone_book[j]
                and phone_book[j].find(phone_book[i]) == 0
            ):
                return False
    return True


def solution3(phone_book):
    phone_book.sort(key=lambda x: len(x))
    N = len(phone_book)
    for i in range(N):
        for j in range(i+1, N):
            if len(phone_book[i]) > len(phone_book[j]):
                break
            if phone_book[i] in phone_book[j]:
                for k in range(len(phone_book[i])):
                    if phone_book[i][k] != phone_book[j][k]:
                        break
                else:
                    return False
    return True


def solution4(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)
    while phone_book:
        prefix = phone_book.pop()
        prefixes = set(x[:len(prefix)] for x in phone_book)
        if prefix in prefixes:
            return False
    return True


def solution5(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)
    while phone_book:
        prefix = phone_book.pop()
        if not phone_book:
            return True
        if len(prefix) > len(phone_book[-1]):
            return True
        if prefix in set(x[:len(prefix)] for x in phone_book):
            return False
    return True


def solution6(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)
    while phone_book:
        prefix = phone_book.pop()
        if not phone_book:
            return True
        if len(prefix) >= len(phone_book[0]):
            return True
        if prefix in set(x[:len(prefix)] for x in phone_book):
            return False
    return True

def solution7(phone_book):
    phone_book.sort(key=lambda x: (len(x), x), reverse=True)
    while phone_book:
        prefix = phone_book.pop()
        if not phone_book:
            return True
        if len(prefix) >= len(phone_book[0]):
            return True
        for phone in sorted([x[:len(prefix)] for x in phone_book], key=lambda x: x[:len(prefix)]):
            if prefix == phone:
                return False
            if phone > prefix:
                break
    return True


def solution8(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)
    while phone_book:
        prefix = phone_book.pop()
        if not phone_book:
            return True
        if len(prefix) >= len(phone_book[0]):
            return True
        for phone in phone_book:
            for k in range(len(prefix)):
                if phone[k] != prefix[k]:
                    break
            else:
                return False
    return True


def solution9(phone_book):
    phone_book.sort(reverse=True)
    while phone_book:
        prefix = phone_book.pop()
        for phone in phone_book:
            if phone.startswith(prefix):
                return False
    return True


def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(f'sorted_phone = ', phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True

if __name__ == '__main__':
    print(solution(["97674223", "1195524421", "119"]))
    print(solution(["123","456","789"]))
    print(solution(["12","233","113235","567","88"]))