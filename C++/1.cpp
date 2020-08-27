#include<bits/stdc++.h>
using namespace std;
main(){
	
	//cout<<sum(a,b);
	vector<int> v(5);
	for (int i = 0; i < 5; i++) {
		cin >> v[i];
	}
	sort(v.begin(),v.end());
	for (auto i : v) {
		cout << i << ' ';
	}
	v.erase(unique(v.begin(), v.end()),v.end());
	for (auto i : v) {
		cout << i << ' ';
	}
}
