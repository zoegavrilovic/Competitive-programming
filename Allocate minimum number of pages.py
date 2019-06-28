def isValid(arr,n,k,ans):
    s=0   #initializing sum of pages to be added up to 0
    students=1  #each student MUST read a book, so no point for this to start from 0
    for i in range(0,n):
        if arr[i]>ans:  #if the arrray element itself is larger than the mid point, no point of adding up, this case is not valid already
            return 0
        sums=s+arr[i]
        if sums>ans:   #if the sum exceedes the mid point, we give another student the next pages
            students=students+1
            s=arr[i]   #and the sum of pages for that student starts at current i because he continues reading the rest of the pages
            if students>k:   #if the number of students exceeded the actual number of students (which means that the mid point of this case
            #is NOT the maximum of pages that can be allocated to a student), break out
                return 0
        else:
            s=sums  #adding up the pages
    return 1   #if the loop doesn't break anywhere (doesn't return 0),
    #it means that this is a valid configuration, NOT neccessarilly the minimum one, but correct one

def binarySearch(arr,n,k):
    start=max(arr)   #no need to start from 0 because 0 is not the minimum maximum of pages for a student, the actual maximum is...or???
    final=-1   #in case this is impossible, final will return -1
    end=sum(arr)  #the upper bound for binary search is sum of the array because that's the total number of pages and it's the range where
    #we try to find the minimum maximum of allocated pages ??? not really clearest
    while start<=end:  #searching between the max number of array and sum of array
        mid=start+(end-start)//2
        if isValid(arr,n,k,mid):  #checking if this mid is the minimum maximum of pages to be allocated
            final=mid  #keeping track of the feasible configuration so it could be returned after everything is done
            end=mid-1  #if the configuration IS valid, we try to find a better...minimaler xD one by limiting searching to the
            #right half of array where smaller numbers to be checked are
        else:
            start=mid+1  #and if the configuration is not valid, that means the solution should be...maximer xD
            #hence we move to the right half of the array
    return final

T=int(input())
while(T>0):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    k=int(input())
    if k>n:  #can't split 3 books on 4 kids x)
        print (-1)
    #arr.sort()
    else:
        print(binarySearch(arr,n,k))
    T-=1
