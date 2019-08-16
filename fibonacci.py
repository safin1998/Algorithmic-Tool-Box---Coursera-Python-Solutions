# Uses python3
'''def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
'''

def fibbo(n):
    if (n <= 1):
        return n
    else:
        F=[0,1]
        count=1
        while count < n:
            res=F[count]+F[count-1]
            F.append(res)
            count+=1
        return F[n]
    
n = int(input())
print(fibbo(n))
