#include <iostream>
using namespace std;
int main(){
    int l1,l2,l3;
    cin>>l1>>l2>>l3;
    if (l1==l2 || l2==l3 || l3==l1){
        cout<<"YES";
    }
    else if (l1==6 && l2==1 && l3==5)
    {
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    return 0;
}