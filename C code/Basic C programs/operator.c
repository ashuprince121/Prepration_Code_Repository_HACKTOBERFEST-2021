/*
	Author: AnOnYmOus001100
	Date: 01/10/2020

	Description: Code to demonstrate operators and operations on variables in C
*/

// including the header for i/o operations
#include <stdio.h>

int main()
{
	// initializing variables
	int num1 = 5, num2 = 10, num3 = 20, num;
	float num4 = 12.56, num5 = 3.75;

	// addition, + is used for addition
	printf("%d",5+3); // adding two numbers
	printf("%f",4.3+8.56);	// addition of two floating point numbers
	printf("%d",num1+num2);	// adding num1 and num2
	printf("%d",num1+num2+num3); // adding three numbers

	// subtraction, - opertor is used for subtraction
	printf("%d",10-7);	// subtraction of two numbers
	printf("%f",20.9-7.5);	// subtraction of two floating point numbers
	printf("%f",num4-num1); // subtracting num1 from num4
	printf("%d",num1-num2);	// subtracting num2 from num1
	printf("%d",num3-num2-num1); // subtracting num2 from num2 and then subtracting the result from num2, subtraction starts from left to right

	// multiplication, * is used for multiplication
	printf("%d",3*2);	// multiplying two numbers
	printf("%f",6.25*2.3);	// multiplication of two float numbers
	printf("%d",num3*num1); // multiplying num3 and num1
	printf("%f",num1*num5*num4);	// multiplication of num1, num4 and num5

	//division
	num = num2/num1; // assigning the result of num2 divided by num1
	printf("%d",80/10); // division of two numbers
	printf("%f",50.34/28.43); // division of two floating point numbers
	printf("%d",num);	// printing num
	printf("%f",num4/num2);	// dividing num4 by num2
	printf("%d",num1/num2); // dividing num1 by num2, will return 0 as it is integer division and the integer part is 0

return 0;
}

