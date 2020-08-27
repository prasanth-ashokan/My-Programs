#include <bits/stdc++.h>
using namespace std;

struct ListNode {
	int val;
	struct ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};
void reverse(struct ListNode* head){
	struct ListNode *current=head;
	struct ListNode *nex=NULL;
	struct ListNode*  prev=NULL;
	while(current!=NULL){
		nex=current->next;
		current->next=prev;
		prev=current;
		current=nex;
	}
	head=prev;
}
int main()
{
	ListNode* head = new ListNode(0);
	ListNode* temp = head;
	for (int i = 0; i < 5; i++) {
		int e;
		cin >> e;
		ListNode* n = new ListNode(e);
		n->next=head;
		head=n;
	}
	
	for (auto p = head; p->next; p=p -> next) 
		cout << p -> val << endl;
	cout<<endl;
	for (auto p = head; p->next; p=p -> next) {
			ListNode* n = new ListNode(p->val);
		n->next=head;
		head=n;
	}
		cout<<endl;
		for (auto p = head; p->next; p=p -> next) 
		cout << p -> val << endl;
	return 0;
}
