#include<stdio.h>
#include<stdlib.h>
void swap(int a[],int u,int v){
	int temp=a[u];
	a[u]=a[v];
	a[v]=temp;
}
int partition(int a[],int low,int high){
	int pivot=a[high];
	int i,j;
	i=low-1;
		for(j=low;j<=high-1;j++){
			if(a[j]<pivot){
				i++;
				swap(a,j,i);
			}
		}
		swap(a,i+1,high);
		return (i+1);
}
void quicksort(int a[],int low,int high){
	if(low<high){
		int pi=partition(a,low,high);
		quicksort(a,low,pi-1);
		quicksort(a,pi+1,high);
	}
}
void printarray(int a[],int n){
	int i;
	for(i=0;i<n;i++){
		printf("%d\t",a[i]);
	}
}
int main(){
	int a[]={5,1,3,7,2};
	int n=sizeof(a)/sizeof(a[0]);
	quicksort(a,0,n-1);
	printf("SORTED ARRAY:");
	printarray(a,n);
}
