#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,count=1,p;
    vector<int> a;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i=1;i<n;i++){
        if((arr[i-1])<=(arr[i])){
            count+=1;
        }
        else{
            a.push_back(count);
            count=1;
        }
    }
        a.push_back(count);
        cout<<*max_element(a.begin(), a.end())<<endl;
    return 0;
}