
#include "string.h"
#include "stdlib.h"
#include "stdio.h"



char *DigitSeparate (char *returnn, int input)
{
	int i, j = 0, k = 0, tmp, x = 1;
	int p = 0;
	int count = 0;
	int n = input;
	
	while(n != 0)  // count number of digit in number
	{
		n /= 10;
		++count;
	}
	char *ptr = malloc(sizeof(char) * (count + 1));   //allocate memory to pointer according to digit in number
	
	while(input)
	{
		if(input < 0)
		{
			printf("\n-");
			input *= -1;
		}
		tmp = input;
		
		while(tmp > 0)   //until array becomes 0
		{
			tmp /= 10;     // divide by 10 to find units
			x *= 10;
			j++;
		}
		i = (j % 3);
		x /= 10;
		
		while(j > 0)
		{
			ptr[p] = ((input/x) + '0');  // stores the number as it is
			input %= x;      
			x /= 10;
			j--;
			k++;
			i--;
			p++;
			
			if((k%3 == 0 && j>0) || (i == 0 && j>2))  // checks for placing , at right place
			{
				ptr[p] = ',';
				p++;
				k = 0;
			}
		}
		for(i=0; i < (count+1); i++)
		{
			returnn[i] = *ptr;     // stores converted array into new array
			*(ptr ++);
		}
	}
	return returnn;
}