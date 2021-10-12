//HEAP SORT
#include <stdio.h>
#include <stdlib.h>

void Swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void heapify(int arr[], int n, int i) {//eapyfiy the array
    int Max = i; //Initialize Max as root
    int leftChild = (2*i) + 1;
    int rightChild = (2*i) + 2;
    if (leftChild < n && arr[leftChild] > arr[Max])Max = leftChild;//If left child is greater than root
    if (rightChild < n && arr[rightChild] > arr[Max])Max = rightChild;//If right child is greater than max
    if (Max != i) {//If max is not root
      Swap(&arr[i], &arr[Max]);
      heapify(arr, n, Max);//heapify the affected sub-tree recursively
    }
}

void heapSort(int arr[], int n) { //Function to perform heap sort
    for (int i = n/2 - 1;i >= 0; i--)heapify(arr, n, i);//Rearrange array
    for (int i = n-1;i >= 0; i--) {
      Swap(&arr[0], &arr[i]); //Current root moved to the end
      heapify(arr, i, 0); //Calling max heapify on the heap reduced array
    }
}

void printArray(int arr[], int n) {//Prints the array
    for (int i = 0; i < n; ++i)printf("%d ", arr[i]);
    printf("\n");
}

int main(void) {
    int n;
    printf("Write value of n : ");
    scanf("%d",&n);
    int arr[n];
    printf("Write some numbers to be sorted \n");
    for(int i=0;i<n;i++)scanf("%d",&arr[i]);
    printf("Array before sorting: \n");
    printArray(arr, n);
    heapSort(arr, n);
    printf("Sorted array:\n");
    printArray(arr, n);
    return 0;
}
