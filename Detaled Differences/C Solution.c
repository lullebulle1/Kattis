#include <stdio.h>

//prints the array from 0 to whatever length
void printArr(char arr[], int len) {
    for(int i=0;i<len;i++) {
        printf("%c",arr[i]);
    }
    printf("\n");
}

int main() {
    //initalization
    int iterations;
    char arr1[51];
    char arr2[51];
    char diffs[51]={'\0'};

    //scans in the number of cases
    scanf("%d",&iterations);

    //for each case:
    for (int i=0; i<iterations;i++) {
        //scans in the two given arrays
        scanf("%s",arr1);
        scanf("%s",arr2);
        
        //compares each point in the arrays and decides if equal or not
        int j=0;
        while (arr1[j]!='\0') {
            if(arr1[j]!=arr2[j])
                diffs[j]='*';
            else
                diffs[j]='.';
            j++;
        }
        
        //prints all the arrays
        printArr(arr1,j);
        printArr(arr2,j);
        printArr(diffs,j);
        printf("\n");
    }    
    return 0;
}
