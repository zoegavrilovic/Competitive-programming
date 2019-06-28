#gave up to see their solution:

#Use Merge sort algorithm, and sort the array.
#In merge function for merge sort, while comparing the elements, if element in right array is smaller,
#then it is an inversion (Why..??)
#This means that this smaller element in the original array, is behind larger elements.
#So add the number of larger elements or elements left in the left array, to the value of counter.
#This process is repeated again and again for complete Merge Sort

inversion_count=0  #global variable to count total inversions

def Inversion_Count(a,n):
    global inversion_count
    inversion_count = 0
    merge_sort(a, 0, n - 1)
    return inversion_count

#merger of two halves .. counting inversion at each step
def merge(a, start, mid, end):
    global inversion_count
    temp = [0 for i in range(end - start + 1)]
    i, j, k = start, mid + 1, 0  # indexes of left,right and temp arrays

    # merge while conditions are valid
    while (i <= mid and j <= end):

        # compare the elements and merge
        if (a[i] <= a[j]):
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
            inversion_count += mid - i + 1 # inversion occurs here as right moved ahead of left ?????

    # storing the rest elements
    while (i <= mid):
        temp[k] = a[i]
        k += 1
        i += 1

    # storing the rest elements
    while (j <= end):
        temp[k] = a[j]
        k += 1
        j += 1

    for i in range(start, end + 1):
        a[i] = temp[i - start]

#merge utility
def merge_sort(a,start,end):
    if (start < end):
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid + 1, end)
        merge(a, start, mid, end)

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(Inversion_Count(a,n))
