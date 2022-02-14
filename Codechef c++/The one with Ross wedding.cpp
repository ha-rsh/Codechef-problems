#include <bits/stdc++.h>
using namespace std;

#define ll          long long
#define vi          vector<int>
#define vll         vector<ll>
#define pll         pair<ll, ll>
#define pii         pair<int, int>
#define ld          long double
#define ff          first
#define ss          second
#define vs          vector<string>
#define vpll        vector<pll>
#define vb          vector<bool>
#define mp          make_pair
#define pb          push_back
#define endl        '\n'

const ll INF       = 2e18;
const ll mod       = 1000000007;
const ll mod2      = 998244353;




signed main(){

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif



    int tc = 0, tt = 1;
    cin >> tt;
    while (tc++ < tt)
    {

        ll n, p, q;
        cin >> n >> p >> q;

        p = abs(p), q = abs(q);

        string s;
        cin >> s;

        vll arr(2);

        ll idx = 0;

        for(auto x: s){
            if(x == '0'){
                idx ^= 1;
            }
            arr[idx]++;
        }

        if(arr[0] >= p and arr[1] >= q){
            if(((arr[0] - p)%2 == 0) and ((arr[1] - q)%2 == 0)){
                cout << "YES" << endl;
                continue;
            }
        }

        if(arr[1] >= p and arr[0] >= q){
            if(((arr[0] - q)%2 == 0) and ((arr[1] - p)%2 == 0)){
                cout << "YES" << endl;
                continue;
            }
        }

        cout << "NO" << endl;




    }

    return 0;
}
