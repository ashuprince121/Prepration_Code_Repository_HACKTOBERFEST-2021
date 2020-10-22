import java.util.Scanner;

class OddCounter{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the array size : ");
    int n = sc.nextInt();
    int[] array = new int[n];
    System.out.print("Enter the array elements : ");
    for(int i=0; i<n; i++)
      array[i] = sc.nextInt();
    for(int i: array)
    if(i%2 != 0)
      System.out.print(i + " ");
    sc.close();
  }
}

