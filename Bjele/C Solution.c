#include <stdio.h>

int main() {
    int correct[] = {1,1,2,2,2,8};
    int solution = 0;
    
    //Takes in the number and compares it with the correct number, then prints
    for(int i=0; i<6;i++) {
        scanf("%d",&solution);
        printf("%d ",correct[i]-solution);
    }

    return 0;
}
