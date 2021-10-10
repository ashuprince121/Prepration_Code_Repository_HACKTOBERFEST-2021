import java.applet.Applet;
import java.awt.Graphics;

public class input extends Applet{
	public void paint(Graphics g){
		int x=0;
		int y=0;
		String msg="";
		x=Integer.parseInt(getParameter("xvalue"));
		y=Integer.parseInt(getParameter("yvalue"));

		msg=getParameter("msg");
		g.drawString(msg,x,y);
	}
}
	