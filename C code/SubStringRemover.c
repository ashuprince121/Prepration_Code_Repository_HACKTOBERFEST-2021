//Program to remove a sub-string from a string
#include<stdio.h>

char* shifter(char a[], char b[], int i, int j)
{
  for(int k = i; a[k] != '\0'; k++)
    a[k] = a[k+j];          //shifting the array forward
  return a;
}

int main(void)
{
  int i, j=0, flag=1;
  char* c;
  char a[100], b[100];
  printf("Enter the main String : ");
  scanf("%s", a);
  printf("Enter the Sub-String : ");
  scanf("%s", b);
  int l;
  for(l=0;b[l] != '\0'; l++);   //finding the length of b
  for(i=0;a[i] != '\0' && flag; i++)
  {
    if(a[i] == b[j])  //checking the pattern
    {
      if(j == l-1)    //checking whether the whole word(b) matches
      {
        flag = 0;
        c = shifter(a,b,i-j,j+1); //shifting
      }
      j++;
    }
    else  //resetting the counter when the pattern breaks
      j=0;
  }
  if(!flag)
    printf("New String : %s", c);
  else
    printf("No Modifications were made.");
  return 0;
}
