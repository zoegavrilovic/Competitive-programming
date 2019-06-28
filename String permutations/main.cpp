#include<bits/stdc++.h>
using namespace std;
void permutation(string S);
int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		string S;
		cin>>S;
		permutation(S);
		cout<<endl;

	}
	return 0;
}
void swap(char *x,char *y) {
    char temp;
    temp=*x;
    *x=*y;
    *y=temp;
}
char* permute(char *a,int l, int r) {
    int i;
    if(l==r) {
        return a;
    } else {
        for(i=l;i<=r;i++) {
            swap((a+l),(a+i));
            permute(a,l+1,r);
            swap((a+l),(a+i));
        }
    }
}
unsigned int factorial(unsigned int n)
{
    if (n == 0)
       return 1;
    return n * factorial(n - 1);
}
void permutation(string S) {
    int n = S.length();
    char char_array[n+1];
    strcpy(char_array, S.c_str());
    string strmat[n];
    for(int i=0;i<n;i++) {
        strmat[i]=permute(char_array, 0, n-1);
    }
}
/*void sort(string S) {
    unsigned int n2=permutation(S.length());
    char t[n2];
    for(int i=1; i<S.length(); i++)
	{
		for(int j=1; j<S.length(); j++)
		{
			if(strcmp(S[j-1], S[j])>0)
			{
				strcpy(t, S[j-1]);
				strcpy(S[j-1], S[j]);
				strcpy(S[j], t);
			}
		}
	}
}
)*/
