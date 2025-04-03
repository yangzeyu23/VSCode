#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>  //strcmp函数
#include "zylib.h"

int main()
{
    int a,b;
    STRING n;

    printf("-----------------------------------------------\n");
    printf("This programm is a dice game.\n");
    srand((int)time(NULL));
    a=rand()%6+1;
    printf("Firstly, let me throw the dice------\n");
    printf("My result is %d.\n",a);
    printf("Now, it's your turn.Please enter \"g\" to throw your dice------");
    n=GetStringFromKeyboard();
    
    while(strcmp(n,"g")!=0)
    {
        printf("Unexpected input! Please try again:\n");
        n=GetStringFromKeyboard();
    }

    b=rand()%6+1;
    printf("\nYour result is %d.\n",b);
    a>b?printf("You lose!\n"):printf("You win!\n");
    printf("-----------------------------------------------\n");

    system("pause");
    return 0;
}