def toString(List):
    return ''.join(List)

def permute(a,l,r,answer):
    if l==r:
        answer.append(toString(a))  #if only one char is left(ABC-BC-C), append the permuted string to list
    else:
        for i in range(l,r+1):  #first and last char
            a[l],a[i]=a[i],a[l]  #swapping 2 characters that are not locked
            permute(a,l+1,r,answer)  #recursion call for the n-1 substring (if ABC- call for BC)
            a[l],a[i]=a[i],a[l] #backtrack, swapping again to get the string back to original

def permutation(S):
    a=list(S)
    n=len(S)
    answer=[]
    permute(a,0,n-1,answer)
    answer.sort()
    for i in answer:
        print(i,end=" ")

import math
def main():
    T=int(input())
    while(T>0):
        S=input()
        permutation(S)
        print()
        T-=1
if __name__=="__main__":
    main()
