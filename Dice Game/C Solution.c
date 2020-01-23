#include <stdio.h>

int main() {
    int gunn = 0, emma = 0;

    //takes in gunnars four dice values
    for (int i=0; i<4; i++) {
        int temp;
        scanf("%d",&temp);
        gunn+=temp;
    } 

    //takes in emmas four dice values
    for (int i=0; i<4; i++) {
        int temp;
        scanf("%d",&temp);
        emma+=temp;
    }

    //prints who has the higher number
    printf("%s",gunn>emma?"Gunnar":gunn==emma?"Tie":"Emma"); 
    return 0;
}
