#include<stdio.h>
#define SIZE 5
int stack[SIZE],top=-1;

int isEmpty(){
	if(top==-1){
		return 1;
	}
	else{
		return 0;
	}
}
int isFull(){
	if(top==SIZE-1){
		return 1;
	}
	else{
		return 0;
	}
}
void display(){
	int i;
	for(i=0;i<=top;i++){
		printf("%d\t",stack[i]);
	}
}
void push(int ele){
	if(isFull()){
		printf("Stack is overflow");
	}
	else{
		top++;
		stack[top]=ele;
	}
}
void pop(){
	if(isEmpty()){
		printf("stack is underflow");
	}
	else{
		top--;
	}
}
main(){
	while(1){
		int ch;
		printf("1.push\n");
		printf("2.pop\n");
		printf("3.dispaly\n");
		printf("4.exit\n");
		scanf("enter the choice:%d",&ch);
		printf("%d",ch);
		if (ch==1){
			int ele;
			scanf("Enter the element to push : %d",&ele);
			push(ele);
			break;
		}
		else if(ch==2){
			pop();
			break;
		}
		else if(ch==3){
			display();
			break;	
		}
		else if (ch==4){
			break;
		}
		else{
			printf("enter the valid choice");
			break;
		}
	}
}
