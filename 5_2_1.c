#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "zylib.h"


int main()
{
    printf("This programm prints a random number from 1~6.\n");
    srand((int)time(0));
    printf("A random number is %d.\n",rand()%6+1);

    system("pause");
    return 0;
}
