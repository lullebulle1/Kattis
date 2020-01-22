#include <stdio.h>
#include <math.h>

int main() {
    int days, a, candles;
    scanf("%d",&days);
    
    //For each test case, print out the number of candles needed
    for (int i=0;i<days;i++) {
        scanf("%d %d",&a,&candles);
        printf("%d %.0f\n",i+1,.5*pow(candles,2) + 1.5*candles);
    } 
    return 0;
}
