#include <stdio.h>
#include "zylib.h"
int main()
{
    double a,b,d;
    int c;
    char str1[100]="please input the principal amount of your deposit:";
    printf("%s\n",str1);
    scanf("%lf",&a);
    char str2[100]="please input the annual interest rate:";
    printf("%s\n",str2);
    scanf("%lf",&b);
    char str3[100]="please input the number of years:";
    printf("%s\n",str3);
    scanf("%d",&c);
    d=a*(1+b/100*c);
    printf("your money number is:  %lf\n",d);
    printf("---------------------------------------------------\n");
    printf("COUNTRY  AREA(10K km2)   POP.(10K)  GDP(Billion$)\n");
    printf("---------------------------------------------------\n");
    STRING  s1,s2,s3,s4,s5;
    double a1,a2,a3,a4,a5;
    double p1,p2,p3,p4,p5;
    double g1,g2,g3,g4,g5;
    s1="China"; s2="Iceland"; s3="India"; s4="Madagascar"; s5="Maldive";
    a1=960, a2=10.3, a3=297.47000, a4=62.7, a5=0.03;
    p1=135700, p2=32.3,p3=125200, p4=2292, p5=34.5;
    g1=9240, g2=15.33, g3=1877, g4=10.61, g5=2.30;
    printf("%-10s  %10.2lf  %10.2lf  %-10.2lf \n",s1,a1,p1,g1);
    printf("%-10s  %10.2lf  %10.2lf  %-10.2lf \n",s2,a2,p2,g2);
    printf("%-10s  %10.2lf  %10.2lf  %-10.2lf \n",s3,a3,p3,g3);
    printf("%-10s  %10.2lf  %10.2lf  %-10.2lf \n",s4,a4,p4,g4);
    printf("%-10s  %10.2lf  %10.2lf  %-10.2lf \n",s5,a5,p5,g5);
    printf("---------------------------------------------------\n");
    return 0;
}
