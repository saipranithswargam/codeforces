#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
    int test,array_size;
    unsigned long long int num_iterations;
    string s,res;
    cin>>test;
    while(test--){
        cin>>array_size>>num_iterations;
        cin>>s;
        res=s;
        int num=array_size>num_iterations ? num_iterations:array_size;
        while(num--){
            
            for(int i=1;i<array_size;i++){
                if((((s[i]=='0')&&(s[i-1]=='1'))||((s[i]=='0')&&(s[i+1]=='1'))) && (!((s[i-1]=='1')&&(s[i+1]=='1')))){
                    res[i]='1';
                    // i++;
                }
                if((s[0]=='0') &&(s[1]=='1')){
                    res[0]='1';
                }
                if((s[array_size]=='0') && (s[array_size-1]=='1')){
                    res[array_size]='1';
                }




            }
            s=res;
        
        }
        cout<<res<<endl;




}

return 0;

}