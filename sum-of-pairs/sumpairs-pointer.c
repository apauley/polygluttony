// C solution by Hardy Jonck

#include <stdio.h>
#include <string.h>


int main (int argc, const char * argv[]) {
   int a[] = {1,2,3,4,5};
       char items = sizeof(a)/sizeof(int);
       int b[items];
       int *c=b;
       memcpy(&b,&a,items*sizeof(int));
       while(c < &b[items-1]) { *c = *c + *(c+1);printf("%d\n",*c);c++;}

   return 0;
}
