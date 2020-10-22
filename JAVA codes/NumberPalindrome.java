import java.util.Scanner;

class NumberPallindrome
{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a number(int) : ");
    int a = sc.nextInt();
    int temp = a, sum = 0;
    while(a!=0)
    {
      sum = sum*10+a%10;
      a /= 10;
    }

    if(sum == temp)
      System.out.printf("%d is a palindrome\n", temp);
    else
      System.out.printf("%d is not a palindrome\n", temp);
    sc.close();
  }
}

