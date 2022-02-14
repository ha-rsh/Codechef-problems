#include <iostream>
using namespace std;
#include<algorithm>

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int arr1[n], arr2[n];
        for(int i = 0; i < n; i++){
            cin>>arr1[i]>>arr2[i];
        }
        sort(arr1,arr1+n);
        sort(arr2,arr2+n);
        int temp1=0, temp2=0;
        for(int j=0; j<n; j++){
            while(j<n-1 && arr1[j] == arr1[j+1])
            {
                j++;
            }
            temp1++;
        }
        for(int j=0;j<n;j++){
            while(j<n-1&&arr2[j]==arr2[j+1])
            { 
                j++;
                }
            temp2++;
        }

        cout<<temp1+temp2<<endl;
    }
	// your code goes here
	return 0;
}