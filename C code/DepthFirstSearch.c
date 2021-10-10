#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 8

struct Simpul {
   char label;
   bool visited;
};

//stack variables

int stack[MAX]; 
int top = -1; 

//graph variables

//array of vertices
struct Simpul* lstVertices[MAX];

//adjacency matrix
int adjMatrix[MAX][MAX];

//Simpul count
int SimpulCount = 0;

//stack functions

void push(int item) { 
   stack[++top] = item; 
} 

int pop() { 
   return stack[top--]; 
} 

int peek() {
   return stack[top];
}

bool isStackEmpty() {
   return top == -1;
}

//graph functions

//tambah Simpul to the Simpul list
void tambahSimpul(char label) {
   struct Simpul* Simpul = (struct Simpul*) malloc(sizeof(struct Simpul));
   Simpul->label = label;  
   Simpul->visited = false;     
   lstVertices[SimpulCount++] = Simpul;
}

//tambah Busur to Busur array
void tambahBusur(int start,int end) {
   adjMatrix[start][end] = 1;
   adjMatrix[end][start] = 1;
}

//display the Simpul
void displaySimpul(int SimpulIndex) {
   printf("%c ",lstVertices[SimpulIndex]->label);
}       

//get the adjacent unvisited Simpul
int getAdjUnvisitedSimpul(int SimpulIndex) {
   int i;

   for(i = 0; i < SimpulCount; i++) {
      if(adjMatrix[SimpulIndex][i] == 1 && lstVertices[i]->visited == false) {
         return i;
      }
   }

   return -1;
}

void depthFirstSearch() {
   int i;

   //mark first node as visited
   lstVertices[0]->visited = true;

   //display the Simpul
   displaySimpul(0);   

   //push Simpul index in stack
   push(0);

   while(!isStackEmpty()) {
      //get the unvisited Simpul of Simpul which is at top of the stack
      int unvisitedSimpul = getAdjUnvisitedSimpul(peek());

      //no adjacent Simpul found
      if(unvisitedSimpul == -1) {
         pop();
      } else {
         lstVertices[unvisitedSimpul]->visited = true;
         displaySimpul(unvisitedSimpul);
         push(unvisitedSimpul);
      }
   }

   //stack is empty, search is complete, reset the visited flag        
   for(i = 0;i < SimpulCount;i++) {
      lstVertices[i]->visited = false;
   }        
}

int main() {
   int i, j;

   for(i = 0; i < MAX; i++){    // set adjacency 
      for(j = 0; j < MAX; j++) // matrix to 0
         adjMatrix[i][j] = 0;
   }

   tambahSimpul('A');   // 0
   tambahSimpul('B');   // 1
   tambahSimpul('C');   // 2
   tambahSimpul('D');   // 3
   tambahSimpul('E');	// 4
   tambahSimpul('F');   // 5
   tambahSimpul('G');   // 6
   tambahSimpul('H');   // 7
 
   tambahBusur(0, 1);    // A - B
   tambahBusur(0, 2);    // A - C
   tambahBusur(1, 3);    // B - D
   tambahBusur(1, 4);    // B - E
   tambahBusur(2, 5);    // C - F
   tambahBusur(2, 6);    // C - G
   tambahBusur(3, 7);    // D - H
   tambahBusur(4, 7);    // E - H
   tambahBusur(5, 7);    // F - H
   tambahBusur(6, 7);    // G - H
   printf("\nDepth First Search: \n\n");
   depthFirstSearch(); 

   return 0;   
}
