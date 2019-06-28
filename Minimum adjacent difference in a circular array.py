def minAdjDiff(arr, n):
    m=abs(arr[0]-arr[n-1])
    for i in range(0,n-1):
        if abs(arr[i]-arr[i+1])<m:
            m=abs(arr[i]-arr[i+1])
    return m

def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(minAdjDiff(arr,n))
        T-=1
if __name__=="__main__":
    main()
