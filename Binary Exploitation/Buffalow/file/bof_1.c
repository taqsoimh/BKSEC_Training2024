#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    setbuf(stdout, NULL);
    int flag = 0xdeadbeef;
    char buf[50] = {0};
    printf("Enter your favorite number: ");
    fgets(buf, 0x64, stdin);

    if (flag == 0x13141516)
    {
        FILE *fp = fopen("flag.txt", "r");
        char flag[100];
        fgets(flag, sizeof(flag), fp);   
        puts(flag);
    }
    return 0;
}