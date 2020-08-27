#include<stdio.h>
main(){
	int n,i,j,k,p,q;
	scanf("%d",&n);
	for(i=1;i<=n;i++){
			for(k=1;k<=i;k++){
				printf("* ");
			}
			for(p=1;p<(n*2)+n-(i*2);p++){
				printf("  ");
			}
			for(k=1;k<=i;k++){
				printf(" *");
			}
			printf("\n");	
	
}
int g=0;
for(i=5;i>=1;i--){
			for(k=i;k>=1;k--){
				printf("* ");
			}
			for(p=1;p<(i*2)+i;p++){
				printf(" ");
			}
			for(k=i;k>=1;k--){
				printf(" *");
			}
			printf("\n");	
	
}
}
