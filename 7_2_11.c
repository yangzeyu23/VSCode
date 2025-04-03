#include <stdio.h>
#include "zylib.h"

STRING s1, s2;

int GetString(CSTRING prompt);

int strcmp(const char *s1, const char *s2);

int main()
{
    s1=GetString("Please enter s1:\n");
    s2=GetString("Please enter s2:\n");
    printf("The result of comparison: %2d\n", strcmp(s1, s2));

    system("pause");
    return 0;
}

int GetString(CSTRING prompt)
{
    printf("%s", prompt);
    return GetStringFromKeyboard();
}

int strcmp(const char *s1, const char *s2)
{
    while(*s1==*s2)
    {
        if(*s1=='\0')
            return 0;
        s1++;
        s2++;
    }
    return *s1-*s2;
}

