/*
	Author: AnOnYmOus001100
	Date: 08/10/2020

	Description: Program to demonstrate the use of thread using runnable interface
*/


// Implementing Runnable Interface
class MyRunnable implements Runnable
{
// Implementing run method of Runnable
  public void run( )
  {
    for( int i = 1 ; i <= 5 ; i++ )
 System.out.println("message " + i) ;
  }
}

// class ThreadTest
public class ThreadTest
{
  public static void main(String[] args)
  {
	// creating MyRunnable object r
    MyRunnable r = new MyRunnable( ) ;
	// creating a new thread
    Thread t = new Thread(r) ;
    System.out.println(t) ; 
// starting the thread by start method which will
    t.start( ) ;	// calling run method internally
  } 
}
