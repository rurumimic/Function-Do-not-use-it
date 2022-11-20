// gcc -S -O0 count.c
// gcc -o count count.c

#include <stdio.h>

void count_with_goto(int array[], int size)
{
  int i = 0;

LOOP:
  printf("%d", array[i]);
  i++;
  if (i < size)
    goto LOOP;
}

void count_with_for(int array[], int size)
{
  for (int i = 0; i < size; i++)
  {
    printf("%d", array[i]);
  }
}

int main(int argc, char const *argv[])
{
  int array[3] = {1, 2, 3};
  count_with_goto(array, 3);
  count_with_for(array, 3);

  return 0;
}
