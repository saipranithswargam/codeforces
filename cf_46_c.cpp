#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL); 
    long long n,k,s;
    cin>>n>>k;
    s=(n%2==0)?n/2:(n+1)/2;
    if( k<=s){
        cout<<2*k-1;
    }
    else{
        k=k-s;
        cout<<2*k;
    }


    return 0;
}
    