#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main()
{ 
int i,j,r,noframes,x,x1=10,x2;
for(i=0;i<200;i++)
r=10000;
noframes=r/200;
i=1;
j=1;
noframes = noframes / 8;
printf("\n number of frames is %d",noframes);
getch();
while(noframes>0)
{
printf("\nsending frame %d",i);
srand(x1++);
x = r%10;
if(x%2 == 0)
{
	for (x2=1; x2<2; x2++)
	{
	printf("\twaiting for %d seconds\n", x2);
	//sleep(1000);
	}
printf("\nsending frame %d",i);
srand(x1++);
x = r%10;
}
printf("\nack for frame %d",j);
noframes-=1;
i++;
j++;
}
printf("\n end of stop and wait protocol");
}

