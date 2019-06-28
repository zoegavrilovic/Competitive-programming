from collections import Counter
def twoRepeated(arr,n):
    c=Counter(arr)  #elements of arr are keys, nums of occurrences are values
    li=[]
    for key,value in c.items():  #unfortunately iterates in sorted key order, not preserving order of elements in arr
        #print(c[index])
        if(value>1):  #if a key is found twice
            li.append(key)
    occ1=len(arr)-arr[::-1].index(li[0])-1  #finding last occurrence of first key (I think this is O(n))
    occ2=len(arr)-arr[::-1].index(li[1])-1  #finding last occurrence of second key
    if(occ1<occ2):
        print(li[0],li[1])
    else:
        print(li[1],li[0])

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            twoRepeated(A,N)
            T-=1
if __name__ == "__main__":
    main()
