#include<stdio.h>
#include<math.h>
long int power(long int x,long int y){
	if (y==1)
	return x;
	else
	return x*power(x,y-1);
}
main(){
	long int b,p;
	scanf("%ld%ld",&b,&p);
	printf("%ld",power(b,p));
}
