//Program to find the roots of a quadratic equation
#include<stdio.h>
#include<math.h>

//stores data related to a quadratic equation
typedef struct equation
{
  double a;
  double b;
  double c;
  double d;
  double r1;
  double r2;
}equation_t;


//Function to determine the solution of the qudratic equation
void solver(equation_t* p)
{
  double a = p->a;
  double b = p->b;
  double c = p->c;
  double d = (b*b)-(4*a*c);
  double r1, r2;

  if(d > 0)
  {
    r1 = ( -b + sqrt(d)) / (2 * a);
    r2 = ( -b - sqrt(d)) / (2 * a);
  }
  else if(d == 0)
  {
    r1 = r2 = -b/(2*a);
  }
  else
  {
    r1 = -b/(2*a);
    r2 = sqrt(-d)/(2*a);
  }
  p->d = d;
  p->r1 = r1;
  p->r2 = r2;
}
//Function to print the solution of the quadratic equation
void print(equation_t p)
{
  if(p.d > 0)
  {
    printf("\nRoots are Distinct\n");
    printf("Root 1 : %.4lf\n", p.r1);
    printf("Root 2 : %.4lf\n", p.r2);
  }
  else if(p.d == 0)
  {
    printf("\nRoots are Equal\n");
    printf("Root 1 : %.4lf\n", p.r1);
    printf("Root 2 : %.4lf\n", p.r2);
  }
  else
  {
    printf("\nRoots are Complex");
    printf("Root 1 : %.4lf+%.4lfi\n", p.r1, p.r2);
    printf("Root 2 : %.4lf-%.4lfi\n", p.r1, p.r2);
  }
}

//reading input from user
void read()
{
  equation_t p;
  printf("Enter the coefficent of x squared : ");
  scanf("%lf",&p.a);
  printf("Enter the coefficent of x         : ");
  scanf("%lf",&p.b);
  printf("Enter the constant                : ");
  scanf("%lf",&p.c);
  solver(&p);
  print(p);
}

//main function
int main(void)
{
  int flag = 1;
  int ch;
  while(flag)
  {
    printf("\n\nQuadratic Equation Solver\n");
    printf("^^^^^^^^^^^^^^^^^^^^^^^^^^^\n");
    printf("1. Solve the equation\n");
    printf("2. Exit\n");
    printf("  Enter your choice : ");
    scanf("%d", &ch);
    switch(ch)
    {
        case 1: read();
                break;
        case 2: flag=0;
                break;
        default: printf("Wrong Choice !!!");
    }

  }
}
