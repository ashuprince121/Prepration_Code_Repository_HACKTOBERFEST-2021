import java.util.Scanner;

class StringPalindrome{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a string : ");
    String a = sc.nextLine();
    if(palindrome(a.toLowerCase()))
      System.out.println(a+" is a palindrome");
    else
      System.out.println(a+" is not a palindrome");
    sc.close();
  }

  public static boolean palindrome(String a){
    int n = a.length();
    for(int i=0; i<n/2; i++)
      if(a.charAt(i) != a.charAt(n-i-1))
        return false;
    return true;
  }
}

