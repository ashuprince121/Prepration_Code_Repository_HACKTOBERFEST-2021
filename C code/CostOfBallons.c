/*
	Author: AnOnYmOus001100
	Date: 07/10/2020

You are conducting a contest at your college. This contest consists of two problems and  participants. You know the problem that a candidate will solve during the contest.

You provide a balloon to a participant after he or she solves a problem. There are only green and purple-colored balloons available in a market. Each problem must have a balloon associated with it as a prize for solving that specific problem. You can distribute balloons to each participant by performing the following operation:

Use green-colored balloons for the first problem and purple-colored balloons for the second problem
Use purple-colored balloons for the first problem and green-colored balloons for the second problem
You are given the cost of each balloon and problems that each participant solve. Your task is to print the minimum price that you have to pay while purchasing balloons.

Input format

First line:  that denotes the number of test cases ()
For each test case: 
First line: Cost of green and purple-colored balloons 
Second line:  that denotes the number of participants ()
Next  lines: Contain the status of users. For example, if the value of the  integer in the  row is , then it depicts that the  participant has not solved the  problem. Similarly, if the value of the  integer in the  row is , then it depicts that the  participant has solved the  problem.
Output format
For each test case, print the minimum cost that you have to pay to purchase balloons.

SAMPLE INPUT 
2
9 6
10
1 1
1 1
0 1
0 0
0 1
0 0
0 1
0 1
1 1
0 0
1 9
10
0 1
0 0
0 0
0 1
1 0
0 1
0 1
0 0
0 1
0 0
SAMPLE OUTPUT 
69
14

*/

#include <stdio.h>

int main(){
	int t,n,cost[2], stat[2], cost1, cost2, min_cost;
	
	// Reading no. of test cases 
	scanf("%d", &t);           

	// reading data for t test cases
	for (int i=1; i <= t; i++){
		cost1 = 0;
		cost2 = 0;
		// reading cost of balloons
		scanf("%d",&cost[0]);
		scanf("%d",&cost[1]);

		// reading number of participants
		scanf("%d",&n);

		// reading status of users
		for(int k=1; k <= n; k++) {
			scanf("%d",&stat[0]);
			scanf("%d",&stat[1]);

			// calculating minimum cost
			cost1 += stat[0]*cost[0] + stat[1]*cost[1];
			cost2 += stat[0]*cost[1] + stat[1]*cost[0];
			
			// checking which cost is minimum
			if (cost1 < cost2)
				min_cost = cost1;
			else
				min_cost = cost2;
		}
		printf("%d\n",min_cost);
	}	
	
}
