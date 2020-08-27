#include<stdio.h>
main(){
	int n=5;
	int sp=n-1;
	int st=1,i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<sp;j++)
		{
			printf(" ");
		}
		for(j=1;j<=2*st-1;j++)
		{
			printf("*");
		}
		printf("\n");
		sp-=1;
		st+=1;
	}
}
