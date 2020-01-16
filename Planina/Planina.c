#include <stdio.h>
#include <math.h>

double x;
int main() {
	scanf("%lf", &x);
	printf("%d",(int) (pow(4.0,x)+pow(2.0,x+1)+1));	
	return 0;
}
