#include "header.h"
#include "string.h"



#define ColorsSize (sizeof colors/sizeof *colors)

enum {MinIn = 5, MaxIn = 12};

enum Colors {BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE, GOLD, SILVER, UNKNOWN};
struct colorList
{
	char *color_name;
	enum Colors id;
}colors[] = {{"black", BLACK}, {"brown", BROWN}, {"red", RED}, {"orange", ORANGE}, {"yellow", YELLOW}, {"green", GREEN},
            {"blue", BLUE}, {"violet", VIOLET}, {"grey", GREY}, {"white", WHITE}, {"gold", GOLD}, {"silver", SILVER}};








int Color (char *ColorName)
{
	int i;
    char LowerColor[MaxIn] = "";  // array to store all the input in lowercase
    Converter (LowerColor, ColorName); 
    for (i = 0; i < (int)ColorsSize; ++i) 
    if (*LowerColor == *(colors[i].color_name))
            if (!ColorMatch(colors[i].color_name, LowerColor))  // checks for error
                return i;
    return -1;
}
