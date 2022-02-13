#include <iostream>
using namespace std;
int main(){
    int n,a{0},d{0};
    cin>>n;
    string s;
    cin>>s;
    for(auto x : s){
        if(x=='A'){
            a=a+1;

        }
        else{
            d=d+1;
        }
        }
        if (a>d){
            cout<<"Anton";
        }
        else if(a<d){
            cout<<"Danik";
        }
        else{
            cout<<"Friendship";
        }
        return 0;
}