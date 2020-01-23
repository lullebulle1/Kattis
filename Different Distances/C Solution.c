#include <stdio.h>
#include <math.h>

int main() {
    double a,b,c,d, p;

    //goes forever until it scans in a 0
    while(1) {
        scanf("%lf",&a);
        if(a==0)
            break;

        //scans in the rest of the variables
        scanf("%lf %lf %lf %lf",&b, &c, &d, &p);

        //does the calculation and prints it
        /*double numb = fabs(pow((c-a),p)) + fabs(pow((d-b),p));*/
        printf("%.10lf\n",pow(fabs(pow((c-a),p)) + fabs(pow((d-b),p)),1/p));
    } 
    return 0;
}
