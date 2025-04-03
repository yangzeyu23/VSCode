#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "zylib.h"
#define NDEBUG

unsigned int n;

BOOL IsPrime(unsigned int n);

int main()
{
    printf("This programm gets a number greater than 2 and determines whether it is a prime number.\n");
    printf("Please enter a number: ");
    n=GetIntegerFromKeyboard();
    if(n<=2)                            printf("Unexpected input!\n");
    else 
        if (IsPrime(n))                 printf("%d is a prime number.\n",n);
        else                            printf("%d is NOT a prime number.\n",n);
        
        system("pause");
        return 0;
}

BOOL IsPrime(unsigned int n)
{
    unsigned int i=3, t=(unsigned int)sqrt(n)+1;
    assert(n>2);
    if (n%2==0) return FALSE;
    while (i<=t) 
    {
        if (n%i==0) return FALSE;
        i+=2;
    }
    return TRUE;
}
