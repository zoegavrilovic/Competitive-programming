#include <iostream>
#include <climits>
using namespace std;
void largestAndSecondLargest(int, int[]);
int main() {
	int testcases;
	cin >> testcases;

	while(testcases--){
	    int sizeOfArray;
	    cin >> sizeOfArray;

	    int arr[sizeOfArray];

	    for(int index = 0; index < sizeOfArray; index++){
	        cin >> arr[index];
	    }

	    largestAndSecondLargest(sizeOfArray, arr);
	}

	return 0;
}

void largestAndSecondLargest(int sizeOfArray, int arr[]){
    int max = INT_MIN, max2= INT_MIN;
    int i;
    int n=sizeOfArray;
    for(i=0;i<n;i++) {
        if(arr[i]>max)
            max=arr[i];
    }
    for(i=0;i<n;i++) {
        if(arr[i]==max)
            arr[i]=INT_MIN;
    }
    for(i=0;i<n;i++) {
        if(arr[i]>max2)
            max2=arr[i];
    }
    if(max2==INT_MIN)
        max2=-1;
    cout<<max<<" "<<max2;
    cout<<endl;
}
//a little faster, in one loop:
/* if(arr[i] > max)
{
       max2 = max
       max = arr[i]
}

else if(arr[i] > max2 && arr[i] != max)
{
     max2 = arr[i];
} */
