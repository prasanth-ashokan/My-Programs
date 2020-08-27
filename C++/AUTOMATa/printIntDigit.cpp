#include<stdio.h>
main(){
	int n,rem,res;
	scanf("%d",&n);;
	while(n!=0){
		rem=n%10;
		res=res*10+rem;
		n=n/10;
	}
	n=res;
	while(n!=0){
		rem=n%10;
		printf("%d   ",rem);
		n=n/10;
	}
}
