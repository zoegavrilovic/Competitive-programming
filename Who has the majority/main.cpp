#include <bits/stdc++.h>
using namespace std;
void majorityWins(int arr[], int n, int x,int y);
int main() {

    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
        cin>>arr[i];

        int x,y;
        cin>>x>>y;
        majorityWins(arr,n,x,y);

    }

	return 0;
}

void majorityWins(int arr[], int n, int x,int y)
{
    int count_x=0;
    int count_y=0;
    for (int i=0;i<n;i++) {
        if(arr[i]==x)
            count_x++;
        else if (arr[i]==y)
            count_y++;
    }
    if(count_x>count_y)
        cout<<x;
    else if(count_y>count_x)
        cout<<y;
    else if(count_y==count_x)
        cout<<min(x,y);

    cout<<endl;
}
