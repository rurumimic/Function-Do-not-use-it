/**
  gcc -o imperative imperative.c
  clang -o imperative imperative.c

  ./imperative

  x = 5
  x + 2 = 7
  x + 3 = 10
  x + 4 = 14
*/

#include <stdio.h>

int main(int argc, char const *argv[])
{
  int x = 5;
  printf("x = %d\n", x);

  x += 2;
  printf("x + 2 = %d\n", x);
  x += 3;
  printf("x + 3 = %d\n", x);
  x += 4;
  printf("x + 4 = %d\n", x);

  return 0;
}
