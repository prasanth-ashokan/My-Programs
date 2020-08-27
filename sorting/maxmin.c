#include<stdio.h>
int min,max;
int a[100];
void minmax(int l,int r){
	int max1,min1,mid;
	if(r==l){
		max=min=a[l];
	}
	else{
	if(l==r-1){
		if(a[l]>a[r]){
			max=a[l];
			min=a[r];
		}
		else{
			max=a[r];
			min=a[l];
		}
	}
	else{
		mid=(l+r)/2;
		minmax(l,mid);
		min1=min;max1=max;
		minmax(mid+1,r);
		if(max1>max){
			max=max1;
		}
		if(min1<min){
			min=min1;
		}
}
	}
}
int main(){
	int a[]={5,1,3,7,2};
	int n=sizeof(a)/sizeof(a[0]);
	min=a[0];
	max=a[0];
	minmax(1,n);
	printf("min: %d\tmax: %d",min,max);
	return 0;
}
	
