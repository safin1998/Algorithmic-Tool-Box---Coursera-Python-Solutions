# Uses python3
import sys

'''def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
'''

def last_digit(n):
    if (n <= 1):
        return n
    else:
        F=[0,1]
        count=1
        while count < n:
            res=(F[count]+F[count-1])%10
            F.append(res)
            count+=1
        return res

if __name__ == '__main__':
    n = int(input())
    print(last_digit(n))
