#include <stdio.h>

int main() {
    int numbTemps,temp;
    int total=0;
    scanf("%d",&numbTemps);
   
    //for each temperature, if negative add to total 
    for(int i=0; i<numbTemps;i++) {
         scanf("%d",&temp);
         total+=temp<0?1:0;
    }    

    //prints result
    printf("%d",total);
    return 0;
}
