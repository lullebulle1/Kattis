#include <stdio.h>

int returnStrLen(char b[]) {
    int x=0;
    while(b[x]!='h') {
        x++;
    }
    return x;
}
int main() {
    char a[1001];
    char b[1001];
    scanf("%s %s",&a,&b);
    printf("%s",returnStrLen(a)>=returnStrLen(b)?"go":"no");
    return 0;
}
