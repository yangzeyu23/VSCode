#include <stdio.h>
#include "zylib.h"

unsigned int n;
int k;

int Binom(n,k);   //二项式系数函数

int main() {

    printf("This programm calculates binomical coefficients C_n^k again.\n");
    printf("Please enter n:");
    n=GetIntegerFromKeyboard();
    printf("Please enter k:");
    k=GetIntegerFromKeyboard();
    printf("C_%u^%d=%d\n",n,k,Binom(n,k));

    system("pause");
    return 0;
}

int Binom(n,k)
{
    if (k==0 || k==n)          return 1;
    return Binom(n-1,k-1)+Binom(n-1,k);
}