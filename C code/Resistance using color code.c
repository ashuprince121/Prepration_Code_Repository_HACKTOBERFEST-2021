#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ColorsSize (sizeof colors/sizeof *colors)

char *UnitFinder (char *ret, int inp);         //seprates unit digits
int FindColor (char *value);                  //search the index values in color codes
char *UpperToLower (char *trgt, char *src);   //converts upper case elements to lower case
int CompareColor (char *color1, char *color2);  //comparison between two color
char condition;

enum Colors {BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE, GOLD, SILVER, UNKNOWN};
enum {MinIn = 5, MaxIn = 12};

typedef float decimal;  // will replace decimal as float data type

decimal multiply[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 0.1, 0.01 };
decimal tolerance[] = { 0, 1, 2,0,0, 0.5, 0.25, 0.1, 0.05,0, 5, 10 };

struct colorList
{
	char *color_name;
	enum Colors id;
}

colors[] = {{"black", BLACK}, {"brown", BROWN}, {"red", RED}, {"orange", ORANGE}, {"yellow", YELLOW}, {"green", GREEN},
            {"blue", BLUE}, {"violet", VIOLET}, {"grey", GREY}, {"white", WHITE}, {"gold", GOLD}, {"silver", SILVER}};

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
	   printf("\n\t\t\t******************************************************************\n");
       printf("\t\t\t==================================================================\n");
       printf("\t\t\t	                  %c  WELCOME  %c\t\t\t\n",sml,sml);
	   printf("\t\t\t==================================================================\n"); 
	   printf("\t\t\t******************************************************************\n");
       printf("\n\n%s\n%s\n\t\t\t","\t\t\tEnter the color of 5 bands on resistor to calculate resistance","\t\t\tBegin with the last band (Nearest to farthest)\n");
       
	   for(i=0; i<MinIn;  i++)
	   {
	   	printf("\n\t\t\tBand %d : ", i+1);
	   	scanf("%s", &in[i]);
	   	color_id[i] = FindColor(in[i]);
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
	    printf("\n\t\t\t******************************************************************\n");
        printf("\t\t\t==================================================================\n");
        printf("\t\t\t	                 (>_<)  AW, SNAP!  (._.)\t\t\t\n");
	    printf("\t\t\t==================================================================\n"); 
	    printf("\t\t\t******************************************************************\n");
	   
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
            printf("\n\t\t\t******************************************************************\n");
            printf("\t\t\t==================================================================\n");
            printf("\t\t\t	                  ( ^_^)  HURRAY !!!  (^_^ )\t\t\t\n",sml,sml);
	        printf("\t\t\t==================================================================\n"); 
	        printf("\t\t\t******************************************************************\n");
            if(decpart>0)
            {
			  printf("\n\n\t\t\tResistance value is : %.2f Ohms \n\n\t\t\tTolerance value is: %.2f %%\n", resistance,tol);
			}
			else
			{
			  UnitFinder(NetResistance, intpart);
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

char *UnitFinder (char *ret, int inp)
{
	int i, j = 0, k = 0, tmp, x = 1;
	int p = 0;
	int count = 0;
	int n = inp;
	
	while(n != 0)  // count number of digit in number
	{
		n /= 10;
		++count;
	}
	char *ptr = malloc(sizeof(char) * (count + 1));   //allocate memory to pointer according to digit in number
	
	while(inp)
	{
		if(inp < 0)
		{
			printf("\n-");
			inp *= -1;
		}
		tmp = inp;
		
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
			ptr[p] = ((inp/x) + '0');  // stores the number as it is
			inp %= x;      
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
			ret[i] = *ptr;     // stores converted array into new array
			*(ptr ++);
		}
	}
	return ret;
}

int FindColor (char *value)
{
	int i;
    char LowerColor[MaxIn] = "";  // array to store all the input in lowercase
    UpperToLower (LowerColor, value); 
    for (i = 0; i < (int)ColorsSize; ++i) 
    if (*LowerColor == *(colors[i].color_name))
            if (!CompareColor(colors[i].color_name, LowerColor))  // checks for error
                return i;
    return -1;
}

char *UpperToLower (char *trgt, char *src)
{
	if(src == '\0' || trgt == '\0')   // check if input string is empty
	return NULL;
    char *ptr = trgt;
    
    while(*src != '\0')                  // runs until src aray reaches null character
        if (*src >= 'A'  && 'Z' >= *src)   // checks if src is has elements in upper case
        {
		  *ptr = *src | (1 << 5);     // convert to lower
           src++;
           ptr++;
		}
        else                            // if already in lower store as it is
            {
			*ptr = *src;                 
            ptr++;
            src++; 
			}
    *ptr = 0;
    return trgt;
}

int CompareColor (char *color1, char *color2)
{
    if (color1=='\0' && color2=='\0') return 0;   // checks if null array is being passed
    if (color1!='\0' && color2=='\0') return 1;
    if (color1=='\0' && color2!='\0') return -1;

    while(*color1 && *color2 && *color1 == *color2)  // runs the loop to increment color strings
	{
	  color1++ ;
	  color2++ ;
    }
    return *color1 - *color2;
}
