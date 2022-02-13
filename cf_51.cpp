#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<int> p;
    int n,vn{0};
    float res,den;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>i;
        p.push_back(i);
    }
    for(int i=0;i<=n;i++){
        vn=vn+p[i];
    }
    cout<<vn<<endl;
    den=100*n;
    res=(double)vn/den;
    cout<<res<<endl;
    cout<<res*100<<endl;
    return 0;
}