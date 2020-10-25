#include<stdio.h>
int main()
{
	float bs,da,hra,gs;	//bs = basic salary, da = dearness allowance, hra = house rent allowance, gs = gross allowance 
	printf("Enter the basic salary: ");
	scanf("%f",&bs);
	hra = bs*20/100;
	da = bs*40/100;
	gs = bs+hra+da;
	printf("Gross salary : %f",gs);
	return 0;
}
