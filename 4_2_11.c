#include <stdio.h>
#include "zylib.h"

int n;
int SumOfDigits(int n);


int main()
{
    printf("This program calculates the sum of the digits of a natural number.\n");
    printf("Please enter a natural number:");
    n = GetIntegerFromKeyboard();

    n<0?printf("Wrong input!"): 
    printf("The result is %d.\n", SumOfDigits(n));
 
    system("pause");
    return 0;
}

int SumOfDigits(int n)
{
    if (n<10) return n;
    return n%10 + SumOfDigits(n/10);
}
