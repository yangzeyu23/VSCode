#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "zylib.h"
#include "zyrandom.h"
const unsigned int n=30;
int a[30];
void GenerateIntegers(int a[], unsigned int n);
void PrintIntegers(int a[], unsigned int n);
int main()
{
    printf("-------------------------------\n");
    printf("The 30 unrepeated generated integers are:\n");

    srand((int)time(NULL));      //初始化随机数种子
    GenerateIntegers(a,n);
    PrintIntegers(a,n);

    system("pause");
    return 0;
}
void GenerateIntegers(int a[], unsigned int n)
{
    unsigned int i;
    for (i=0;i<n;i++)
    {
        a[i]=GenerateRandomNumber(10,99);
        for (unsigned int j=0;j<i;j++)
        {
            while (a[i]==a[j])
            {
                a[i]=GenerateRandomNumber(10,99);
            }
        }
    }
}
void PrintIntegers(int a[], unsigned int n)
{
    unsigned int i;
    for (i=0;i<n;i++)
    {
        i==15?printf("\n"):0;
        printf("%d  ",a[i]);
    }
}
