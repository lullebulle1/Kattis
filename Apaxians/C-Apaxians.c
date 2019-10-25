#include <stdio.h>

int main()
{
    char arr[250], output[250];
    int place = 0;
    scanf("%s",arr);

    output[0] = arr[0];
    for (int i = 1; i < sizeof(arr);i++) {
        if(arr[i]==NULL) break;
        
        if(arr[i] != output[place])
            output[++place]=arr[i];
    }
    printf(output);
    return 0;
}