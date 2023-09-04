team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players_1(players: list[dict]) -> None:
    """This function should print all players to the client"""
    for player in players:
        print (player)

# show_players_1(team)

def show_players_2(players: list[dict]) -> None:
    """This function should print all player's names to the client"""
    for player in players:
        print(player["name"])
        
# show_players_2(team)


def show_players_3(players: list[dict]) -> None:
    """This function should print all player's names,ages,numbers to the client"""
    for player in players:
        print(f"Name: {player['name']}, Age: {player['age']}, Number: {player['number']}")
        
# show_players_3(team)


    
    




def add_player( name: str, age: int,num: int) -> None:
    """This function adds the new player."""
    player = {"name": name, "age": age,"number": num}
    team.append(player)
    
# add_player("Sophia",18,14)
# add_player("Sophia",21,15)
# add_player("Sophia",16,17)
# add_player("Sophia",24,21)
# add_player("Sophia",17,5)


    

    
    


def remove_player(players: list[dict], num: int) -> None:
    """This function removes the player by his/her number."""
    remove_player=[]
    for player in players:
            if player["number"] == num:
                remove_player.append(player)
    print(f"\nwill be removed:{remove_player} \n")
    
    for player in remove_player:
        players.remove(player)
        
       
       
                
                
            
# remove_player(team,17)

# print("\nCurrent list:\n")
# show_players_3(team)

def main():
    show_players_3(team)
    print("\nAdded players:\n")

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    
    show_players_3(team) 
    
    remove_player(players=team, num=17)

    show_players_3(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")