package com.company;

import java.util.Scanner;

class OverL
{
    //if four numbers are given find maximum
    int max,i,j;
    OverL(int a, int b,int c,int d)
    {
        max = a;
        max = a >= b ? a : b;
        max = b >= c ? b : c;
        max = c >= d ? c : d;
    }

    OverL()
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter two numbers : ");
        i = in.nextInt();
        j = in.nextInt();
        i = i+j;
        j = i-j;
        i = i-j;
    }
}
public class Main
{

    public static void main(String args[])
    {
        int a,b,c,d,n;
        Scanner in = new Scanner(System.in);
        System.out.print("Enter no of elements : ");
        n = in.nextInt();
        if(n==2)
        {
            OverL o1 = new OverL();
            System.out.print("Numbers after swapping are : " + o1.i + " and " + o1.j);
        }
        else if(n==4)
        {
            System.out.print("Enter 4 elements : ");
            a = in.nextInt();
            b = in.nextInt();
            c = in.nextInt();
            d = in.nextInt();
            OverL o1 = new OverL(a,b,c,d);
            System.out.print("Maximum is : " + o1.max);
        }
    }
}
