int leftIndex(int sizeOfArray, int arr[], int elementToSearch){

    int left=lower_bound(arr,arr+sizeOfArray,elementToSearch)-arr;
    return left;

}

#include <iostream>
using namespace std;
//Position this line where user code will be pasted.
// Driver Code
int main() {

	// Testcase input
	int testcases;
	cin >> testcases;

    // Looping through all testcases
	while(testcases--){
	    int sizeOfArray;
	    cin >> sizeOfArray;

	    int arr[sizeOfArray];

	    // Array input
	    for(int index = 0; index < sizeOfArray; index++){
	        cin >> arr[index];
	    }

	    int elemntToSearch;
	    cin >> elemntToSearch;

	    cout << leftIndex(sizeOfArray, arr, elemntToSearch) << endl;
	}

	return 0;
}
