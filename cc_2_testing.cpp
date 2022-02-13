#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n{0},x{0},t{0},sum{0};
    cin>>t;

    while(t--){
        cin>>n>>x;
        int val[n];
        for(int i=0;i<n;i++){
            cin>>val[i];
            sum=sum+val[i];
        }
        if(sum<x){cout<<-1<<endl;continue;}
        sort(val, val + n, greater<int>());//sorting of array in descending in cpp
        sum=0;
        for(int i=0;i<n;i++){
            sum=sum+val[i];
            if(sum>=x){
                cout<<(i+1)<<endl;
                sum=0;
                break;
            }
            
        }
        


    }
    return 0;
}