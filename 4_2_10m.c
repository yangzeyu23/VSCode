#include <stdio.h>
#include "zylib.h"

unsigned int n;
int k;

//定义这个函数是为了容错时的报错语句为ILLEGAL,使之与作业要求一致
int getIntegerFromKeyboard();


int Binom(int n, int k);         //二项式系数函数

int main() 
{
    n=getIntegerFromKeyboard();
    if (n<0)    printf("ILLEGAL\n");

    k=getIntegerFromKeyboard();
    if (k<0)    printf("ILLEGAL\n");

    while(n<k)
    {
        printf("ILLEGAL\n");
        k=getIntegerFromKeyboard();
    }   

    printf("%d\n",Binom(n,k));

    system("pause");
    return 0;
}

int Binom(n,k)
{
    if (k==0 || k==n)          return 1;
    return Binom(n-1,k-1)+Binom(n-1,k);
}








int  getIntegerFromKeyboard()
{
  while( TRUE )
  {
    int  _n;
    char  _junk;
    STRING  _s = GetStringFromKeyboard();
    switch( sscanf( _s, " %d %c", &_n, &_junk ) )
    {
    case 1:
      DestroyObject( _s );
      return _n;
    case 2:
      printf( "ILLEGAL\n" );
      break;
    default:
      printf( "ILLEGAL\n" );
      break;
    }
    DestroyObject( _s );
    printf( "" );
  }
}