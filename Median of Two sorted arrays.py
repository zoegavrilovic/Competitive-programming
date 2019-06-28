T=int(input())
while(T>0):
    nm=input().strip().split()
    n=int(nm[0])
    m=int(nm[1])
    arr=[int(x) for x in input().strip().split()]
    brr=[int(x) for x in input().strip().split()]

    arr=arr+brr  #just merging them
    arr.sort()  #and sorting
    #print(arr)
    r=m+n  #new size
    if(r%2==0):
        median=(arr[r//2-1]+arr[r//2])//2
    else:
        median=arr[r//2]

    print(median)
    T-=1

#EEZEH    
