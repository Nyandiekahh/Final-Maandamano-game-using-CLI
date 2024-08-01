from game.nairobi_police_game import NairobiPoliceGame
from network.multiplayer import MultiplayerManager

if __name__ == "__main__":
    game = NairobiPoliceGame()
    print("Do you want to play multiplayer? (y/n)")
    choice = game.get_player_input("Enter your choice: ").lower()
    if choice == 'y':
        multiplayer = MultiplayerManager(game)
        player_name = game.get_player_input("Enter your name: ")
        print("Do you want to (1) host or (2) join a game?")
        host_or_join = game.get_player_input("Enter your choice (1/2): ")
        if host_or_join == '1':
            multiplayer.host_game()
        else:
            multiplayer.join_game()
    else:
        game.start_game()
