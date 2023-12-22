#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    printf("Content-type: text/html\n\n");
    printf("<html><head><title>Login</title></head><body>\n");
    printf("<h1>Login</h1>\n");

    const char* req_method = getenv("REQUEST_METHOD");
    if (!strcmp(req_method, "POST")) {
        const char* len_str = getenv("CONTENT_LENGTH");
        const int content_length = atoi(len_str);

        char* post_data = malloc(content_length + 1);
        fgets(post_data, content_length + 1, stdin);

        char username[50], password[50];
        sscanf(post_data, "username=%[^&]&password=%s", username, password);
        free(post_data);

        printf("<p>Welcome %s!</p>\n", username);

        if (!strcmp(username, "pn1fg") && !strcmp(password, "pxpx")) {
            char flag[50];
            FILE* fp = fopen("/flag", "r");
            fgets(flag, 50, fp);
            fclose(fp);
            printf("<p>%s</p>\n", flag);
        }
    }

    printf("</body></html>");
    return 0;
}
