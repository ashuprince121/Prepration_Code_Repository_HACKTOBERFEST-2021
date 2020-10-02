#include<stdio.h>
#include<malloc.h>

int linear_search(int* p, int a, int n, int i)
{
  //recursion breakers
  if(p[i] == a)
    return i;
  else if(i == n)
    return -1;
  else
    linear_search(p,a,n,++i);
}

//main function
int main()
{
  int n, *p, i, a, flag = 0;
  printf("Enter the no. of Elements : ");
  scanf("%d", &n);
  p = (int*)malloc(n*sizeof(int));
  printf("Enter the Elements : ");
  for(i=0;i<n;i++)
    scanf("%d", p+i);
  printf("Enter the Element to be searched : ");
  scanf("%d", &a);
  int pos = linear_search(p,a,n,0);

  if(!(pos+1))
    printf("Element not Found in the array !!!");
  else
    printf("Element found at position %d.", pos + 1);
  free(p);
}
