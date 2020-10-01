#include<bits/stdc++.h>
using namespace std;

int power(int a,int n)//O(N)
{
    if(n==0)
        return 1;

    return a*power(a,n-1);
}

int fastpower(int a,int n)//O(logN)
{
    if(n==0)
        return 1;

    int smallno=fastpower(a,n/2);
    smallno*=smallno;

    if(n&1)
        return smallno*a;
    else
    {
        return smallno;
    }
    


}

int main()
{
    int n=6;
    cout<<power(2,6)<<endl;
    cout<<fastpower(2,6);

    
    return 0;
}

/*
output
64
64
*/
