#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) 

{
	int angle1, angle2, angle3, sum;
	printf("Enter three angles of triangle: \n");
	scanf("%d, %d, %d", &angle1, &angle2,&angle3);
	
	sum = angle1 + angle2 + angle3;
	 
	if(sum == 180 && angle1 != 0 && angle2 != 0 && angle3 != 0)
	{
		printf("Triangle is valid.");
	}
	else
	{
		printf("Triangle is not valid.");
	}
	
	return 0;
}
