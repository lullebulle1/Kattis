#include <stdio.h>
#include <math.h>

int main()
{
    int ang;
    int wall;
    
    scanf("%i %i",&wall,&ang);
    
    printf("%i",(int)ceil((wall/sin(ang*3.1415926535897932384626433/180.0))));
    
    return 0;
}