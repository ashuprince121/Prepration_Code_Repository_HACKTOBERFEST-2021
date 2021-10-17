#include<iostream>
using namespace std;
int main()
{
    int num;
    cin>>num;
    int arr[100000] = {0};          //array to store digits of factorial 

    arr[0] = 1;                     //initializing 0th element as 1 because it is going to store unit digit

    int remainingNum = 0;           //variable to store carry or other/remaining  digit after storing unit digit in array at 0th position after multiplying it with number

    int lengthOfFactorial = 1;

    int number = 2;                 //factorial will start by 2 onwards and from 3,4,5,6......to N 

    int position = 0;               //variable to store position of digits which are to be stored in array

    while(number<=num){

        position = 0;
        remainingNum = 0;
        while(position<lengthOfFactorial)
        {
            arr[position] = arr[position] * number;              //this will work for single digit result 

            arr[position] = arr[position] + remainingNum;        //we have to add the remaining number in result so that are result is perfect

            //to store carry or remaining digit
            remainingNum = arr[position]/10;


            //now to store unit digit from 2digit number 
            arr[position] = arr[position]%10;



            position++;
        }

        //now we have to store remaining num into array too so

        while(remainingNum!=0)
        {
            //storing at last because we are storing one's digit at leftmost position
            //and we have to increase length of result too here as now we are storing 2nd digit   
            arr[lengthOfFactorial] = remainingNum%10;


            //if remaining num will have more digits than we are storing all starting digit of it
            remainingNum = remainingNum/10;                       

            lengthOfFactorial++;
        }
        number++;
    }
    lengthOfFactorial--;

    while(lengthOfFactorial>=0)
    {
        cout<<arr[lengthOfFactorial];
        lengthOfFactorial =  lengthOfFactorial-1;
    }
}
