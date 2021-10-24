//Problem Link  https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node * next;
    Node * prev;
    Node (int x)
    {
        data=x;
        next=NULL;
        prev=NULL;
    }

};

Node *newNode(int data)
{
    Node *temp=new Node(data);

    return temp;
}

void displayList(Node *head)
{
    //Head to Tail
    while(head->next)
    {
        cout<<head->data<<" ";
        head=head->next;
    }
    cout<<head->data;

}

int getLength(Node * head)
{
    Node *temp=head;

    int count=0;
    while(temp->next!=head)
    {
        count++;
        temp=temp->next;
    }
    return count+1;
}

bool verify(Node* head)
{
    int fl=0;
    int bl=0;

    Node *temp=head;

    while(temp->next)
    {
        temp=temp->next;
        fl++;
    }

    while(temp->prev)
    {
        temp=temp->prev;
        bl++;
    }

    return fl==bl;
}

Node* reverseDLL(Node * head)
{
    if(head==NULL || head->next==NULL){
        return head;
    }
    Node *curr=head, *p=NULL;
    while(curr!=NULL){
        p=curr->prev;
        curr->prev=curr->next;
        curr->next=p;
        curr=curr->prev;
    }
    return p->prev;

}

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    Node *head=NULL, *tail=NULL;
        int x;
	    cin>>x;
	    head = newNode(x);
	    tail = head;

	    for(int i=0;i<n - 1;i++)
	    {
	        cin>>x;
	        Node* temp=newNode(x);
	        tail->next=temp;
	        temp->prev= tail;
	        tail = temp;
	    }
	    head=reverseDLL(head);


	    if(verify(head))
	        displayList(head);
	    else
	        cout<<"Your pointers are not correctly connected";

	    cout<<endl;
	}
	return 0;
}
