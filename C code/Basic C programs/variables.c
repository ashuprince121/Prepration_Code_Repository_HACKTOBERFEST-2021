/*
        Author: AnOnYmOus001100
        Date: 01/10/2020

	A Code to demonstrate variables and variable types in C
	This code perfoms variable assignment and printing the values
*/

// header of i/o operations
#include <stdio.h>

int main()
{
	// variable declaration, variables are like containers that can hold a value of a particular data type
	// C is statically typed, so have to specify data type during the declaration like(int, float etc.)

	// integer variables holds integer numbers
	int num1, num2,num;

	// float variable holds floating point numbers
	float num3, num4, num_float;

	// double variable holds longer floating point numbers
	double num5, num6 = 6.89077, num_double;	// initialising num6 to 6.89077, means to assign a value to variable during declaration 

	// character variable holds a single character
	char c = 'a',c_un;

	// variable assignment
	num1 = 1;
	num2 = 2;
	num3 = 5.2, num4 = 6.7;	// multiple variables can be assigned on the same line using commas
	num5 = 112.88989890;

	// printing the values of the variables
	// here %d is a called format specifier and used to print the decimal or integer value
	printf("%d %d\n",num1,num2);	// prints values stored in num1 and num2
	// un-initialised integer variables hold 0
	printf("%d\n",num);
	// %f is used to print float values
	printf("%f %f\n",num3,num4);
	// un-initialised float variables hold 0.0
	printf("%f\n",num_float);
	// %lf is used for double numbers representation
	printf("%lf %lf\n",num5,num6);
	// uninitialised double holds 0.000000
	printf("%lf\n",num_double);
	// %c is used to print characters
	printf("%c\n",c);
	// non-initialised character variables holds nothing
	printf("%c",c_un);
	
return 0;
}
