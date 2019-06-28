#We need to use Sliding window Method to solve this Problem.

#Add the elements, to currsum till it is less than S.
#If it becomes more than S, start deleting elements from start
#in the cuusum. if the currsum again becomes less than S,
#again start adding elements to it. In between also check,
#if the currsum becomes equal to S.
#If yes, then output start and end index,
#else after traversing array no such solution is found, output -1.
#FIX THIS
def subArraySum(arr, n, s):
    start=0
    sums=0
    for i in range(0,n):
        sums=sums+arr[i]
        #print(sums)
        if sums==s:
            print(start+1,i+1,end="")
            break
        if sums>s:
            sums=sums-arr[start]
            start=start+1
            if sums==s:
                print(start+1,i+1,end="")
                break
            while(sums>s):

                sums=sums-arr[start]
                start=start+1
                #print("you are here")
    if sums!=s:
        print(-1,end="")
    #print (start,i,sums)
import math
def main():
        T=int(input())
        while(T>0):
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            A=list(map(int,input().split()))
            subArraySum(A, N, S)
            print()
            T-=1
if __name__ == "__main__":
    main()
