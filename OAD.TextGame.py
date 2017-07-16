from debug import dbg
import traceback

from gameserver import Game
from thing import Thing
from room import Room  
from console import Console

## 
## "game" is a special global variable, an object of class Game that holds
## the actual game state. 
## 
game = Game()
nulspace = Room('nulspace')         #"nulspace" is a room for objects that should be deleted. TODO: Automaticly delete items from nulspace every 10 heartbeats.
nulspace.game = game
nulspace.set_description('void', 'This is an empty void where dead and destroyed things go. Good luck getting out!')
nulspace.add_names('void')
nulspace.add_exit('north', 'nulspace')
nulspace.add_exit('south', 'nulspace')
nulspace.add_exit('east', 'nulspace')
nulspace.add_exit('west', 'nulspace')
game.events.schedule(game.time+5, game.clear_nulspace)
game.nulspace = nulspace

try:
    import domains.wizardry.galsbilly

    import domains.school

    import home.owen.house
except:
    dbg.debug(traceback.format_exc())
    try:
        import domains.school
    except:
        game.user.cons.write('The game is broken, sorry! Error below:')
        game.user.cons.write(traceback.format_exc())
        dbg.debug(traceback.format_exc())
        cons.write('\nDue to the problem with the above error, the game is closing.')
        try:
            game.user.move_to(nulspace)
        except:
            dbg.debug(traceback.format_exc())
            cons.write('NOTHING IS WORKING. THE GAME IS BROKEN. PLEASE COME AGAIN LATER AFTER THIS ISSUE IS RESOLVED.')

Thing.ID_dict['great hall'].insert(game.user)
Thing.ID_dict['scroll'].move_to(game.user)
game.register_heartbeat(Thing.ID_dict['scroll'])
game.user.set_start_loc = Thing.ID_dict['great hall']
game.user.cons.write("\nWelcome to Firlefile Sorcery School!\n\n"
"Type 'look' to examine your surroundings or an object, "
"'inventory' to see what you are carrying, " 
"'quit' to end the game, and 'help' for more information.")
game.loop()

