#include <stdio.h>

int numbAtBats, totalPts, totalPlays;
int main() {
    scanf("%d",&numbAtBats);
    
    for (int i=0;i<numbAtBats;i++) {
        int play;
        scanf("%d",&play);
        if(play != -1) {
            totalPlays++;
            totalPts+=play;
        }
    }
    printf("%f",(float)totalPts/(float)totalPlays);
    return 0;
}
