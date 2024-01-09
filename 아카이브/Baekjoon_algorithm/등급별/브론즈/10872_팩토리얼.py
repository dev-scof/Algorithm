def recursive_factorial(num):
    if num==1:
        return 1
    else:
        return recursive_factorial(num-1) * num
