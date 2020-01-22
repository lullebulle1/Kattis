#include <stdio.h>

//sorts the arr that is passed in
void sortArr (int arr[], int len) {
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            if (arr[i] < arr[j]) {
                int a =  arr[i];
                arr[i] = arr[j];
                arr[j] = a;
            }
        }
    }
}

int main() {
    int iterations, strings, stringLen;
    char type;

    //takes in the number of cases to do
    scanf("%d",&iterations);
    
    //for each problem set
    for (int i=0; i<iterations;i++) {

        //takes in the amount of data points in this case
        scanf("%d",&strings);
        
        //sets the two arrays and positions in array
        int bs[strings];
        int rs[strings];
        int placeB=0;
        int placeR=0; 

        //for each data point in the line 
        for(int j=0; j<strings; j++) {
            
            //takes in the data point in the line
            scanf("%d%c",&stringLen,&type);

            //breaks it into B's and R's and puts them into a separate array
            if(type=='B') {
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

        //calculates the string lengths
        int totalLen=0;
        int smaller = placeB>placeR?placeR:placeB;
        for (int k=0;k<smaller;k++) 
            totalLen+=bs[k]+rs[k]-2;
        
        //prints answer
        printf("Case #%d: %d\n",i+1,totalLen);
    }    
    return 0;
}
