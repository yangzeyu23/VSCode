#include <stdio.h>
#include "zylib.h"

int main()
{
    double n;
    n=GetRealFromKeyboard();
    if ((int)n==n)
    {
        printf("n is an integer.\n");
    }
    else
    {
        printf("n is not an integer.\n");
    }
}