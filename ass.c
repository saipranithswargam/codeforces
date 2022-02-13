#include <stdio.h>
int main(){
    int n,rev,rem;
    scanf("%d",&n);
    for(int i=0;n!=0;i++ ){   
        rem=n%10;
        rev= rev*10 +rem;
        n=n/10;
        }
        printf("%d",rev);
        return 0;

}