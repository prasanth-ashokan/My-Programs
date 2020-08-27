#include<stdio.h>
int binarysearch(int a[],int low,int high,int x){
	while(high>=low){
		int mid=low+(high-low)/2;
		if (a[mid]==x){
			return mid;
		}
		else if(a[mid]>x){
			return binarysearch(a,low,mid,x);
		}
		return binarysearch(a,mid+1,high,x);
	}
	return -1;
}
int main(){
	int a[]={5,1,3,7,2};
	int n=sizeof(a)/sizeof(a[0]);
	int x=31;
	int f=binarysearch(a,0,n,x);
	if (f==-1){
		printf("NOT FOUND");
	}
	else{
		printf("FOUND AT %d",f);
	}
}
