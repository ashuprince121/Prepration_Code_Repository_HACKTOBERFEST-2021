#include "stddef.h"

#include "string.h"

char *Converter (char *target, char *source)
{
	if(!source || !target)    // check if input string is empty
	return NULL;
    char *ptr = target;
    
    while(*source)                  // runs until src aray reaches null character
        if (*source >= 'A'  && 'Z' >= *source)   // checks if src is has elements in upper case
        {
		  *ptr = *source | (1 << 5);     // convert to lower
           source++;
           ptr++;
		}
        else                            // if already in lower store as it is
            {
			*ptr = *source;                 
            ptr++;
            source++; 
			}
    *ptr = 0;
    return target;
}