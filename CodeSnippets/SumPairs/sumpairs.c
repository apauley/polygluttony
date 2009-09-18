// C solution by Hardy Jonck

#include <stdio.h>

int main (int argc, const char * argv[]) {
   int a[] = {1,2,3,4,5};
       char x;
       for (x=0; x<sizeof(a)/sizeof(int)-1; x++) { a[x] += a[x+1];printf("%d,",a[x]);}
   return 0;
}
