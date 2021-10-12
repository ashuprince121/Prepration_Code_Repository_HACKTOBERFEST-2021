#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int isFirstInnings = 0;
int playersPerTeam = 4;
int batsmanrun=0;
int ballsplayed=0;
int totalballsbawled=0;
int bowlsbawled=0;
int runGiven=0;
int wicketlost=0;
int wickettaken=0;
int maxBalls = 6;
int totalPlayers = 11;
char batsman;
char bowler;
char TeamA[4]={'a','b','c','d'};
char TeamB[4]={'e','f','g','h'};
void startFirstInnings(char TeamA[],char TeamB[],int maxballs);
void initialisingPlayers(char TeamA[],char TeamB[],int maxballs);
void startSecondInnings(char TeamB[],char TeamA[],int maxballs );
void letsPlay(char batsman,char bowler,int maxballs);
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
	batsman=TeamA[0];
	bowler=TeamB[0];
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
    
    
    isFirstInnings=0;
    initialisingPlayers(TeamB,TeamA,maxballs);
}

void letsPlay(char batsman,char bowler,int maxballs){
	int i;
	if(maxballs>0){
		for(i=0;i<maxballs;i++){
		
		printf("Let's Play \n");
		printf("\t\t\t\tPress Enter\n");
        while((getchar())!='\n');
		bat(batsman,bowler);
}
}
}

int bat(char batsman,char bowler)
{

printf("\t\t\t\tpress Enter to start the spell\n");
 while((getchar())!='\n');
//batsman status
srand(time(0));
batsmanrun=rand()%7;//batsmanrun per bowl
ballsplayed+=1;

//bowler status 
bowlsbawled+=1;
runGiven+=batsmanrun;
totalballsbawled+=1;

if(batsmanrun==4){
printf("Runs = %d\n",4);
printf("Hurray! Hit the Four");
}
if(batsmanrun==6){
printf("Runs = %d\n",6);
printf("Awsome! That's what the Yes Bank MAXIMUM SIX");
}
if(batsmanrun==1){
printf("Runs = %d\n",1);
printf("Well Played");
}
if(batsmanrun==0){
printf("Runs = %d\n",0);
printf("Hurray! Bowled\n");
printf(" BATSMAN %c SCORED %d\n",batsman,batsmanrun);//displaying individual batsman run
wicketlost+=1;
wickettaken+=1;
batsman=TeamA[wicketlost];
printf("BOWLER NAME %c\n",bowler);
}

if((totalballsbawled==maxBalls)||(wicketlost==4)){
	startSecondInnings(TeamA,TeamB,maxBalls);
}
}




int main()
{
    startFirstInnings(TeamA,TeamB,maxBalls);
    return 0;
}
