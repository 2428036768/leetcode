
def validMountainArray(A):
    j = 0
    if not A or len(A) == 1:
        return False
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            continue
        elif A[i] == A[i+1] or i == 0:
            return False
        else:
            j = i+1
    while j != len(A)-1:
        if A[j] > A[j+1]:
            j += 1
        else:
            return False
    return True

print(validMountainArray([3,7,6,4,3,0,1,0]))
