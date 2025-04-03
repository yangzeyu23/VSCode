#include <stdio.h>
#include "zylib.h"

unsigned int n;
int k;

int EVA(int n);            //阶乘函数
int Binom(int n, int k);   //二项式系数函数

int main() {

    printf("This programm calculates binomical coefficients C_n^k.\n");
    printf("Please enter n:");
    n=GetIntegerFromKeyboard();
    printf("Please enter k:");
    k=GetIntegerFromKeyboard();
    printf("C_%u^%d=%d\n",n,k,Binom(n,k));

    system("pause");
    return 0;
}
int EVA(int n)
{
    int i=n,t=1;
    while(i>1)
    {
        t=t*i;
        i--;
    }
    return t;
}
int Binom(int n, int k)
{
    return EVA(n)/(EVA(k)*EVA(n-k));
}
