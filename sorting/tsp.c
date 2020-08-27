#include<stdio.h>
int tsp(int g[],int v[],int cp,int n,int count,cost){
	int k=0;
	if(count==n && g[cp][0]){
		a[k]=cost+g[cp][0]
	}
	for(i=0;i<n;i++){
		if(v[i]==-1 and g[cp][i]!=0){
			v[i]=1
			tsp(g,v,i,n,count+1,cost+g[cp][i])
			v[i]=-1
		}
	}
}
main(){
	int i,j;
	int g[4][4]={{0, 10, 15, 20},{10, 0, 35, 25},{15, 35, 0, 30 },{20, 25, 30, 0}};
	int n=sizeof(g)/sizeof(g[0]);
	int v[n];
	for(i=0;i<n;i++){
		v[i]=-1;
	}
	v[0]=1
	int a[n];
	tsp(g,v,0,n,1,0,a)
}
