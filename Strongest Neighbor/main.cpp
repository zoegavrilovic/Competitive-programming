#include <iostream>
#include <climits>
using namespace std;
void maximumAdjacent(int, int[]);
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
	    maximumAdjacent(sizeOfArray, arr);
	    cout << endl;
	}

	return 0;
}

void maximumAdjacent(int sizeOfArray, int arr[]){
    int n=sizeOfArray;
    int i;
    for(i=0;i<n-1;i++) {
        if(arr[i]>arr[i+1])
            cout<<arr[i]<<" ";
        else
            cout<<arr[i+1]<<" ";
    }

}
/* This problem is based on window sliding method. Take window of size 2 and iterate through whole array.

Algorithm:

Start window of size two taking the first two elements of the array in the window.
Lower index of window is at 0th index and higher is at 1st index.
Now, take maximum of the two.
Now, increase the lower index and higher index by 1, to keep window of size 2.
In this way, slide the window through whole array and each time store maximum of current window with max stored.
*/
