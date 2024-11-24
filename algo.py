import json 


##algo for who has the belt?
## algo for who won and whos the next opponent for the next team

##input = schedule, previous winner of the nba championship
##output = nba belt (winner)

##schedule ( key value pair or dictionary)

def beltWinner(schedule, prevWinner):
    ##1. need to create a variable for currentWinner
    ##2. based on the schedule, we need to go through each team to determine if the prevWinner beat the opposing team.
    ##3. if they beat the team, the currentWinner remains the same, go to the next game
    ##4. if currentWinner loses, switch currentWinner with the other team and then check shedule for the  game id.
    ##5. if next game id is null then return winner

    currentTitleTeam = prevWinner
    currentTeamNextGameId = schedule[currentTitleTeam]['Games'][0]['nextGameId']
    currentTeamGameId = schedule[currentTitleTeam]['Games'][0]['GameId']

    while currentTeamNextGameId != None:
        break

    print(schedule)

with open('./data.json', 'r') as data:
    print(data)
    comp = json.load(data)
beltWinner(comp, "Celtics")
