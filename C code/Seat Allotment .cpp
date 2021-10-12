#include<iostream>
#include<fstream>
#include<conio.h>

using namespace std;


class allotment                              // class Declaration
{                                           //Data Members
	string plan;
	string line;
	int offset;
	string search;
	int choice;

	public:
		void getplan();            //Memeber Functions Declarations
		void getplan1();
		void getplan2();
		void show();
		void show1();
		void show2();
		void show3();
		void core();
		
};
void allotment::core() 
{
	
	int a;
	here:
    cout<<"\n\n\t\t\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\";
	cout<<endl<<"\n\n\t\t\tWELCOME TO LPU's SEAT ALLOTMENT SYSTEM"<<endl;
	cout<<endl<<"\n\n\t\t\tThis Page Is Home"<<endl;
	cout<<"\n\n\t\t\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\";
	cout<<"\n\n\t\t\t1-> FOR EEE PRESS-1"<<endl;
	cout<<"\n\n\t\t\t2-> FOR CSE PRESS-2"<<endl;
	cout<<"\n\n\t\t\t3-> FOR MEC PRESS-3"<<endl;
	cout<<"\n\n\t\t\t4-> FOR TABULAR FORM OF ALL DEPARTMENTS PRESS-4"<<endl;
	cout<<"\n\n\t\t\t5->quit"<<endl;
    cout<<"\n\n\t\t\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\";
	cout<<endl<<"\n\n\t\t\t";
	cin>>a;
	system("cls");

	switch(a)
	{
		case 1:
			{   
			    show(); 
				break;
			}
		case 2:
			{
				
			    show1();
				break;
			}
		case 3:
			{
				show2();
				break;
			}
		case 4:
			{
				show3();
				break;
			}
		
		case 5:
			{
				break;
			}
		default:
			{
				cout<<"\n\n\t\t\tPlease Enter valid choice.......Thank you!........."<<endl;
				cout<<"\n\n\t\t\tPress any key two times to re-enter";
            getch();
            getch();
            system("cls");
            goto here;
			}
	}}





void allotment::getplan()                //Member Function Defination
{
	ifstream myfile;
	myfile.open("File.txt");         //Opening of file
	cout<<"\n\n\t\t\tEnter the REGISTRATION  NUMBER  you want to search :-(EX Registration_Number_11704685)";
	cout<<endl<<"\n\n\t\t\t";
	cin>>search;
	system("cls");

	if(myfile.is_open())
	{
		while(!myfile.eof())
		{
			getline(myfile,line);
			if((offset=line.find(search,0))!=string::npos)    
			{
				myfile>>line;
			    cout<<"\n\t******\tRegistration No\t\t\tName-->Seat No\t\t  ******";
				cout<<"\n\t\t"<<search<<"\t\t\t"<<line;
				cout<<"\n\n\t\t\tPress any key two times to jump to Home page";
            getch();
            getch();
            system("cls");
            core();
				exit(0);
				
			}
			else
			{cout<<"\n\n\t\t\tNo Such Directory Found";
			cout<<endl<<"\n\n\t\t\t";
			cout<<"\n\n\t\t\tPress any key two times to re-enter";
            getch();
            getch();
            system("cls");
        
            
			}show();
		
			
		}
	}
}

void allotment::getplan1()
{
	ifstream myfile;
	myfile.open("File2.txt");
	cout<<"\n\n\t\t\tEnter the REGISTRATION  NUMBER  you want to search :-(EX Registration_Number_11704685)";
	cout<<endl<<"\n\n\t\t\t";
	cin>>search;
	system("cls");

	if(myfile.is_open())
	{
		while(!myfile.eof())
		{
			getline(myfile,line);
			if((offset=line.find(search,0))!=string::npos)    
			{
				myfile>>line;
				cout<<"\n\t******\tRegistration No\t\t\tName-->Seat No\t\t  ******";
				cout<<"\n\t\t"<<search<<"\t\t\t"<<line;
					cout<<"\n\n\t\t\tPress any key two times to jump to Home page";
            getch();
            getch();
            system("cls");
            core();
				exit(0);
				
			}
			else
			{cout<<"\n\n\t\t\tNo Such Directory Found";
			cout<<endl<<"\n\n\t\t\t";
			cout<<"\n\n\t\t\tPress any key two times to re-enter";
            getch();
            getch();
            system("cls");
        
            
			}show1();
		
			
		}
	}
}



void allotment::getplan2()
{
	ifstream myfile;
	myfile.open("File3.txt");
	cout<<"\n\n\t\t\tEnter the REGISTRATION NUMBER  you want to search :-(EX Registration_Number_11704685)";
	cout<<endl<<"\n\n\t\t\t";
	cin>>search;
	system("cls");

	if(myfile.is_open())
	{
		while(!myfile.eof())
		{
			getline(myfile,line);
			if((offset=line.find(search,0))!=string::npos)    
			{
				myfile>>line;
				cout<<"\n\t******\tRegistration No\t\t\tName-->Seat No\t\t  ******";
				cout<<"\n\t\t"<<search<<"\t\t\t"<<line;
					cout<<"\n\n\t\t\tPress any key two times to jump to Home page";
            getch();
            getch();
            system("cls");
            core();
				exit(0);
			}else
			{cout<<"\n\n\t\t\tNo Such Directory Found";
			cout<<endl<<"\n\n\t\t\t";
			cout<<"\n\n\t\t\tPress any key two times to re-enter";
            getch();
            getch();
            system("cls");
            
			}show2();
			
		}
	}
}



void allotment::show()
{   
	cout<<"\n\n\t\t\tEnter 1 for tabular representation else enter 0 for individual data";
	cout<<endl<<"\n\n\t\t\t";
	cin>>choice;
	if(choice==1)
	{
	ifstream f("File.txt");
	if (f.is_open())
	system("cls");
	cout<<f.rdbuf();
		cout<<"\n\n\t\t\tPress any key two times to jump to Home page";
            getch();
            getch();
            system("cls");
            core();
	exit(0);

}   else if(choice==0)
     {cout<<endl;
	 getplan();
	 }
	 else
	 {cout<<"\n\n\t\t\tinvalid input";
	 cout<<"\n\n\t\t\tPress any key two times to re-enter";
            getch();
            getch();
            system("cls");
            show();
	 } 
	}
	
	

void allotment::show1()
{
	cout<<"\n\n\t\t\tEnter 1 for tabular representation else enter 0 for individual data";
	cout<<endl<<"\n\n\t\t\t";
	cin>>choice;
	if(choice==1)
	{
	ifstream f("File2.txt");
	if (f.is_open())
	system("cls");
	cout<<f.rdbuf();
		cout<<"\n\n\t\t\tPress any key two times to jump to Home page";
            getch();
            getch();
            system("cls");
            core();
	exit(0);
}   else if(choice==0)
     {cout<<endl;
	 getplan1();
	 }
	 else
	 {cout<<"\n\n\t\t\tinvalid input";
	 cout<<"\n\n\t\t\tPress any key two times to re-enter";
            getch();
            getch();
            system("cls");
	 }show1();
	}



void allotment::show2()
{
	cout<<"\n\n\t\t\tEnter 1 for tabular representation else enter 0 for individual data";
	cout<<endl<<"\n\n\t\t\t";
	cin>>choice;
	if(choice==1)
	{
	ifstream f("File3.txt");
	if (f.is_open())
	system("cls");
	cout<<f.rdbuf();
		cout<<"\n\n\t\t\tPress any key two times to jump to Home page";
            getch();
            getch();
            system("cls");
            core();
	exit(0);
	exit(0);
}   else if(choice==0)
     {cout<<endl;
	 getplan2();
	 }
	 else
	 {cout<<"\n\n\t\t\tinvalid input";
	 cout<<"\n\n\t\t\tPress any key two times to re-enter";
            getch();
            getch();
            system("cls");
	 }
	 show2();
	 
	}
	
	
	
void allotment::show3()
{	ifstream f("File1.txt");
	if (f.is_open())
	system("cls");
	cout<<f.rdbuf();
	exit(0);
}

                                                                                            

int main()
{
	allotment obj;
        obj.core();
	return 0;
}


