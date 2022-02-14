#include <iostream>
#include<vector>
#include<map>

using namespace std;

int main()
{
    int n,t,k,size;
    cin>>n>>t>>k;
    size = n+t+k;
    int arr[size];
    for(int i=0; i<size; i++)
    {
        cin>>arr[i];
    }
    vector<int>result;
    map<int,int>m;
    for(int i=0; i<size; i++)
    {
        m[arr[i]]++;
    }
    map<int,int>::iterator it;
    for(it = m.begin(); it!=m.end(); it++)
    {
        if (it->second >= 2) 
            result.push_back(it->first);
    }
    cout<<result.size()<<endl;
    for(int i=0; i<result.size();i++)
    {
        cout<<result[i]<<endl;
    }

    return 0;
}

