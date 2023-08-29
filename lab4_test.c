#include "types.h"
#include "stat.h"
#include "user.h"
#include "uspinlock.h"
struct shm_cnt { 
    struct uspinlock lock; 
    int cnt;
};

int main(int argc, char *argv[]){
    int pid;
    int i=0;
    struct shm_cnt *counter;
    int max = atoi(argv[1]); 
    pid=fork(); 
    sleep(1);
    shm_open(1,(char **)&counter);  
    for(i = 0; i < max; i++){ 
        uacquire(&(counter->lock)); 
        counter->cnt++; 
        if(i%1000 == 0) 
            printf(1,"-"); 
        urelease(&(counter->lock));
    } 
    uacquire(&(counter->lock)); 
    printf(1, "\nCNT_%d_\n", counter->cnt); 
    urelease(&(counter->lock)); 
    if(pid){ 
        wait(); 
    } 
    shm_close(1); 
    exit(); 
    return 0;
}
