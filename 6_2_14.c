#include <stdio.h>
#include "zylib.h"

typedef enum{N,X,O} TTT;
TTT phase[3][3];

#define N_ " "
#define X_ "X"
#define O_ "O"

int main()
{
    TTT phase[3][3] ={
        {X, X, X},
        {N, N, N},
        {O, O, O}
    };
printf("-----------------------\n");
printf("%s  ", phase[0][0]==N?N_:phase[0][0]==X?X_:O_);
printf("%s  ", phase[0][1]==N?N_:phase[0][1]==X?X_:O_);
printf("%s\n", phase[0][2]==N?N_:phase[0][2]==X?X_:O_);
printf("%s  ", phase[1][0]==N?N_:phase[1][0]==X?X_:O_);
printf("%s  ", phase[1][1]==N?N_:phase[1][1]==X?X_:O_);
printf("%s\n", phase[1][2]==N?N_:phase[1][2]==X?X_:O_);
printf("%s  ", phase[2][0]==N?N_:phase[2][0]==X?X_:O_);
printf("%s  ", phase[2][1]==N?N_:phase[2][1]==X?X_:O_);
printf("%s\n", phase[2][2]==N?N_:phase[2][2]==X?X_:O_);
printf("-----------------------\n");
system("pause");
return 0;
}