#include <stdio.h>

int main() {
    char arr[100];
    int i;
    scanf("%s",arr);
    printf("%c",arr[0]);
    
    while(arr[i]!=NULL) {
        if(arr[i]=='-') printf("%c",arr[i+1]);
        i++;
    }
    
    return 0;
}