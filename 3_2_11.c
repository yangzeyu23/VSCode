#include <stdio.h>
#include "zylib.h"

int year,month,totaldays,weekday,days_of_month;

typedef enum{SUN,MON,TUE,WED,THU,FRI,SAT} WEEKDAY;
const WEEKDAY date_1=THU;

BOOL IsLeap(int year);
int Days(int month);
int Monthdays(int month);

int main()
{
    printf("This programm prints a monthly calendar you want after 2015 A.D. .\n");   
    printf("Please enter the year: ");
    year=GetIntegerFromKeyboard();
    printf("Please enter the month: ");
    month=GetIntegerFromKeyboard();
    
    if(year<2015||month<1||month>12)
    {
        printf("Unexpected input!\n");
        return 1;
    }
    
    totaldays=(year-2015)*365+(year-2013)/4-(year-1-2000)/100+(year-1-2000)/400+Monthdays(month-1)+1;
    weekday=(WEEKDAY)((totaldays+(int)date_1-1)%7);  

    printf("              %d-%d              \n",year,month);
    printf("-----------------------------------\n");
    printf(" Sun  Mon  Tue  Wed  Thu  Fri  Sat\n");
    printf("-----------------------------------\n");
    switch(weekday)
    {
        case SUN: printf(" 1");        break;
        case MON: printf("      1");        break;
        case TUE: printf("           1");       break;
        case WED: printf("                1");       break;
        case THU: printf("                     1");       break;
        case FRI: printf("                          1");       break;
        case SAT: printf("                               1");       break;
    default:  ;
    }
    for(int i=2;i<=Days(month);i++)
    {       
        if (i==10 && (i+weekday-1)%7!=0)       printf("%6d",i);                   
        else if ((i+weekday-1)%7==0)           printf("\n %d",i);
        else                                   printf("%5d",i);
    }
printf("\n-----------------------------------\n");       

    system("pause");
    return 0;
}

BOOL IsLeap(int year)
{
    return year%4==0&&year%100!=0||year%400==0;
}

int Days(int month)
{
    switch(month)
    {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            days_of_month=31;
            break;
        case 4: case 6: case 9: case 11:
            days_of_month=30;
            break;
        case 2:
            days_of_month=28+(int)IsLeap(year);
            break;
    }
    return days_of_month;
}

int Monthdays(int month)
{
    if (month==0)         return 0;
    else if (month==1)    return 31;
    else                  return Days(month)+Monthdays(month-1);
}