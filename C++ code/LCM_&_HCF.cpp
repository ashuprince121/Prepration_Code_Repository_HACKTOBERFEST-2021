#include<iostream>
using namespace std;

int gcd(int a,int b){
    return b==0 ? a : gcd(b,a%b);
}
int main()
 {
	//code
	int t,a,b,hcf,lcm;
	cin>>t;
	while(t--){
	    cin>>a>>b;
	    hcf=gcd(a,b);
	    
	    lcm=(a*b)/hcf;
	    cout<<lcm<<" "<<hcf<<endl;
	}
	return 0;
}