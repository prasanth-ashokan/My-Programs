#include<stdio.h>
#include<stdlib.h>
int i,j;
void merge(int a[],int l,int m,int r){
	int i,j,k;
	int n1=m-l+1;
	int n2=r-m;
	int l1[n1],r1[n2];
	for(i=0;i<n1;i++){
		l1[i]=a[l+i];
	}
	for(j=0;j<n2;j++){
		r1[j]=a[m+1+j];
	}
	i=0;
	j=0;
	k=l;
	while(i<n1 && j<n2){
		if(l1[i]<=r1[j]){
			a[k]=l1[i];
			i++;
		}
		else{
			a[k]=r1[j];
			j++;
			
		}
		k++;
	}
	while(i<n1){
		a[k]=l1[i];
		i++;
		k++;	
	}
		while(j<n2){
		a[k]=r1[j];
		j++;
		k++;
	}
	}
	

void mergesort(int a[],int l,int r){
	if(l<r){
		int m=l+(r-l)/2;
		mergesort(a,l,m);
		mergesort(a,m+1,r);
		merge(a,l,m,r);
	}
}
void printarray(int a[],int n){
	for(i=0;i<n;i++){
		printf("%d\t",a[i]);
	}
}
int main(){
	int a[]={5,1,3,7,2};
	int n=sizeof(a)/sizeof(a[0]);
	mergesort(a,0,n-1);
	printf("SORTED ARRAY:");
	printarray(a,n);
}
