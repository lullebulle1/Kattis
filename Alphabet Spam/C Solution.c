#include <stdio.h>

int main() {
    float upp, low, white, special, total;
    char arr[100000];
    scanf("%s",arr);
    
    for (int i=0; i<sizeof(arr);i++) {
        if (arr[i]==NULL) break;
        
        if(isupper(arr[i])) upp++;
        else if(islower(arr[i])) low++;
        else if(arr[i]=='_') white++;
        else special++;
        total++;
    }
    printf("%f\n%f\n%f\n%f",white/total,low/total,upp/total,special/total);
    
    
    return 0;
}