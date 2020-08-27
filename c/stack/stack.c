#include<stdio.h>
#include<conio.h>

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
	if(top==-1){
		printf("\nstack is empty\n");
	}
	else{
	int i;
	for(i=0;i<=top;i++){
		printf("%d\t",stack[i]);
	}
}
}
void push(int ele){
	if(isFull()){
		printf("\nStack is overflow\n");
	}
	else{
		top++;
		stack[top]=ele;
	}
}
void pop(){
	if(isEmpty()){
		printf("\nstack is underflow\n");
	}
	else{
		top--;
	}
}
void peek(){
	if(top==-1){
		printf("\nstack is empty\n");
	}
	else{
	printf("\npeek is %d\n",stack[top]);
}
}
main(){
	while(1){
		int ch;
		printf("\n1.push\n");
		printf("2.pop\n");
		printf("3.dispaly\n");
		printf("4.peek\n");
		printf("5.exit\n");
		printf("enter the choice:");
		scanf("%d",&ch);
		if (ch==1){
			int ele;
			printf("\nEnter the element to push : ");
			scanf("%d",&ele);
			push(ele);
		}
		else if(ch==2){
			pop();
		}
		else if(ch==3){
			display();
		}
		else if(ch==4){
			peek();
		}
		else if (ch==5){
			break;
		}
		else{
			printf("enter the valid choice");
			break;
		}
	}
}
