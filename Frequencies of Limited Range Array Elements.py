from collections import Counter
def printfrequency(A,N):
    C=Counter(A)  #dictionary of value in array: num of occurrences
    B=[0]*N
    for i in range(1,N+1):
        B[i-1]=C[i]
        print(B[i-1],end=" ")
#execution 2.3 :/

#Their way:
#1)  Subtract 1 from every element so that the elements
#    become in range from 0 to n-1
#    for (int j =0; j < n; j++)
#        arr[j] = arr[j]-1;

#2)  Use every element arr[i] as index and add 'n' to
#    element present at arr[i]%n to keep track of count of
#    occurrences of arr[i]
#    for (int i=0; i < n; i++)
#        arr[arr[i]%n] = arr[arr[i]%n] + n;

#3)  To print counts, simply print the number of times n
#    was added at index corresponding to every element
#    for (int i =0; i < n; i++)
#        print "(i + 1) -> arr[i] "

import math
def main():
    T=int(input())
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        printfrequency(A,N)
        print()
        T-=1
if __name__=="__main__":
    main()
