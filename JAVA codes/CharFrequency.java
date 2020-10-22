import java.util.Scanner;

class CharFrequency{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the String    : ");
    String a = sc.nextLine();
    System.out.print("Enter the character : ");
    char b = sc.next().charAt(0);
    int count = counter(a,b);
    System.out.println("Frequency = " + count);
    sc.close();
  }

  public static int counter(String a, char b){
    int n = a.length();
    int count = 0;
    for(int i=0; i<n; i++)
    if(a.charAt(i) == b)
      count++;
      //EITHER IF PART or CONDITIONAL OPERATOR PART, NOT BOTH
      //count += (a.charAt(i) == b) ? 1:0;
    return count;
  }
}

