#include<bits/stdc++.h>
using namespace std;
struct ListNode {
   int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };
void push(ListNode** head_ref, int new_data)  
{  
    /* 1. allocate node */
    ListNode* new_node = new ListNode(0); 
  
    /* 2. put in the data */
    new_node->val = new_data;  
  
    /* 3. Make next of new node as head */
    new_node->next = (*head_ref);  
  
    /* 4. move the head to point to the new node */
    (*head_ref) = new_node;  
} 

int main(){
	char r[100];
	ListNode* l3=NULL;
	char s="9";
	char e="1999999999";
	int n,m;
	n=stoi(s);
	m=stoi(e);
	cout<<n<<" "<<m;
	int  t = n + m ;
        
        r=to_char( t );
        vector<int> g;
        for(int  i = 0; i< r.length(); i++ ){
            string s4; s4=(char) r[i];
            g.push_back(stoi(s4));
        }
          for (auto i = g.begin(); i != g.end(); ++i) 
          {
              push(&l3,*i);
          }
    while(l3){
    	cout<<l3->val<<endl;
    	l3=l3->next;
    	
	}
          
	
}
