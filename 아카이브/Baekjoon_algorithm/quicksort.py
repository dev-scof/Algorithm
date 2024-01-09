def partition(L, k):
    p = L[k] # 피벗
    LT, EQ, GT = [], [], []
    for e in L:
        if e < p:
            LT.append(e)
        elif e == p:
            EQ.append(e)
        else:
            GT.append(e)
    return (LT, EQ, GT)
def quickSort(L):
    if len(L) > 1:
        k = len(L)-1 # 피벗을 맨 뒤로 잡음
        LT, EQ, GT = partition(L, k)
        LT = quickSort(LT)
        GT = quickSort(GT)
        L = LT+EQ+GT
    return L

import random
def inPlaceQuickSort(L, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a, b = inPlacePartition(L, l, r, k)
    inPlaceQuickSort(L, l, a-1)
    inPlaceQuickSort(L, b+1, r)
    return L

def inPlacePartition(A, l, r, k):
    p = A[k]
    A[k], A[r] = A[r], A[k]
    i = l
    j = r-1
    while i <= j:
        while i<=j and A[i] <= p:
            i += 1
        while i<=j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[i], A[r] = A[r], A[i]
    return i, j


L = [6,1,8,2,3,3,5,7,4]
L = inPlaceQuickSort(L, 0, len(L)-1)
print(L)