#include <stdio.h>
#include <math.h>
void insert(int arr[], int i);
/* Function to sort an array using insertion sort*/
void insertionSort(int arr[], int n)
{
   int i;
   for (i = 1; i <n; i++)
      insert(arr, i);
}
/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("
");
}
// Driver program to test above functions
int main()
{
    int arr[1000],n,T,i;
    scanf("%d",&T);
    while(T--){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
    insertionSort(arr, n);
    printArray(arr, n);
    }
    return 0;
}
void insert(int arr[], int i)
{
    int j,key=arr[i];
    for(j=i-1;j>=0 && arr[j]>key;j--) {
        arr[j+1]=arr[j];
    }
    arr[j+1]=key;
}
