#include<bits/stdc++.h>
using namespace std;
void reverse(string s){
	for(int i=s.length()-1;i>=0;i--)
	cout<<s[i];
}
void printReverse(string s){
	string delim=" ";
	int pos=0;
	string token;
	int f=0;
	while(pos==s.find(delim)!=string ::npos)
	{
		token=s.substr(0,pos);
		if(f==0){
			cout<<token;
			f=1;
		}
		else{
			reverse(token);
			cout<<" ";
		}
		s.erase(0,pos+delim.length());
	}
	cout<<s;
}
main(){
	string str;
	getline(cin,str);
	printReverse(str);
}
