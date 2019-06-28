from collections import Counter
T=int(input())
while(T>0):
    N=int(input())
    arr=[int(x) for x in input().strip().split()]
    c=Counter(arr)
    for index,key in enumerate(c):
        if(c[key]>1):   #c[key] is the value of key
            print(key,c[key])
    T-=1
