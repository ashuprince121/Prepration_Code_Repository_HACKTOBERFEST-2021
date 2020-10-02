//Program to find the factorial of a number
#include<stdio.h>

unsigned long long int factorial(int n)
{
  unsigned long long int fact = 1;
  for(int i = 2; i<=n; i++)
    fact *= i;
  return fact;
}


int main()
{
  unsigned long long int fact;
  int n;
  printf("Factorial Calculator\n");
  printf("^^^^^^^^^^^^^^^^^^^^\n");
  printf("Enter the number : ");
  scanf("%d", &n);
  fact = factorial(n);
  printf("%d! = %llu", n, fact);
  return 0;
}
