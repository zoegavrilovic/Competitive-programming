#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int T;
	cin>>T;
	while(T--){
	    int num;
	    cin>>num;
	    int arr[num];
	    for(int i = 0; i<num; ++i)
	        cin>>arr[i];

	    int res[3] = {0};
	    maxProductSubsequence(arr, num, res);

	    if(res[0] == 0)
	        cout<<"Not Present";
	    else{
	    for(int i = 0; i<3; ++i)
	        cout<<res[i]<<" ";
	    cout<<" ";
	    }
	}
}
/*
Make a Greatest element array, by storing the greatest element, available at right side for every element.
Make the Largest Smaller Element Array. This can be done with the help of set​
Insert the element in set, and store the address returned.
If the address points to begin(), store -1, else store the value at the previous address.
Traverse the original array, multiply the element at original array, LS array and Greatest element array,
and store the maximum of all.
*/
//the other one

void maxProductSubsequence(int *arr , int n, int *res)
{
    int greatest[n];  //greatest from the right
    int lsmaller[n];  //largest smaller from the left
    greatest[n-1]=arr[n-1];
    int original[n];
    for(int i=0;i<n;i++) {
        original[i]=arr[i];
    }
    for(int i=n-2;i>=0;i--) {
        greatest[i]=std::max(arr[i],greatest[i+1]);
    }
    greatest[n-1]=-1;
    set<int>s;

    for(int i=0;i<n;i++) {
        auto j=s.insert(arr[i]);
        auto itc=j.first;
        --itc;
        if (itc != s.end())
            lsmaller[i]=*itc;
        else
            lsmaller[i]=-1;
    }
    lsmaller[0]=-1;
    int maxx=0;
    for(int i=0;i<n;i++) {
        if(greatest[i]!=-1)
            arr[i]=arr[i]*greatest[i];
        if(lsmaller[i]!=-1)
            arr[i]=arr[i]*lsmaller[i];
        if(arr[i]>maxx) {
            maxx=arr[i];
        }
    }
    int result[n];
    for(int i=0;i<n-1;i++) {
        if(maxx%original[i]==0) {
            result[i]=original[i];
        }
    }
    for(int i=0;i<n;i++) {
        cout<<result[i]<<" ";
    }
}
/*
void maxProductSubsequence(int *arr , int n, int *res)
{
    int greatest[n];
    for(int i=0;i<n;i++) {
        greatest[i]=max(greatest[i+1],arr[i])
    }
    int max1=0,max2=0,max3=0;
    for(int i=0;i<n;i++) {
        if(arr[i]>max1) {
            max3=max2;
            max2=max1;
            max1=arr[i];
        }
        else if(arr[i]<max1 && arr[i]>max2) {
            max3=max2;
            max2=arr[i];
        }
    }
    res[0]=max3;
    res[1]=max2;
    res[2]=max1;
}
*/
