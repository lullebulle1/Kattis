#include <stdio.h>
#include <string.h>

int main() {
    //This doesn't actually work
    char arr[12];
    int found;
    
    for (int i=1; i<6; i++) {
        fgets(arr,12,stdin);
        
        if(strstr(arr,"FBI")!=NULL) {
            printf("%i ",i);
            found++;
        }
    }

    if(found==0) printf("HE GOT AWAY!");
    return 0;
}