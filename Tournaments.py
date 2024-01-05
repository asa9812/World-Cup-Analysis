# Simulate a sports tournament. 16 teams in knockout round of 2018 & ratings of each available.
# order of team listings determines which teams will play each other in each round.


import csv # this is all code related to csv.
import sys
import random

# Number of simluations to run
N = 1000

                        #"./2018m.csv"
                        # CSV files can have up to 16,384 columns (in general)
def main():

    if len(sys.argv) != 2: # making sure number of command-line arguments is 2.
        sys.exit("Usage: python tournament.py FILENAME")

    teams = [] 
  
     filename = sys.argv[1]  
with open(filename) as file:  
      reader = csv.DictReader(file) 
      for team in reader: 
          team["rating"] = int(team["rating"]) 
          teams.append(team) 
          # print(teams)

    counts = {} 
for i in range (N): 
    winner = simulate_tournament(teams)
    if winner in counts: # dont forget :
        counts[winner] += 1 # python specific for iterations.
    else:
        counts[winner] = 1 # creates a start
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning") 
 # prepending execution of python code with time.
def simulate_game(team1, team2): # simulates a single game.
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"] 
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600)) 
    return random.random() < probability 


def simulate_round(teams): # simulates the whole round, returning the winners for that round.
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams.
    for i in range(0, len(teams), 2): # start val., stop val., step val.
        if simulate_game(teams[i], teams[i + 1]): 
            winners.append(teams[i])
        else: # else, if false.
            winners.append(teams[i + 1])

    return winners # returns the winners list.


def simulate_tournament(teams): 
    """Simulate a tournament. Return name of winning team."""
 

while len(teams)>1:
    teams = simulate_rounds(teams) 
return teams[0]["team"] 
# print(winners)
#for i in range(0, len(winners),2):
#{ # virtual curly br.
#    simulate_rounds(teams)
#} # virtual curly br.
#return winners



if __name__ == "__main__":
    main()


















