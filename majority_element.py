# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def majorityElement(A,n):
    if n==1:
        return 1
    A.sort()
    B=[]
    i=0
    flag=0
    for i in range(1,len(A)):
        if i<len(A):
            if A[i]==A[i-1]:
                if flag==0:
                    temp=i-1
                    flag=1
                if i==len(A)-1:
                    B.append(1+i-temp)
                
            else:
                if flag==1:
                    B.append(i-temp)
                    flag=0
    
    for i in B:
        if i > n/2:
            return 1
    return 0
            
if __name__ == '__main__':
    n=int(input())
    a=[int(x) for x in input().split()]
    print(majorityElement(a,n))
