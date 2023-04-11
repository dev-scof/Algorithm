number=1
created_numbers=set()
def is_self_number(number):
    created_number = number
    for num in str(number):
        created_number+=int(num)
    created_numbers.add(created_number)
    if number not in created_numbers:
        return True
    else:
        return False
    
while number <= 10000:
    result = is_self_number(number)
    if result:
        print(number)
    number+=1