#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>
char name[0x100];

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    mprotect((void *)0x00404000, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC);
}

void banner() {
    puts("---------------------------------------------------\n"
         "███████╗██╗   ██╗██╗   ██╗ ██████╗████████╗███████╗\n"
         "██╔════╝██║   ██║██║   ██║██╔════╝╚══██╔══╝██╔════╝\n"
         "███████╗██║   ██║██║   ██║██║        ██║   █████╗  \n"
         "╚════██║╚██╗ ██╔╝██║   ██║██║        ██║   ██╔══╝  \n"
         "███████║ ╚████╔╝ ╚██████╔╝╚██████╗   ██║   ██║     \n"
         "╚══════╝  ╚═══╝   ╚═════╝  ╚═════╝   ╚═╝   ╚═╝     \n"
         "                                                   \n"
         "         WELCOME TO SVUCTF WINTER 2023         \n"
         "---------------------------------------------------");
}

void menu() {
    puts("1. Fujiya\n"
        "2. Huogai\n"
        "3. Unique Human Adventured");
    printf("Command:");
}

void vuln() {
    int x;
    char buf[0x100];

    printf("Input your favorite candy:\n");
    loop_start:
    menu();
    scanf("%d",&x);
    switch(x) {
        case 1 :
            read(0,name,0x100);
            goto loop_start;
        case 2 :
            printf("There's a candy voucher in the flag!\n");
            memset(buf,0,0x100);
            read(0,buf,0x100);
            printf(buf);
            goto loop_start;
        case 3 :
            puts("There is no Unique Human Adventured");
            break;
        default:
            printf("Don't you like all of them?\n");
            break;
    }
}

int main() {
    init();
    banner();
    vuln();

    return 0;
}
