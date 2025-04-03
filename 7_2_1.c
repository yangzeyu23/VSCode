#include <stdio.h>
#include "zylib.h"

void CalculateAverage(int *p, unsigned int n);

int main()
{
    int n;
    printf("Please input the number of integers:\n");
    n=GetIntegerFromKeyboard();
    int a[n];
    printf("Please input %d integers:\n", n);
    for(int i=0; i<n; i++)
    {
        scanf("%d", &a[i]);
    }
    CalculateAverage(a, n);

    system("pause");
    return 0;
}

void CalculateAverage(int *p, unsigned int n)
{
    int sum=0,i=0,k;
    for(i=0; i<n; i++)
    {
        sum+=*(p+i);
    }
    printf("The average of this array is: %f\n", (float)sum/n);
}