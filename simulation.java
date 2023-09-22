//println(random(0,1));

println("This program simulates a game of raquetball between two");
println("players called 'A' and 'B'. The abilities of each player");
println("is indicated by a probability (a number between 0 and 1) that");
println("the player wins the point when serving. Player A always");
println("has the first serve.\n");

float probA = 0.65;
float probB = 0.6;

int games = 5000;

int winsA = 0;
int winsB = 0;
int scoreA;
int scoreB;

String serving;
for( int i = 0; i < games; i++ ){
  scoreA = 0;
  scoreB = 0;

  serving = "A";
  while( !( scoreA == 15 || scoreB == 15 )){
    if( serving == "A"){
      if( random(0,1) < probA ){
         scoreA++; 
      } else {
         serving = "B";
      }
    } else {
      if( random(0,1) < probB ){
         scoreB++; 
      } else {
         serving = "A"; 
      }
    }
  } // end of while loop
  if( scoreA > scoreB ) winsA++;
  else winsB++;
}

println("Games simulated: " + games );
float percentA = winsA / float(games) * 100;
float percentB = winsB / float(games) * 100;

println("Wins for A: " + winsA + " (" + percentA + "%)");
println("Wins for B: " + winsB + " (" + percentB + "%)");