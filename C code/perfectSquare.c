//Program to check whether a given number is a perfect square or not
#include<stdio.h>
#include<math.h>

int square_root(int num)
{
  float sqroot = sqrt((float)num);
  int temp = sqroot;
  if(temp == sqroot)
    return 1;
  else
    return 0;
}


int main(void)
{
  int num;
  printf("Perfect square checker\n");
  printf("^^^^^^^^^^^^^^^^^^^^^^\n");
  printf("Enter the number : ");
  scanf("%d", &num);
  if(square_root(num))
    printf("%d is a Perfect Square.", num);
  else
    printf("%d is not a Perfect Square", num);
  return 0;
}
