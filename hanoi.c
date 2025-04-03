#include <stdio.h>
#include "zylib.h"

unsigned int n;

typedef enum{X,Y,Z} HANOI;

void Welcome();
unsigned int GetInteger(CSTRING prompt);

STRING CovertHanoiToString(HANOI y);
void MovePlate(unsigned int n, HANOI from, HANOI to);
void MoveHanoi(unsigned int n, HANOI from, HANOI via, HANOI to);

int main()
{
    Welcome();
    n=GetInteger("Input the number of plates: ");
    MoveHanoi(n, X, Y, Z);
    system("pause");
    return 0;
}

void Welcome()
{
    printf("  Welcome to the Tower of Hanoi program.\n");
    printf("-----------------------------------------\n");
}

unsigned int GetInteger(CSTRING prompt)
{
    printf("%s", prompt);
    return GetIntegerFromKeyboard();
}

STRING  CovertHanoiToString(HANOI y)
{
    switch(y)
    {
        case X: return "X";
        case Y: return "Y";
        case Z: return "Z";
    default : return "Unknown";
    }
}

void MovePlate(unsigned int n, HANOI from, HANOI to)
{
    STRING from_str, to_str;
    from_str=CovertHanoiToString(from);
    to_str=CovertHanoiToString(to);
    printf("Move plate %d from %s to %s\n", n, from_str, to_str);
}

void MoveHanoi(unsigned int n, HANOI from, HANOI via, HANOI to)
{
    if(n==1)
        MovePlate(n, from, to);
    else
    {
        MoveHanoi(n-1, from, to, via);
        MovePlate(n, from, to);
        MoveHanoi(n-1, via, from, to);
    }
}
  
