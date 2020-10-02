//Proram to check whether a given string is palindrome or not
#include<stdio.h>
#include<string.h>

int palin(char name[])
{
  int n = strlen(name);
  for(int i = 0; i < n/2; i++)
  {
    if(name[i] != name[n-i-1])
      return 0;
  }
  return 1;
}

int main(void)
{
  char name[100];
  printf("String Palindrome Checker\n");
  printf("^^^^^^^^^^^^^^^^^^^^^^^^^\n");
  printf("Enter the String : ");
  scanf("%s", name);
  if(palin(name))
    printf("\"%s\" is a palindrome.", name);
  else
    printf("\"%s\" is not a palindrome.", name);
  return 0;
}
