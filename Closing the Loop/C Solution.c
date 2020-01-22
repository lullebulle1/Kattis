#include <stdio.h>

//sorts the arr that is passed in
void sortArr (int arr[], int len) {
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            if (arr[i] > arr[j]) {
                int a =  arr[i];
                arr[i] = arr[j];
                arr[j] = a;
            }
        }
    }
}


int main() {
    int iterations, strings;
    int stringLen;
    char type;

    scanf("%d",&iterations);
    
    //for each problem set
    for (int i=0; i<iterations;i++) {
        scanf("%d",&strings);
        int bs[strings];
        int rs[strings];

        int placeB = 0;
        int placeR = 0;
       
        //for each data point in the line 
        for(int j=0; j<strings; j++) {
            scanf("%d%c",&stringLen,&type);

            printf("*%d %d*\n",placeB,placeR);
            printf("%c",type);

            //breaks it into B's and R's and puts them into a separate 
            if(type=='B') {
                printf("Here with %d",placeB);
                bs[placeB]=stringLen;
                placeB++;        
            }
            else {
                rs[placeR]=stringLen;
                placeR++;        
            }
        }

        //sorts the arrays
        sortArr(bs,placeB);
        sortArr(rs,placeR);

        int totalLen=0;
        for (int k=0;k<placeB>placeR?placeR:placeB;k++) {
            totalLen+=bs[k]+rs[k]-2;
        }
        printf("Case #%d: %d\n",i+1,totalLen);
    }    
    return 0;
}
