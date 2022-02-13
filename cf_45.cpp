#include <iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(auto x:a){
        if(x==1){
            cout<<"HARD";
            return 0;
        }
        }
    cout<<"EASY";
    return 0;
    
    
}