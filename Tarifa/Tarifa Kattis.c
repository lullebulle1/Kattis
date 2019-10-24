#include <stdio.h>

int main()
{
    int mega,i,p,total;
    scanf("%i",&mega);
    
    for (scanf("%i",&i); i>0;i--) {
        scanf("%i",&p);
        total+=(mega-p);
    }
    printf("%i\n",total+mega);
    
    return 0;
}