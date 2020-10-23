class point{
	int x;
	int y;
	void setpoint(int a,int b){
		x=a;
		y=b;
	}
}

class parameter{
	public static void main (String args[]){
		point p = new point();
		p.setpoint(100,200);
		System.out.println("x = "+p.x);
		System.out.println("y = "+p.y);
	}
}