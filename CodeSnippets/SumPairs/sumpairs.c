// C solution by Hardy Jonck

#include <stdio.h>

int main (int argc, const char * argv[]) {
   int a[] = {1,2,3,4,5};
       int b[sizeof(a)/sizeof(int)-1];
       char x;
       for (x=0; x<sizeof(a)/sizeof(int)-1; x++) { b[x] = a[x]+ a[x+1];printf("%d,",b[x]);}

   return 0;
}
