#include <iostream>
using namespace std;
int main(){
    unsigned int t,n,count{0};
    cin>>t;
    while(t--){
        cin>>n;
        for(int i=1;i*i<n;i++){
            if(i*i<n){count=count+1;}
            if(i*i*i<n){count=count+1;}
            if(i*i==i*i*i)

        }
        cout<<count<<endl;
        count=0;
    }
    return 0;}
