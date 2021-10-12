import java.util.Arrays;
import java.util.Scanner;

public class KthSmallestElement {
	public static int kthSmallest(int a[], int k) {
		Arrays.sort(a);
		return a[k - 1];
	}
	public static void main(String[] args) {
		int n;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Array Size : ");
		n = sc.nextInt();
		int a[] = new int[n];
		System.out.println("Enter "+n+" element of the array : ");
		for (int i = 0; i < n; i++)
			a[i] = sc.nextInt();
		int k;
		System.out.println("Enter k , k Should be smaller than "+n);
		k = sc.nextInt();
		if (k < n)
			System.out.println(k+"th smallest element is " + kthSmallest(a, k));
		else
			System.out.println("k is greater than "+n);
	}
}
