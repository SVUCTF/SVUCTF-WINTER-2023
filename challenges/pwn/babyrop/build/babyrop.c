#include <stdio.h>

void init() {
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
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

void gadget() {
    asm("pop %rdx; ret");
}

void vuln() {
    char buf[100];
    char buff[30] = "Do you know buffer overflow?\n";

    write(1,buff,sizeof(buff));
    read(0,buf,0x200);
}

int main() {
    init();
    banner();
    vuln();

    return 0;
}
