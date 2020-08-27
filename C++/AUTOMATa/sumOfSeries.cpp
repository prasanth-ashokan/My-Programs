#include<stdio.h>
main()
{
	int n;
	float sum=0;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		float val;
		val=1.0/i;
		if(i%2!=0)
		sum+=val;
		else
		sum-=val;
	}
	printf("%f",sum);
}
