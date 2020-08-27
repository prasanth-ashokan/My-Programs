#include <bits/stdc++.h>
using namespace std;

struct node {
	int val;
	struct node* next;
	node(int x) : val(x), next(NULL) {}
};
int main()
{
	node* head = new node(0);
	node* temp = head;
	for (int i = 0; i < 5; i++) {
		int e;
		cin >> e;
		node* n = new node(e);
		temp -> next = n;
		temp = temp -> next;
	}
	head = head -> next;
	for (auto p = head; p; p=p -> next) 
		cout << p -> val << endl;
	return 0;
}
