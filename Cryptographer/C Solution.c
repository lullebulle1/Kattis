#include <stdio.h>

int main() {
    int i = 0;
    int days = 0;

    char secretMsg[301];
    char letters[] = {'P','E','R'};

    scanf("%s",secretMsg);

    //counts the days which the letter in the message
    //does not match the sequence PER
    while(secretMsg[i]!='\0') {
        if(secretMsg[i]!=letters[i%3])
            days++;
        i++;
    } 

    //prints result
    printf("%d",days);
    return 0;
}
