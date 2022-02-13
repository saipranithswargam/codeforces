#include <iostream>
using namespace std;
int main(){
    int perb,ind,nob,cost{0},borr;
    cin>>perb>>ind>>nob;
    for(int i=1;nob>0;i++){

        cost=cost+i*perb;
        nob=nob-1;


    }
    borr=cost-ind;
    if (borr>0){
        cout<<borr;

    }
    else{
        cout<<0;
    }
    return 0;

    
}