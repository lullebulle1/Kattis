#include <stdio.h>
#include <string.h>

int found;
int main() {
	char word[12];
	for(int i=0; i<5; i++) {
		scanf("%s",word);
		if(strstr(word,"FBI")!=NULL) {
			printf("%d ",i+1);
			found=1;
		}	
	}

	if(!found) printf("HE GOT AWAY!");
	return 0;
}
