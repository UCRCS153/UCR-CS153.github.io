#include "types.h"
#include "user.h"

void getParent(void){
    int pid1, pid2;
    pid1 = fork();
    if (pid1 == 0) {
        sleep(10);
    } else {
        pid2 = fork();
        if (pid2 == 0) {
            // check if the sibling is pid1
            // printf(1, "getsiblings pid %d\n", getsiblings());
            if (pid1 == getsiblings()) {
                printf(1, "%d\n", 0);
            } else {
                printf(1, "%d\n", 1);
            }
        }
    }
    wait();
    wait();
    return;
}

int main(int argc, char *argv[])
{
    // printf(1, "\nlab1 part1: test getsiblings\n");
    getParent();
    exit();
    // return 0;
}
