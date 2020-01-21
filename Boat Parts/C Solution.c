#include <stdio.h>
#include <string.h>

int parts,days,count,found;
int main() {
    //scans in the number of parts to replace and boating days
    scanf("%d %d",&parts,&days);

    //the list of previous parts and the part on a particular day
    char partList[parts][21];
    char partOnDay[21];

    //goes through every day
    for(int i=0; i<days;i++) {
        found = 0;
        scanf("%s",partOnDay);

        //goes through all previous parts and compares to today's
        for (int j=0; j<count; j++) {
            if(strcmp(partOnDay, partList[j])==0) {
                found = 1;
                break;
            }
        }

        //if there was no match found, add to count
        if(!found) {
            strcpy(partList[count],partOnDay);
            count++;
        }

        //if unique parts is equivalent to what the problem wanted, done
        if(count==parts) {
            printf("%d",i+1);
            return 0;
        }
    }
    //the case where he didn't replace all parts
    printf("paradox avoided");

    return 0;
}
