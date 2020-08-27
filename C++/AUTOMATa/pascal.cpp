#include<stdio.h>
int main(){
	int i,j,rows,k,c;
	scanf("%d",&rows);
	for(i=0;i<rows;i++){
		for(k=1;k<rows-i;k++){
			printf(" ");
		}
		for(j=0;j<=i;j++){
			if(i==0 || j==0){
				c=1;
			}
			else{
				c=c*(i-j+1)/j;
				
			}
			printf("%d ",c);
		}
		printf("\n");
	}
}
