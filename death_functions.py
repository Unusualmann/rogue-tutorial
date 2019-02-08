import libtcodpy as libtcod

from game_messages import Message

from game_states import GameStates

from render_functions import RenderOrder

import config


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    global win
    win = False

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)
    win_message = Message('You defeated the {0}! You Win!'.format(monster.name.capitalize()), libtcod.cyan)
    config.win = False

    if monster.name == 'Lord of Evil':
        config.win = True

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = monster.name + ' corpse'
    monster.render_order = RenderOrder.CORPSE
    if not config.win == True:
        return death_message
    else:
        return win_message