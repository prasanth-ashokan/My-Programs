#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node* next;
};
struct node* root=NULL;
int length(){
	if(root==NULL){
		return 0;
	}
	else{
		int c=0;
		struct node* p;
		p=root;
		while(p!=NULL){
		c=c+1;	
		p=p->next;
		}
		return c;
	}
}

void shift(){
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else if(root->next==NULL){
		root=NULL;
		free(root);
		printf("only one node in list");
	}
	else{
		struct node *p;
		p=root;
		root=root->next;
		free(p);
		printf("\n deleted");
	}
}


void search(){
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else{
		printf("Enter the element to search:\t");
		int ele;
		int f=0;
		scanf("%d",&ele);
		struct node* s;
		s=root;
		printf("\n");
		while(s!=NULL){
			if(s->data==ele){
				printf("element found");
				f=1;
				break;
			}
			s=s->next;
		}
		if (f==0){
			printf("element not found");
		}
	}
}
void append(){
	struct node* temp;
	temp=(struct node*)malloc(sizeof(struct node));
	printf("\nEnter the element:");
	scanf("%d",&temp->data);
	temp->next=NULL; 
	if(root==NULL){
		root=temp;
	}
	else{
		struct node* p;
		p=root;
		while(p->next!=NULL){
			p=p->next;
		}
		p->next=temp;
	}
}
void display()
{
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else{
		struct node* d;
		d=root;
		printf("\n");
		while(d!=NULL){
			printf("%d\t",d->data);
			d=d->next;
		}
	}
	
}

void unshift(){
	struct node* temp;
	temp=(struct node*)malloc(sizeof(struct node));
	printf("enter the element to push:\t");
	scanf("%d",&temp->data);
	if(root==NULL){
	root=temp;
	}
	else{
		temp->next=root;
		root=temp;
	}	
}
void pop(){
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else if(root->next==NULL){
		root=NULL;
		free(root);
		printf("only one node in list");
	}
	else{
		struct node *r,*p;
            p=root;   
            while(p->next != NULL)  
                {  
                    r = p;  
                    p = p->next;  
                }  
                r->next = NULL;  
                free(p);  
                printf("deleted");  
            }     
		
}

void delete_pos(){
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else{
		printf("enter the position:\t");
		int pos;
		scanf("%d",&pos);
		int l;
		l=length();
		if (pos>l+1){
			printf("position invalid");
			printf("size of list is %d",l);
		}
		else{
			if(pos==1){
				shift();
			}
			else if(pos==l+1){
				pop();
			}
	}
}
}

void sort(){

	if(root==NULL){
		printf("\nEMPTY");	
	}
	else{
	}
}

void swap(){
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else{
	}
}
void insert_pos(){
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else{
		printf("enter the position:\t");
		int pos;
		scanf("%d",&pos);
		int l;
		l=length();
		if (pos>l+1){
			printf("position invalid");
			printf("size of list is %d",l);
		}
		else{
			if(pos==1){
				unshift();
			}
			else if(pos==l+1){
				append();
			}
		}
		
		
	}
}

void insert_after_x(){
	if(root==NULL){
		printf("\nEMPTY");	
	}
	else{
		printf("enter the element:\t");
		int ele;
		scanf("%d",&ele);
	}
}

main(){
while(1){
	printf("\n");
	printf("\n1.insert at end");
	printf("\n2.insert at begin");
	printf("\n3.insert at k poistion");
	printf("\n4.search");
	printf("\n5.delete at end");
	printf("\n6.delete at begin");
	printf("\n7.delete at k poistion");
	printf("\n8.Display");
	printf("\n9.swap");
	printf("\n10.insert after x element");
	printf("\n11.Length");
	printf("\n12.exit\n");
	int c;
	scanf("\n%d",&c);
	if(c==1){
append();
	}
	if(c==2){
		unshift();
	}
		if(c==3){
			insert_pos();
	}
	
	if(c==4){
		search();
	}
		if(c==5){
			pop();
	}
	
		if(c==6){
			shift();
	}
	
		if(c==7){
			delete_pos();
			
	}
	
	if(c==8){
		display();
	}
		if(c==9){
			swap();
	}
	
		if(c==10){
		insert_after_x();
	}
	if(c==11){
		printf("\n%d",length());
	}
	if(c==12){
		break;
	}
}	
}

