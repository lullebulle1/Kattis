#include <stdio.h>

//returns the unique element in the array
int getUnique(int arr[]) {
    if(arr[0]==arr[1])
        return arr[2];
    else if(arr[0]==arr[2]) 
       return arr[1];

    return arr[0];
}
int main() {
    int xs[3];
    int ys[3];
    
    //takes in the data
    for (int i=0; i<3;i++) {
        scanf("%d %d",&xs[i],&ys[i]);
    }
    //prints the answer
    printf("%d %d",getUnique(xs),getUnique(ys));
    return 0;
}
