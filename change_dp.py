# Uses python3
import sys

def get_change(m):
    M = [0] * (m+1)
    if m == 0:
        return 0
    for i in range(1,m+1):
        B=[]
        if i - 1 >= 0:
            coin_1 = M[i-1] + 1
            B.append(coin_1)
        if i-3 >= 0:
            coin_3 = M[i-3] + 1
            B.append(coin_3)
        if i-4 >= 0:
            coin_4 = M[i-4] + 1
            B.append(coin_4)
        M[i] = min(B)
    return(M[m])

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
