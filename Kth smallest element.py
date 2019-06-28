T=int(input())
while(T>0):
    N=int(input())
    arr=[int(x) for x in input().strip().split()]
    K=int(input())
    arr.sort()
    print(arr[K-1])  #lol, why is this a medium?
    T=T-1
