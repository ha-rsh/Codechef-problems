#include <bits/stdc++.h>
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define lld long long double

/*#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;*/

#define dbug(x) cout << #x << " " << x << "\n";
#define loop(n) for(int i = 0; i < n; i++)
#define loop2(n) for(int j = 0; j < m; j++)
#define ve vector<ll>
#define ft first
#define imin INT_MIN
#define imax INT_MAX
#define st second
#define pb push_back
#define pob pop_back
#define mpr make_pair
#define mp map<ll, ll>
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define pr pair<ll, ll>
#define all(c) (c).begin(), (c).end()
#define EACH(x, a) for (auto& x: a)
using namespace std;

void solve(){
    ll n;
    cin >> n;
    ve ar(n);
    loop(n){
        cin >> ar[i];
    }
    sort(all(ar), greater<int>());
     int j = n - 1;
     while(ar[j] == ar[n - 1])
      j--;
    ll ans=(ll)n * ((ll)ar[n - 1]) + (ll)(j + 1);
    cout << ans << "\n";
}

int main(){
    ll t;
    cin >> t;
    while(t--){
    solve();
    }
}
        
