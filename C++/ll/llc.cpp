#include<bits/stdc++.h>
using namespace std;

void display();
void insert();
class sovi{
	public:
		int val;
		sovi* next;
};
void insert(sovi* prev_node,int data){
if (prev_node == NULL)  
    {  
        cout<<"the given previous node cannot be NULL";  
        return;  
    }  
  
    /* 2. allocate new node */
    sovi* new_node = new sovi(); 
  
    /* 3. put in the data */
    new_node->val = data;  
  
    /* 4. Make next of new node as next of prev_node */
    new_node->next = prev_node->next;  
  
    /* 5. move the next of prev_node as new_node */
    prev_node->next = new_node;  
}  
void append(sovi** head_ref, int new_data)  
{  
    sovi* new_node = new sovi(); 
  
    sovi *last = *head_ref; /* used in step 5*/
  
    /* 2. put in the data */
    new_node->val = new_data;  
  
    /* 3. This new node is going to be  
    the last node, so make next of  
    it as NULL*/
    new_node->next = NULL;  
  
    /* 4. If the Linked List is empty, 
    then make the new node as head */
    if (*head_ref == NULL)  
    {  
        *head_ref = new_node;  
        return;  
    }  
  
    /* 5. Else traverse till the last node */
    while (last->next != NULL)  
        last = last->next;  
  
    /* 6. Change the next of last node */
    last->next = new_node;  
    return;  
}  
void display(sovi* s){
	while(s!=NULL){
	cout<<s->val<<endl;
	s=s->next;
}
}
main(){
	int i,n;
	sovi* s=new sovi();
	for(i=0;i<5;i++){
		cout<<"enter:";
	cin>>n;
	append(&s, n);
}
	display(s);
}
