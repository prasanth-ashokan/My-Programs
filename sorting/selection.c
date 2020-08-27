#include<stdio.h>
int i,j;
void swap(int a[],int u,int v){
	int temp=a[u];
	a[u]=a[v];
	a[v]=temp;
}
void selection(int a[],int n){
	for(i=0;i<n-1;i++){
		int min_index=i;
		for(j=i+1;j<n;j++){
			if(a[j]<a[min_index]){ //ascending,decending(a[j]>a[min_index]
				swap(a,j,min_index);
			}
		}
	}
}
void printarray(int a[],int n){
	for(i=0;i<n;i++){
		printf("%d\t",a[i]);
	}
}
int main(){
	int a[]={5,1,8,3,7};
	int n=sizeof(a)/sizeof(a[0]);
	selection(a,n);
	printf("SORTED ARRAY:");
	printarray(a,n);
}
