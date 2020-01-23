#include <stdio.h>

int main() {
    int d, m, y;
    y = 2009;
    
    //scans in day and month, then calculates the day number using maths
    scanf("%d %d",&d,&m);
    int day  = (d += m < 3 ? y-- : y - 2, 23*m/9 + d + 4 + y/4- y/100 + y/400)%7; 
    
    //prints out the name of the day based on the day calculated
    switch(day) {
        case 0:
            printf("Sunday");
            break;
        case 1:
            printf("Monday");
            break;
        case 2:
            printf("Tuesday");
            break;
        case 3:
            printf("Wednesday");
            break;
        case 4:
            printf("Thursday");
            break;
        case 5:
            printf("Friday");
            break;
        case 6:
            printf("Saturday");
            break;
    }

    return 0;
}
