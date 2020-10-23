import java.util.*;

public class OddOrEven {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //Scanner for taking inputs from the keyboard
        System.out.println("Enter a Number: ");
        int num;
        num = sc.nextInt();
        if(num%2==0)
        {
            System.out.println(num+" is Even");
        }
        else if(num%2==1)
        {
            System.out.println(num+" is Odd");
        }
        else
            System.out.println(num+" is zero");
    }
}
