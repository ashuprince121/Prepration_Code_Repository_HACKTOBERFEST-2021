  #include<stdio.h>
  #include<math.h>

  int main(void)
  {
    int a,b,flag = 1;
    printf("Armstrong Numbers in a range\n");
    printf("^^^^^^^^^^^^^^^^^^^^^^^^\n");
    printf("Enter the range (eg: 1<space>1000) : ");
    scanf("%d %d", &a, &b);
    for(int i = a; i<= b; i++)
    {
      int sum = 0, length = 0, temp = i;
      //finding the number of digits
      for(length=0; temp != 0; length++, temp /= 10);
      temp = i;
      while(temp!=0)
      {
        sum += pow(temp%10,length);
        temp /= 10;
      }
      if(sum == i)
      {
        if(flag)
        {
          printf("Armstrong Numbers in the given range are \n");
          flag = 0;
        }
        printf("%d ", i);
      }
    }
    if(flag)
      printf("There were no Armstrong Numbers in the given range.\n");
    return 0;
  }
