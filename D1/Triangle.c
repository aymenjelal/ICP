#include <stdio.h>

void printSpace(int rows,int sides){
    
    for(int j=0; j<sides-rows;j++){
            printf(" ");
       }
}

void printStar(int rows){
    for(int j=0; j<2*(rows+1)-1;j++){
            printf("*");
        }
}

int main()
{
    int sides;
    printf("enter number \n");
    scanf("%d",&sides);
    
    
    for (int rows=0;rows<sides;rows++){
        
        printSpace(rows,sides);
        
        printStar(rows);
        
        
        printf("\n");
    }

    return 0;
}