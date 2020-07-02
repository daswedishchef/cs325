#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

void badsort(int *mylist,int n){
    if(n==2 && mylist[0]>mylist[1]){
        int temp = mylist[0];
        mylist[0] = mylist[1];
        mylist[1] = temp;
    }
    else if(n>2){
        float a = 0.666;
        int m = (int)(a*n);
        int *mysub = &mylist[0];
        badsort(mysub,m-1);
        mysub = &mylist[n-m];
        badsort(mysub,m);
        mysub = &mylist[0];
        badsort(mysub,m-1);
    }
}

int main(int argc,char *argv[]){
    srand(time(NULL));
    time_t time0, time1;
    int i;
    int size = atoi(argv[1]);
    int *randint = malloc(size+1*sizeof(int));
    for(i=0;i<size;i++){
        randint[i] = rand() % 10000;
    }
    clock(&time0);
    badsort(randint,size);
    clock(&time1);
    double mytime = (double)(time1-time0);
    printf("\nTime: %1.6f\n",time1);
    printf("\nsize: %d\n",size);
    for(i=0;i<size;i++){
        printf(" %d ",randint[i]);
    }
    printf("\n");
}
