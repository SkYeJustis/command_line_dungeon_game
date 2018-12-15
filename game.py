import logging
from game_board import GameBoard
from player import Player


def play():
    game_board = GameBoard()
    player = Player()
    
    logging.basicConfig(filename='dd_game.log',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - [FUNCTION]: %(funcName)s - line %(lineno)d",
    level=logging.DEBUG)
    
    monster, door, player.location = game_board.get_locations()
    
    logging.info("GAME_DIMENSIONS: {}".format(str(game_board.GAME_DIMENSIONS)))
    logging.info("LOCATIONS: Monster - {}; Door - {}; Player - {}"\
    .format(monster, door, player.location))

    while True:
        game_board.clear()

        print("WELCOME TO THE DUNGEON!")
        moves = game_board.get_moves(player.location)

        game_board.draw_map(player)

        current_plyr_loc = "\nYou're currently in room {}".\
        format(player.location)
        
        logging.info(current_plyr_loc)
        print(current_plyr_loc)
        
        print("\nYou can move {}".format(', '.join(moves)))
        print("Enter QUIT to quit")

        move = input("> ").upper()
        
        if move in ['QUIT', 'Q']:
            break

        if move not in moves:
            print("\n** Walls are hard! Stop running into them! **\n")
            continue

        player.move_player(move)

        if player.location == door:
            logging.info('Escaped at {}'.format(player.location))
            print("\n** You escaped! **\n")
            break
            
        elif player.location == monster:
            logging.info('Eaten at {}'.format(player.location))
            print("\n** You got eaten! **\n")
            break

if __name__ == '__main__':
    play() 
