#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){

    int tc = 0, t = 1;
    cin >> t;
    while (tc++ < t)
    {
        // declaring variables
        ll n, k;
        // input parameters
        cin >> n >> k;
        vector<ll> arr(1, 1);  //creating vector
        k -= n;

        ll current = 2;       

        for (int i = 2; i <= n; i++) {
            if (k < arr.size()) {
                int ele = arr[arr.size()- k- 1];
                arr.push_back(ele);
                break;
            }
            k -= arr.size();
            arr.push_back(current);
            current++;
        }

        while (arr.size() < n) {
            arr.push_back(arr.back());
        }

        for(auto i: arr){
            cout << i << " ";
        }cout << endl;

    }

    return 0;
}