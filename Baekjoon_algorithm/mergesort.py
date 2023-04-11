from collections import deque
def merge(L1, L2):
    L = []
    while L1!=[] and L2!=[]:
        if L1[0] <= L2[0]:
            L.append(L1.pop(0))
        else:
            L.append(L2.pop(0))
    while L1!=[]:
        L.append(L1.pop(0))
    while L2!=[]:
        L.append(L2.pop(0))
    print(f'merged list = {L}')
    return L

def merge_sort(L):
    length = len(L)//2
    if len(L) > 1:
        L1 = L[:length]
        L2 = L[length:]
        print(f'L1 = {L1}')
        print(f'L2 = {L2}')
        merge_sort(L1)
        merge_sort(L2)
        L = merge(L1, L2)
        
        return L


def rMerge_sort(arr, l, r):
    if l<r:
        m = (l+r)//2
        rMerge_sort(arr, l, m)
        rMerge_sort(arr, m+1, r)
        rMerge(arr, l, m, r)
    
def rMerge(arr, l, m, r):
    L1 = arr[l:m+1]
    L2 = arr[m+1:r+1]
    l_idx=r_idx=0
    sorted_idx=l
    
    while l_idx < len(L1) and r_idx  < len(L2):
        if L1[l_idx] <= L2[r_idx]:
            arr[sorted_idx] = L1[l_idx]
            l_idx+=1
        else:
            arr[sorted_idx] = L2[r_idx]
            r_idx+=1
        sorted_idx+=1
    
    while l_idx < len(L1):
        arr[sorted_idx] = L1[l_idx]
        l_idx+=1
        sorted_idx+=1
    
    while r_idx < len(L2):
        arr[sorted_idx] = L2[r_idx]
        r_idx+=1
        sorted_idx+=1



L = [6,1,8,2,3,5,7,4]
rMerge_sort(L, 0, len(L)-1)
print(L)