#include<stdio.h>
#include<math.h>

//for tagging the type of root
typedef enum type
{
  DISTINCT,
  EQUAL,
  COMPLEX
}type_t;

//stores data related to a quadratic equation
typedef struct equation
{
  float a;
  float b;
  float c;
  float r1;
  float r2;
  type_t tag;
}equation_t;

//determines the value of discriminent
int checker(int a, int b, int c)
{
  float determinant = (b*b)-(4*a*c);
  if(determinant>0)
    return 1;
  else if(determinant<0)
    return -1;
  else
    return 0;
}

//determine whether the roots are distinct, equal or complex
type_t tager(int a, int b, int c)
{
  int check = checker(a,b,c);
  if(check == -1)
    return  COMPLEX;
  if(check == 0)
    return EQUAL;
  else
    return DISTINCT;
  }

//determines the solution when the roots are distinct
int dist_solver(equation_t* p)
{
  int a = p->a;
  int b = p->b;
  int c = p->c;
  int d = (b*b)-(4*a*c);
  p->r1 = ( -b + sqrt(d)) / (2* a);
  p->r2 = ( -b - sqrt(d)) / (2* a);
  return 1;
}

//determines the solution when the roots are equal
int equa_solver(equation_t* p)
{
  int a = p->a;
  int b = p->b;
  p->r1 = p->r2 = -b/(2*a);
  return 1;
}

//determine the solution, when the roots are complex
int comp_solver(equation_t* p)
{
  int a = p->a;
  int b = p->b;
  int c = p->c;
  int d = (b*b)-(4*a*c);
  printf("Roots are Complex\n");
  printf("Root 1 : %.2f+%.2fi\n",-(float)b/(2*a),sqrt(-d)/(2*a));
  printf("Root 2 : %.2f-%.2fi\n",-(float)b/(2*a),sqrt(-d)/(2*a));
  return 0;
}

//solves the equation by calling required functions
int solver(equation_t* p)
{
  p->tag = tager(p->a,p->b,p->c);
  if(p->tag == DISTINCT)
    dist_solver(p);
  else if(p->tag == EQUAL)
    equa_solver(p);
  else if(p->tag == COMPLEX)
    comp_solver(p);
}

//reading input from user
void read()
{
  equation_t p;
  printf("Enter the coefficent of x squared : ");
  scanf("%f",&p.a);
  printf("Enter the coefficent of x         : ");
  scanf("%f",&p.b);
  printf("Enter the constant                : ");
  scanf("%f",&p.c);
  if(solver(&p))
  {
    if(p.tag == DISTINCT)
      printf("Roots are Distinct\n");
    else
      printf("Roots are Equal\n");
    printf("Root 1 : %.2f\n",p.r1);
    printf("Root 2 : %.2f\n",p.r2);
  }
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
