// CPP program to check if a number is Magic number
#include<iostream>
using namespace std;

bool isMagic(int n)
{
	int sum = 0;

	while (n > 0 || sum > 9)
	{
		if (n == 0)
		{
			n = sum;
			sum = 0;
		}
		sum += n % 10;
		n /= 10;
	}
    return (sum == 1);
}
int main()
{
	int n ;
	cin>>n;
	if (isMagic(n))
		cout << "Magic Number";
	else
		cout << "Not a magic Number";
	return 0;
}

