#include <iostream>
using namespace std;
int main() {
    long long int t;
    cin>>t;
    while(t--){
        long long int n,m;
        cin>>n>>m;
        string s;
        cin>>s;
        while (m--){
            for(int i=1;i<n-1;i++){
                if (( (s[i]==0) && (s[i+1]==1) ) || ((s[i]==0) && (s[i-1]==1))){
                    if (((s[i-1]==1)&&(s[i+1]==2))){
                        s[i]=1;
                        }
                }
        } 
        cout<<s; }
    }
 return 0;
}