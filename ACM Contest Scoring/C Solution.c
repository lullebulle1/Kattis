#include <stdio.h>

//initialization
int corr, time, min;
int prevAtt [26];

int main() {
    char status[6];
    char prob;

    //scans in the number of minutes, the prob letter, and whether right/wrong
    scanf("%d %c %s",&min, &prob, &status);
   
    while (min!=-1) {
        //if correct
        if(status[0]=='r') {
            corr++;
            time+=min;

            //checks at the numerical pos of the letter if it has been attempted before
            if(prevAtt[(int)prob%101]!=0)
                time+=20*prevAtt[(int)prob%101];
        }
        //increase the spot of the letter in the array
        prevAtt[(int)prob%101]++;
        scanf("%d %c %s",&min, &prob, &status);
    }
    //prints solution
    printf("%d %d",corr, time);
    return 0;
}
