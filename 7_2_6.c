#include <stdio.h>
#include "zylib.h"
#include "zyrandom.h"

void TransposeMatrix(int *p, unsigned int m, unsigned int n);

int main()
{
    int n,i,j;

    printf("This program will transpose a n*n matrix.\n");
    printf("----------------------------------------------------------\n");
    printf("Please input the size of the matrix: ");

    n=GetIntegerFromKeyboard();
    int a[n][n];

    printf("Let's generate a %d*%d matrix:\n", n, n);
    Randomize();
    for (int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            a[i][j]=GenerateRandomNumber(1, 100);
            j!=n? printf("%-4d", a[i][j]): printf("%d\n", a[i][j]);
        }
    }
    TransposeMatrix(a, n, n);
    printf("    \n");
    printf("The transposed matrix is:\n");
    for(i=0; i<n; i++)
    {
        for( j=0; j<n; j++)
        {
        j!=n? printf("%-4d", a[i][j]): printf("%d\n", a[i][j]);
        }
        printf("\n");
    }
    system("pause");
    return 0;
}

void TransposeMatrix(int *p, unsigned int m, unsigned int n)
{
    int temp;
    for(int i=0; i<m; i++)
    {
        for(int j=i+1; j<n; j++)
        {
            temp=*(p+i*n+j);
            *(p+i*n+j)=*(p+j*n+i);
            *(p+j*n+i)=temp;
        }
    }
}