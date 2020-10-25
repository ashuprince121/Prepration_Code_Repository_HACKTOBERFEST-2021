import java.util.Scanner;

class maths{
	int x,y;
	int add(){
		return (x+y);
	}
}

class inputscanner{
   public static void main(String args[]){
	   maths m=new maths();
	   Scanner s=new Scanner(System.in);
	   System.out.println("Enter the fisrt number :");
	   m.x=s.nextInt();
	   System.out.print("Enter the second number :");
	   m.y=s.nextInt();
	   System.out.print("sum of "+m.x+" and "+m.y+" is "+m.add());

    }
}
