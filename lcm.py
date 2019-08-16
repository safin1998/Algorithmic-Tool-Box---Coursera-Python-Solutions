# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a,b):
    rem=1
    if b>a:
        while True:
            rem=b%a
            if rem!=0:
                b=a
                a=rem
            else:
                break
        return a
        
    elif a==b:
        return a
        
    else:
        while True:
            rem=a%b
            if rem!=0:
                a=b
                b=rem
            else:
                break
        return b


def lcm(a,b):
    if a==0 or b==0:
        return 0
    m=int((a*b)/gcd(a,b))
    return m
    

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

