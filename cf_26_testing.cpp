#include <iostream>
using namespace std;
int main(){
    int t,n;
    string s;
    cin>>n>>t;
    cin>>s;
    while(t--){
        for(int i=0;i<n-1;i++){
            if((s[i] =='B')&& (s[i+1]=='G')){
                s[i] ='G';
                s[i+1] ='B';
                i++;
            }
        }
    }
    cout<<s;
    return 0;

}