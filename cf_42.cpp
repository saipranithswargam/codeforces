#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int mag[n];
    for(int i=0;i<n;i++){
        cin>>mag[i];
        }
    int count{n};
    for(int i=1;i<n;i++){
        if(mag[i]==mag[i-1]){
            count=count-1;
        }
    }
    cout<<count;
    return 0;
}