#include <stdio.h>
#include "zylib.h"
int n;
void judge(int n);            //判断函数
void InputNaturalNumber();    //输入审查函数
int main() {
    printf("This program will determine whether a natural number is a perfect number or not.\n");
    InputNaturalNumber();
    judge(n);
    system("pause");
    return 0;
}
void judge(int n) 
{
    if (n == 0)  printf("0 is not a perfect number.\n");
    else
    {    int sum = 0;
        for (int i = 1; i < n; i++) 
        {
            if (n % i == 0)  sum += i;
        }
        sum == n?
        printf("%d is a perfect number.\n", n):printf("%d is not a perfect number.\n", n);
    }
}
void InputNaturalNumber() 
{
    printf("Please enter a natural number: ");
    n=GetIntegerFromKeyboard();
    while (n < 0) 
    {
        printf("%d is NOT a natural number!\n", n);
        printf("Please try again: ");
        n=GetIntegerFromKeyboard();
    }
}