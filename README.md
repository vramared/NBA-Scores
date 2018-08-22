# NBA-Scores
This is a simple app which web scrapes from [NBA Box Score Generator](http://www.nbaboxscoregenerator.com/) and reports final game scores on the command line. 
It also calculates the NBA Player of the Day based on points, rebounds, and assists posted. 

Run it by simply typing `python3 nba-results.py` on the command line.

All scores for the day's NBA games will be shown on the command line. 
If a game is not finished yet, the current score will be shown. 

Player of the Day is calculated using this formula:

`playerScore = (.8 * points) + (.3 * rebounds) + (.6 * assists)`

The player with the highest player score will be the Player of the Day. 

* This can be calculated most accurately if all the games for the day are complete. 
