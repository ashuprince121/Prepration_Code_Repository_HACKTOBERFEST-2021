//Program to find the solution of a Quadratic Equation

import java.util.Scanner;

//Main Class
public class EquationSolver
{
  public static void main(String[] args)
  {
    Scanner in = new Scanner(System.in);

    System.out.println("Quadratic Equation Solver");
    System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^");
    System.out.print("Enter the coefficent of x squared : ");
    double a = in.nextDouble();
    System.out.print("Enter the coefficent of x         : ");
    double b = in.nextDouble();
    System.out.print("Enter the constant                : ");
    double c = in.nextDouble();

    QuadraticEquation e = new QuadraticEquation(a,b,c);
    e.solution();
  }
}

//Class to deal with the Quadratic Equation
public class QuadraticEquation
{
  private double a;
  private double b;
  private double c;
  private double d;
  private double r1;
  private double r2;

  //Constructor to assign values of a,b,c,d
  QuadraticEquation(double a, double b, double c)
  {
    this.a = a;
    this.b = b;
    this.c = c;
    this.d = d = (b*b)-(4*a*c);
    solver();
  }

  //Method to find the solution
  private void solver()
  {
    if(d > 0)
    {
      r1 = ( -b + Math.sqrt(d)) / (2 * a);
      r2 = ( -b - Math.sqrt(d)) / (2 * a);
    }
    else if(d == 0)
    {
      r1 = r2 = -b/(2*a);
    }
    else
    {
      r1 = -b/(2*a);
      r2 = Math.sqrt(-d)/(2*a);
    }
  }

  //Method to display solution on demand
  public void solution()
  {
    if(d > 0)
    {
      System.out.println("\nRoots are Distinct");
      System.out.println("Root 1 : " + r1);
      System.out.println("Root 2 : " + r2);
    }
    else if(d == 0)
    {
      System.out.println("\nRoots are Equal");
      System.out.println("Root 1 : " + r1);
      System.out.println("Root 2 : " + r2);
    }
    else
    {
      System.out.println("\nRoots are Complex");
      System.out.println("Root 1 : " + r1 + " + " + r2 + "i");
      System.out.println("Root 2 : " + r1 + " - " + r2 + "i");
    }
  }
}
