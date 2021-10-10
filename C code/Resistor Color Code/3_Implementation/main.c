#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "inc/header.h"

// Initialization starts
char *DigitSeparate (char *ret, int inp);         //seprates unit digits
int Color (char *value);                  //search the index values in color codes
char *Converter (char *trgt, char *src);   //converts upper case elements to lower case
int ColorMatch (char *color1, char *color2);  //comparison between two color
char condition;
enum {MinIn = 5, MaxIn = 12};
typedef float decimal;  // will replace decimal as float data type
decimal multiply[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 0.1, 0.01 };
decimal tolerance[] = { 0, 1, 2,0,0, 0.5, 0.25, 0.1, 0.05,0, 5, 10 };
// Initialization ends

int main (void)
{
	int i;
	int m, n;      // m stores resistance value , n stores tolerance value
	int sml = 1;   // used to print emoji in console
	decimal tol;     // stores tolerance value
	int invalid = 0;       // stores the times invalid input is entered
	int color_id[MinIn];     // stores values to color
	
	char in[MinIn][MaxIn];    // to store input from user
	char wrong[MinIn][MaxIn];  // used to store wrong entered values
	
	decimal resistance = 0;        // stores resistance before unit sepration
	char NetResistance[20] = "";  // stores resistance after unit speration
	
	do
	{
	   system("cls");
	   printf("\n\t\t\t************************\n");
       printf("\t\t\t==================================================================\n");
       printf("\t\t\t	                  %c  WELCOME  %c\t\t\t\n",sml,sml);
	   printf("\t\t\t==================================================================\n"); 
	   printf("\t\t\t************************\n");
       printf("\n\n%s\n%s\n\t\t\t","\t\t\tEnter the color of 5 bands on resistor to calculate resistance","\t\t\tBegin with the last band (Nearest to farthest)\n");
       
	   for(i=0; i<MinIn;  i++)
	   {
	   	printf("\n\t\t\tBand %d : ", i+1);
	   	scanf("%s", &in[i]);
	   	color_id[i] = Color(in[i]);
	   }
	   
	   for(i=0; i<MinIn; i++)
	   {
	   	if(color_id[i] == -1)
	   	{
	   		invalid++;
	   		strcpy(wrong[i], in[i]);
		   }
	   }
	   if(invalid>0)
	   {
	   	system("cls");
	    printf("\n\t\t\t************************\n");
        printf("\t\t\t==================================================================\n");
        printf("\t\t\t	                 (><)  AW, SNAP!  (..)\t\t\t\n");
	    printf("\t\t\t==================================================================\n"); 
	    printf("\t\t\t************************\n");
	   
	   if (invalid == 1)
        {
            printf("\n\n\t\t\tInvalid colour: %s\n", wrong[0]);
        }
        else if (invalid == 2)
        {
            printf("\n\n\t\t\tInvalid colours: %s, %s\n", wrong[0], wrong[1]);
        }
        else if (invalid == 3)
        {
            printf("\n\n\t\t\tInvalid colours: %s, %s, %s\n", wrong[0], wrong[1], wrong[2]);
        }
        else if (invalid == 4)
        {
            printf("\n\n\t\t\tInvalid colours: %s, %s, %s, %s\n", wrong[0], wrong[1], wrong[2], wrong[3]);
        }
        else 
        {
            printf("\n\n\t\t\tInvalid colours: %s, %s, %s, %s, %s\n", wrong[0], wrong[1], wrong[2], wrong[3], wrong[4]);
        }
	   }
	   
	   else
	   {
	   	for(i=0; i < (MinIn-2); i++)
	   	{
	   		resistance = (resistance*10) + color_id[i];
		   }
		   m = color_id[3];
		   n = color_id[4];
		   resistance *= multiply[m];
		   char *NetResistance = malloc(sizeof(char) * (resistance + 1)); 
		   int intpart = (int)resistance;     // stores the integer part of resistance
		   decimal decpart = resistance - intpart;   // stores deciaml part of resistance
		   tol = tolerance[n];
		    system("cls");
            printf("\n\t\t\t************************\n");
            printf("\t\t\t==================================================================\n");
            printf("\t\t\t	                  ( ^^)  HURRAY !!!  (^^ )\t\t\t\n",sml,sml);
	        printf("\t\t\t==================================================================\n"); 
	        printf("\t\t\t************************\n");
            if(decpart>0)
            {
			  printf("\n\n\t\t\tResistance value is : %.2f Ohms \n\n\t\t\tTolerance value is: %.2f %%\n", resistance,tol);
			}
			else
			{
			  DigitSeparate(NetResistance, intpart);
			  printf("\n\n\t\t\tResistance value is : %s Ohms \n\n\t\t\tTolerance value is: %.2f %%\n", NetResistance,tol);
			}			      
	   }
	   invalid = 0;     // reset vairables here
	   resistance = 0;
	   
	   for(i=0; i<MinIn; i++)
	   {
	   	color_id[i] = 0;
	   }
	   printf("\n\n\t\t\tWould you like to start over again ? \n\t\t\tPlease enter 'Y' or 'y' for YES : ");
       fflush(stdin) ;      // clear the buffer
       scanf("\n%c", &condition);
       
       if(condition == 'Y' || condition =='y');
       else break;
    }
    while(condition == 'Y' || condition =='y');
    return 0;	
}


