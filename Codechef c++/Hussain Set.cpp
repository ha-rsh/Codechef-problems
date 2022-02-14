#include<iostream>
#include<algorithm>
#include<queue>
typedef long long ll;
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    ll arr[n];
    for(int i=0;i<n;i++)
       cin >> arr[i];
    sort(arr, arr+ n);
    int end_p=n-1;
    queue<ll> q;
    int count_m = 0;
    for(int i=0; i<m; i++)
    {
        int curr_m;
        cin>> curr_m;
        ll ans = 0;
        while(count_m<curr_m)
        {
            if(q.size() == 0)
            {
                ans = arr[end_p];
                end_p--;
                if(ans / 2 > 0)
                {
                    q.push(ans/2);
                }
            }
            else if(end_p >=0 && (arr[end_p] > q.front()))
            {
                ans = arr[end_p];
                if(ans / 2 > 0)
                {
                    q.push(ans/2);
                }
                end_p--;
            }  
            else
            {
                ans = q.front();
                q.pop();
                if(ans / 2 > 0)
                {
                    q.push(ans/2);
                }
            } 
            count_m++; 
        }
        cout<< ans << endl;
    }

    return 0;
}