#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int k,l,i{1};
    int s=k;
    cin>>k>>l;
    for(int i=1;k<=l;i++){
        if(k==l){
            cout<<"YES";
        }
        else{
            k=pow(s,i);
            cout<<i<<endl;
            cout<<k<<endl;
        }
    }
    cout<<"NO";
    return 0;

}