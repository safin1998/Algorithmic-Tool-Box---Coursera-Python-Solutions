#Uses python3

import sys

def max_dot_product(a, b):
    n=len(a)
    res=0
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(n):
        res+=a[i]*b[i]
    return res

if __name__ == '__main__':
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    print(max_dot_product(a, b))
    
