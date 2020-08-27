#include <bits/stdc++.h>
using namespace std;

int main()
{
	/*
	vector<int> v;
	//push_back();
	//emplace_back();
	v.push_back(2);
	v.push_back(1);
	v.push_back(9);
	for (int i = 0; i < (int)v.size(); i++) {
		cout << v[i] << endl;
	}
	*/
	vector<int> v{5,8,1,3,9};
	/*
	for (auto i : v) {
		cout << i << endl;
	} 
	for (int i = 0; i < (int)v.size(); i++) {
		cout << v[i] << endl;
	}
	for (vector<int>::iterator i = v.begin(); i != v.end(); i++) {
		cout << *i << endl;
	}
	for (vector<int>::reverse_iterator i = v.rbegin(); i != v.rend(); i++) {
		cout << *i << endl;
	}*/
	//cout << *v.begin() << endl;
	sort(v.begin(),v.end()); //o(nlogn)
	for (int i = 0; i < (int)v.size(); i++) {
		cout << v[i] << endl;
	}	
	cout << accumulate(v.begin(), v.end(), 20);
	return 0;
}
