#include <stdio.h>
#include "zylib.h"

unsigned int a,b;

int gcd(a,b);

int main()
{
    printf("This program calculates the greatest common divisor of two numbers.\n");
    printf("Please input the first number:");
    a=GetIntegerFromKeyboard();
    printf("Please input the second number:");
    b=GetIntegerFromKeyboard();

    printf("The greatest common divisor of %u and %u is %d\n", a, b, gcd(a, b));
    system("pause");
    return 0;
}

int gcd(unsigned int a, unsigned int b)
{
    int t,i=0;
    while (i<=a && i<=b)
    {
        i++;
        if (a%i==0 && b%i==0)  t=i ;
    }
    return t;
}