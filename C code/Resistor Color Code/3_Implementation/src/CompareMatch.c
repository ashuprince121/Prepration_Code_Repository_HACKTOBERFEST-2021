
#include "string.h"


int ColorMatch (char *SampleColor, char *InputColor)
{
    if (*SampleColor=='\0' && *InputColor=='\0') return 0;   // checks if null array is being passed
    if (*SampleColor!='\0' && *InputColor=='\0') return 1;
    if (*SampleColor=='\0' && *InputColor!='\0') return -1;

    while(*SampleColor && *InputColor && *SampleColor == *InputColor)  // runs the loop to increment color strings
	{
	  *SampleColor++ ;
	  *InputColor++ ;
    }
    return *SampleColor - *InputColor;
}