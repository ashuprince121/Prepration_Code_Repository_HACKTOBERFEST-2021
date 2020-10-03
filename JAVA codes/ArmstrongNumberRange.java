//Program to print Armstrong Numbers in a given range
import java.util.Scanner;

public class ArmstrongNumberRange
{
  public static void main(String[] args)
  {
    Scanner in = new Scanner(System.in);
    System.out.println("Armstrong Numbers in a Range");
    System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^");
    System.out.print("Enter the lower limit : ");
    int a = in.nextInt();
    System.out.print("Enter the upper limit : ");
    int b = in.nextInt();
    boolean flag = true;
    for(int i = a; i<= b; i++)
    {
      int sum = 0, length = 0, temp = i;
      //finding the number of digits
      for(length=0; temp != 0; length++, temp /= 10);
      temp = i;
      while(temp!=0)
      {
        sum += Math.pow(temp%10,length);
        temp /= 10;
      }
      if(sum == i)
      {
        if(flag)
        {
          System.out.println("Armstrong Numbers in the given range are ");
          flag = false;
        }
        System.out.print(i + " ");
      }
    }
    if(flag)
      System.out.println("There were no Armstrong Numbers in the given range.");
  }
}
