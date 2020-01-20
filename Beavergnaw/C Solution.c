#include <stdio.h>
#include <math.h>
#define M_PI 3.14159265358979323846 

double height, volume;
int main() {
    //This is the equation to use: (D^3 - 6V/π)^(1/3)
    scanf("%lf %lf",&height,&volume);
    while(height!=0) {
        printf("%.9lf\n",pow(pow(height,3)-6*volume/M_PI,(1.0/3)));
        scanf("%lf %lf",&height,&volume);
    }
    return 0;
}
