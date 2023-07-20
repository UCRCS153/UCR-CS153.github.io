#include "types.h"
#include "user.h"

void getParent(void){
    int pid = getpid();
    int ret = fork();
    if(ret == 0){
        int ppid_child = getppid();
        if (pid == ppid_child){
            printf(1, "%d\n", 0);
        }
        else{
            printf(1, "%d\n", 1);
        }
    }
    else if (ret > 0) {
        sleep(1);
        return;
    }
    else{
        printf(2, "\nError using fork\n");
    }
}

int main(int argc, char *argv[])
{
    printf(1, "\nlab1 part1: test getppid\n");
    getParent();
    // exit();
    return 0;
}
