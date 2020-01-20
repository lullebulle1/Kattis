#include <stdio.h>

int a,b,i;
int main() {
    char record[201];
    scanf("%s",&record);
   
    //loops through until the end of the array 
    while(record[i]!='\0') {
        //if the record is a, add score to a, otherwise b
        if (record[i]=='A') a+=(int)record[i+1];
        else b+=(int)record[i+1];
        i+=2;
    }
    //print result
    printf("%s",a>b?"A":"B");
    return 0;
}
