#include <stdio.h>

int numbHands,total,i;
char suit,a,b;
int main() {

    scanf("%d %c",&numbHands,&suit);
    for (i=0; i<4*numbHands;i++) {
        scanf(" %c%c",&a,&b);
        if (a == 'A')
            total+=11;
        else if (a== 'K')
            total+=4;
        else if (a== 'Q')
            total+=3;
        else if (a== 'J') {
            total+=2;
            if(b==suit)
               total+=18;
        }
        else if (a=='T')
            total+=10;
        else if (a=='9'&& b==suit)
            total+=14;
    }    
    printf("%d",total);
    return 0;
}
