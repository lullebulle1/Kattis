#include <stdio.h>

//prototypes of the functions below
void initArray(int[], int);
int findMax (int[], int);
void printMaxLoc (int[], int, int);

int main() {
    //initialization
    int a,b,size;
    scanf("%d %d",&a,&b);
    size = a+b+1;

    //create array of size a+b+1
    int poss[size];
    initArray (poss, size);

    //for each possible combination, add one to that select spot
    for(int i=1; i<a+1; i++) {
        for(int j=1; j<b+1; j++) {
            poss[i+j]++;
        }
    }    

    //prints all the spots that have max size 
    printMaxLoc(poss,size,findMax(poss,size));
    return 0;
}

//sets all array elements to 0
void initArray(int arr[], int len) {
    for (int i=0; i<=len; i++) 
        arr[i]=0;
}

//finds the max number in the array
int findMax (int arr[], int len) {
    int max=-1;
    for (int i=1; i<len+1; i++) {
        if(arr[i]>max)
            max=arr[i];
    }
    return max;
}

//prints all locations where the number is max
void printMaxLoc (int arr[], int len, int max) {
    for (int i=1; i<len+1; i++) {
        if(arr[i]==max)
            printf("%d\n",i);
    }
}
