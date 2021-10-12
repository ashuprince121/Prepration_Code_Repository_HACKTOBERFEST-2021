#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int isFirstInnings = 0;
int netbatsmanrun=0;
int playersPerTeam = 4;
int batsmanrun=0;
int neteamrun=0;
int ballsplayed=0;
int totalballsbawled=0;
int bowlsbawled=0;
int runGiven=0;
int wicketlost=0;
int wickettaken=0;
int maxBalls = 6;
int totalPlayers = 11;
int count=0;
char TeamA[4]={'a','b','c','d'};
char TeamB[4]={'e','f','g','h'};
void startFirstInnings(char TeamA[],char TeamB[],int maxballs);
void initialisingPlayers(char TeamA[],char TeamB[],int maxballs);
void startSecondInnings(char TeamB[],char TeamA[],int maxballs );
int letsPlay(char batsman,char bowler,int maxballs);
int bat(char batsman,char bowler);


void startFirstInnings(char TeamA[],char TeamB[],int maxballs) {
    
    
    printf("|                                                                                               |\n");
    printf("|===================================== FIRST-INNINGS-STARTS ====================================|\n");
    printf("|                                                                                               |\n");
    printf("\t\t\t\tPress Enter\n");
    while((getchar())!='\n');
    
	isFirstInnings=1;
    
    initialisingPlayers(TeamA,TeamB,maxBalls);
}

void initialisingPlayers(char TeamA[],char TeamB[],int maxballs){
	char batsman=TeamA[0];
	char bowler=TeamB[0];
	printf("Ready To bat %c\n",batsman);
	printf("Ready To bowler %c\n",bowler);
	letsPlay(batsman,bowler,maxballs);
    
}

void startSecondInnings(char TeamA[],char TeamB[],int maxballs ) {
    
    
    printf("|                                                                                               |\n");
    printf("|===================================== SECOND-INNINGS-STARTS ===================================|\n");
    printf("|_____|\n");
    printf("\t\t\t\tPress Enter\n");
    while((getchar())!='\n');
    netbatsmanrun=0;
    neteamrun=0;
    ballsplayed=0;
    count++;
    initialisingPlayers(TeamA,TeamB,maxballs);
}

int letsPlay(char batsman,char bowler,int maxballs){
	int teamtotalscore=0,i;
	if(maxballs>0){
		for(i=0;i<maxballs;i++){
		
		printf("\t\t\t\tLet's Play \n");
		printf("\t\t\t\tPress Enter\n");
        while((getchar())!='\n');
        if(count>0)
		{
		batsman=TeamB[wicketlost-1];}
		else
		{
		batsman=TeamA[wicketlost];	
		}
        
		bat(batsman,bowler);
		
		
	}
}
printf("\t\t\t\tTEAM B SCORED %d\n",neteamrun);//displaying individual batsman run
}

int bat(char batsman,char bowler)
{

printf("\t\t\t\tpress Enter to start the spell\n");
 while((getchar())!='\n');
//batsman status
srand(time(NULL));
batsmanrun=rand()%7;//batsmanrun per bowl
netbatsmanrun+=batsmanrun;
neteamrun+=batsmanrun;
ballsplayed+=1;

//bowler status 
bowlsbawled+=1;
runGiven+=batsmanrun;
totalballsbawled+=1;

if(batsmanrun==4){
printf("Runs = 4\n");
printf("Hurray! Hit the Four\n");
}
else if(batsmanrun==6){
printf("Runs = 6\n");
printf("Awsome! That's what the Yes Bank MAXIMUM SIX\n");
}
else if(batsmanrun==1){
printf("Runs = 1\n");
printf("Well Played\n");
}
else if(batsmanrun==0){
printf("Runs = 0\n");
printf("Hurray! Bowled\n");
printf(" BATSMAN %c SCORED %d RUNS\n",batsman,netbatsmanrun);//displaying individual batsman run
printf(" BATSMAN %c PLAYED %d BALLS\n",batsman,ballsplayed);//displaying individual batsman run
netbatsmanrun=0;
ballsplayed=0;
wicketlost+=1;
wickettaken+=1;
batsman=TeamA[wicketlost];
printf("BOWLER NAME %c\n",bowler);
}
else{
printf("Runs = %d\n",batsmanrun);
}

	

if((totalballsbawled==maxBalls)||(wicketlost==4)){
	printf("\t\t\t\tTEAM A SCORED %d\n",neteamrun);//displaying individual batsman run
	startSecondInnings(TeamB,TeamA,maxBalls);
}

}




int main()
{
    startFirstInnings(TeamA,TeamB,maxBalls);
    return 0;
}
