#include <iostream>
#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() 
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        ll x;
        cin >> x;
        
        ll a = x,b = 0,c = x;
        for(ll i=0;i<31;i++) 
        {
            if(!(c&((ll)1<<i)))
            {
                c = c | ((ll)1<<i);
                break;
            }
        }
    
        cout<<a<<" "<<b<<" "<<c<<endl;
    }

  return 0;
}
