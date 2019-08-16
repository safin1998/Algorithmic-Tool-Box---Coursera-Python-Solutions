# Uses python3


'''def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence) '''

def primitive_calculator(n):
    if n==1:
        return [1]
    if n==2:
        return [1, 2]
    if n==3:
        return [1, 3]
    res = 1
    L = [0,0,1,1]
    S = [1]
    A=[]
    for i in range(4,n+1):
        val1 = L[i - 1] + 1
        val2 = L[i // 2] + 1 if i % 2 == 0 else float("inf")
        val3 = L[i // 3] + 1 if i % 3 == 0 else float("inf")
        steps=min(val1, val2, val3)
        L.append(steps)
    return(L)

def backtracking(L,n):
    A = [n]
    while L[n] != 1:
        val1 = L[n - 1] + 1
        val2 = L[n // 2] + 1 if n % 2 == 0 else float("inf")
        val3 = L[n // 3] + 1 if n % 3 == 0 else float("inf")
        m = min(val1, val2, val3)
        if m == val1:
            n = n-1
            A.append(n)
        elif m == val2:
            n = n//2
            A.append(n)
        else:
            n = n//3
            A.append(n)
    A.append(1)
    return A

n = int(input())
operations = (primitive_calculator(n))
if operations == [1,2] :
     print (1)
     print (1, 2)
elif operations == [1]:
     print (0)
     print (1)
elif operations == [1,3]:
     print (1)
     print (1, 3)
else:
    sequence = backtracking(operations, n)
    print(len(sequence)-1)
    for x in range(len(sequence)-1, -1, -1):
        print(sequence[x], end=' ')
