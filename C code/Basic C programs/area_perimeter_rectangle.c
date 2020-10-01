/* 
	Author: AnOnYmOus001100
	Date: 02/10/2020

	Descripton: This program calculates the perimeter and area of a rectangle and outputs the result.
	*Note: Can be used to calculate perimeter and area of square also
	(height and width needs to be same)
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
	// variable decalaration and initialization
    double height, width, area = 0.0, perimeter = 0.0;

	// calculating perimeter
    perimeter = 2 * (height + width);
	
	// calculating area
    area = height * width;

	// input prompt
	printf("Enter the height and width: ");
	scanf("%lf %lf",&height,&width);

	// output
    printf("\nThe perimeter of the rectangle is %lf.",perimeter);
    printf("\nThe area of the rectangle is %f.",area);

    return 0;
}
