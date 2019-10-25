#include <stdio.h>

int main()
{
    char arr[250], last;
    scanf("%s",arr);
    last=arr[0];
    printf("%c",arr[0]);
    
    for (int i = 1; i < sizeof(arr);i++) {
        if(arr[i]==NULL) break;
        
        if(arr[i] != last) {
            printf("%c",arr[i]);
            last=arr[i];
        }
    }
    return 0;
}