#include<stdio.h>
#define N 5
int queue[N];
int front=-1;
int rear=-1;
void enqueue(int ele){
	if (rear==N-1){
		printf("\n");
		printf("Queue is Full");
	}
	else if(rear==-1 && front==-1){
		rear=front=0;
		queue[rear]=ele;
	}
	else{
		rear++;
		queue[rear]=ele;
	}
}
void dequeue(){
	if (front==-1 && rear==-1){
		printf("\n");
		printf("Queue is empty");
	}
	else if (front==rear){
		front=rear=-1;
	}
	else{
		front++;
	}
}
void peek(){
	if(front==-1 && rear==-1){
		printf("\n");
			printf("Queue is empty");
	}
	else{
		printf("\n");
		printf("peek is %d",queue[front]);
	}
}

void display(){
	int i;
	if(front==-1 &&rear==-1){
		printf("\n");
		printf("queue is empty");
	}
	else{
		printf("\n");
	for(i=front;i<=rear;i++){
		printf("%d\t",queue[i]);
	}
}
}
int main(){
	while(1){
		int ch;
		printf("\n");
		printf("\n1.enqueue\n");
		printf("2.dequeue\n");
		printf("3.dispaly\n");
		printf("4.peek\n");
		printf("5.exit\n");
		printf("enter the choice:");
		scanf("%d",&ch);
		if (ch==1){
			int ele;
			printf("\nEnter the element to enqueue : ");
			scanf("%d",&ele);
			enqueue(ele);
		}
		else if(ch==2){
			dequeue();
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
	return 0;
}
