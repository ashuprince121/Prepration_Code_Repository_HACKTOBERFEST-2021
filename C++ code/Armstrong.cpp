#include<iostream>
using namespace std;
int main()
 {
	//code
	int t,n,m,sum=0,r;
	cin>>t;
	while(t--){
	    cin>>n;
	    int m=n;
	    while(m>0){
	        
	    r=m%10;
	    sum=sum+(r*r*r);
	    m=m/10;
	    }
	    if(sum==n){
	        cout<<"Yes"<<endl;
	        
	    }else
	    cout<<"No"<<endl;
	}
	return 0;
}