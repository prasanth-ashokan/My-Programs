#include<stdio.h>

main(){
	int n;
	scanf("%d",&n);
	int a[n];
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	int i,j,k;
	for(i=0;i<n;i++){
		for(j=i+1;j<n;){
			if(a[i]==a[j]){
				for(k=j;k<n;k++){
					a[k]=a[k+1];
					
				}
				n=n-1;
			}
			else{
				j++;
			}
		}
	}
	for(i=0;i<n;i++){
		printf("%d ",a[i]);
	}
}
