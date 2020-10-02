//program to print the prime numbers in a given range
#include<stdio.h>

int main(void)
{
  int a,b,flag1 = 1,flag2 = 1;
  printf("Prime Numbers in a range\n");
  printf("^^^^^^^^^^^^^^^^^^^^^^^^\n");
  printf("Enter the range (eg: 1<space>100) : ");
  scanf("%d %d", &a, &b);
  for(int i = a; i <= b; i++)
  {
    if(i < 2)
      continue;
    for(int j=2;j<=i/2;j++)
    {
      if(i%j==0)
      {
        flag1 = 0;
        break;
      }
    }
    if(flag1)
    {
      if(flag2)
      {
        printf("Prime numbers in the given range\n");
        flag2 = 0;
      }
      printf("%d ", i);
    }
    flag1 = 1;
  }
  if(flag2)
    printf("There were no prime numbers in the given range.\n");
  return 0;
}
