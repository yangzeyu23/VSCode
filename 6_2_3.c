#include <stdio.h>
#include "zylib.h"
#include <stdbool.h> 
//fgets函数: 从指定的流读取一行，并把它存储在str所指向的字符串内,stdin表示标准输入流

#define MAX_LENGTH 100      //定义宏替换最大字符串长度

BOOL isVowel(char c);
int findFirstVowelPosition(const char str[]);

int main() 
{
    char str[MAX_LENGTH];

    printf("Please enter a string: ");
    fgets(str, MAX_LENGTH, stdin); 

    int pos = findFirstVowelPosition(str);

    pos==-1? printf("There is no vowels in this string.\n") : 
    printf("The first vowel is at the position of : %d\n", pos); 
    
    system("pause");
    return 0;
}
// 判断字符是否是元音字母
BOOL isVowel(char c) 
{
    char vowels[] = "aeiouAEIOU";
    for (int i = 0; vowels[i] != '\0'; i++) 
    {
        if (c == vowels[i])   return true;
    }
    return false;
}
// 查找字符串中第一个元音字母的位置
int findFirstVowelPosition(const char str[]) 
{
    for (int i = 0; str[i] != '\0'; i++) 
    {
        if (isVowel(str[i]))  return i+1;
    }
    return -1;
}