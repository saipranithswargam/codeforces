#include <iostream>
using namespace std;
int main(){
    int n{0},x{0},t{0},sum{0};
    cin>>t;

    while(t--){
        cin>>n>>x;
        int val[n]={0};
        for(int i=0;i<n;i++){
            cin>>val[i];
        }
        for(int i=0;i<n;i++){
            sum=sum+val[i];
            if(sum>=x){
                cout<<i;
                break;
            }
        }
        


    }
}