//Program to find the factorial of a number recursively
#include<stdio.h>

unsigned long long int factorial(int n)
{
  if(n <= 1)
    return 1;
  else
    return n*factorial(n-1);
}


int main()
{
  unsigned long long int fact;
  int n;
  printf("factorial Calculator\n");
  printf("^^^^^^^^^^^^^^^^^^^^\n");
  printf("Enter the number : ");
  scanf("%d", &n);
  fact = Factorial(n);
  printf("%d! = %llu", n, fact);
  return 0;
}
