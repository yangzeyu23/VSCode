#include <stdio.h>
#include "zyrandom.h"
#include "arrmanip.h"
static const unsigned int lower_bound=10;
static const unsigned int upper_bound=99;

void GenerateIntegers(int *p, unsigned int n)
{
    unsigned int i;
    Randomize();
    for(i=0; i<n; i++)
        *p++ = GenerateRandomNumber(lower_bound, upper_bound);
}

void ReverseIntegers(int *p, unsigned int n)
{
    unsigned int i;
    for(i=0; i<n/2; i++)
        Swap(p+i, p+n-i-1);
}

void Swap(int *a, int *b)
{
    int t;
    t = *a;
    *a = *b;
    *b = t;
}

void PrintIntegers(int *p, unsigned int n)
{
    unsigned int i;
    for(i=0; i<n; i++)
        printf("%-4d", *(p+i));
    printf("\n");
}


