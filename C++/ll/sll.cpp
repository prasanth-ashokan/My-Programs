#include <bits/stdc++.h> 
using namespace std; 
struct ListNode {
     int val;
      ListNode *next;
  };
/*class Solution {
public:
    ListNode* middleNode(ListNode* head) {
    	return head;
      /*  ListNode* g;
        ListNode* h;
        g->val=3;
        g->next=h;
        h->val=5;
        return g;
    }
};
*/
void printList(ListNode* n) 
{ 
    while (n != NULL) { 
        cout << n->val << " "; 
        n = n->next; 
    } 
} 
int main(){
	ListNode* head=NULL;
	head = new ListNode(); 
	head->val=5;
	head->next=NULL;
	printList(head);
	return 0;
}
