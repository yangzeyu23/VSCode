#include <stdio.h>
#include "zylib.h"

int main()
{
    printf(" X | X | X \n");
    printf("---+---+---\n");
    printf("   |   |   \n");
    printf("---+---+---\n");
    printf(" 0 | 0 | 0 \n");
    
    int x,y,a,b,c,d;
    printf("The program gets two integers, and calculates their sum, difference, procuct and quotient.\n");
    printf("The first number:");
    scanf("%d",&x);
    printf("The second number:");
    scanf("%d",&y);
    a=x+y;
    b=x-y;
    c=x*y;
    d=x/y;
    printf("The sum is %d\n",a);
    printf("The difference is %d\n",b);
    printf("The product is %d\n",c);
    printf("The quotient is %d\n",d);
    return 0;
}
