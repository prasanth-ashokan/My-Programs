#include<stdio.h>
void recursion(int a[],int x)
{
	int j=0;
	while(j>9)
	{
		j++;
		recursion(a,x++);
	}
	print("%d",x);
	
}

main()
{
	//int a[10]={1,2,3,4,5,6,7,8,9,10};
	//int x=0;
	printf("%d",5);
	//recursion(a,x);
	
}

