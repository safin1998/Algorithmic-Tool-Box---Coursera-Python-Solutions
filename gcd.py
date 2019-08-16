# Uses python3
import sys

'''def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
'''
    
if __name__ == "__main__":
    a, b = map(int, input().split())
    rem=1
    if b>a:
        while True:
            rem=b%a
            if rem!=0:
                b=a
                a=rem
            else:
                break
        print(a)
        
    elif a==b:
        print(a)
        
    else:
        while True:
            rem=a%b
            if rem!=0:
                a=b
                b=rem
            else:
                break
        print(b)

