#include<stdio.h>
void swap(int *a,int *b){
	int tmp;
	tmp=*a;
	*a=*b;
	*b=tmp;
	printf("\n%d\n%d",*a,*b);
}
main(){
	int m,n;
	scanf("%d%d",&n,&m);
	swap(&n,&m);
}

