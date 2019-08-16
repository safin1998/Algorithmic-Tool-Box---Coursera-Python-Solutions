# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge(n,m):
    if (n <= 1):
        return n
    else:
        F=[0,1]
        H=[0,1]
        count=1
        while True:
            res=F[count]+F[count-1]
            count+=1
            F.append(res)
            H.append(res%m)
            if H[count]==1 and H[count-1]==0 and count>1:
                break
    
    rem=n%(len(H)-2)
    ans=(F[rem])%m
    return ans
        
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
