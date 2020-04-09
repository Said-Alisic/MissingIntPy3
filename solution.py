def solution(A):
    
    if len(A) > 1:
        A.sort(reverse = True)
        return missing_int(A)
    elif A[0] != 1:
        return 1
    else:
        return 2
        
def missing_int(A):

    result = A[0] + 1
    counter = 0

    for i in range(len(A) - 1):
        if A[i] < 0:
            break

        elif (A[i + 1] + 1) < A[i] and A[i + 1] > 1:
            result = A[i + 1] + 1
            
        if A[i + 1] > 0:
            counter = A[i + 1]
    
    if counter != 1:
            result = 1
    
    return int(result)