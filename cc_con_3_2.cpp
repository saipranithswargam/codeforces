#include <iostream>
using namespace std;
int main(){
    int test;
    cin>>test;
    for(int i=0; i<test ; i++){
        int num=52,count=0,k;
        cin>>k;
        for(int i=0;i<=num;i++){
            if (num%k==0){
                cout<<count<<endl;
                break;
            }
            else if(num%k!=0){
                num--;
                count++;
            }
        }
    }
    return 0;
}