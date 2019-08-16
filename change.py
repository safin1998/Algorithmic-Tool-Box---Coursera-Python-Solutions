# Uses python3
import sys

def get_change(m):
    cnt=0
    cnt=int(m/10)
    m=m%10
    if m==0:
        return cnt
    cnt+=int(m/5)
    m=m%5
    if m==0:
        return cnt
    cnt+=int(m/1)
    return cnt

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
