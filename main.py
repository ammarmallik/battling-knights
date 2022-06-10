##############################################################################
# @author: Malik Ammar Akbar                                                 #
# @date: June 01, 2022                                                       #
##############################################################################
import os
import sys
from copy import deepcopy

from item import Item
from block import Block
from knight import Knight
from battlearena import BattleArena

MOVES_FILEPATH = './moves.txt'
OUTPUT_FILEPATH = './final_state.json'
I_MAP = {'A': Item('A', Block(2, 2), 2, 0, 4),
         'D': Item('D', Block(2, 5), 1, 0, 2),
         'M': Item('M', Block(5, 2), 1, 1, 3),
         'H': Item('H', Block(5, 5), 0, 1, 1)}
K_MAP = {'R': Knight('R', Block(0, 0)),
         'Y': Knight('Y', Block(0, 7)),
         'B': Knight('B', Block(7, 0)),
         'G': Knight('G', Block(7, 7))}


def load_moves():
    """
    Load moves from the file.
    @return: List of moves. (list)
    """
    print('Loading moves')
    if not os.path.isfile(MOVES_FILEPATH):
        sys.exit(1)
    moves = []
    with open(MOVES_FILEPATH) as fptr:
        moves.extend(fptr.read().splitlines()[1:-1])
    return moves


def save_final_state(state):
    """
    Write output in JSON file.
    @return: None. (none)
    """
    print('Saving final state of the arena')
    with open(OUTPUT_FILEPATH, 'w') as fptr:
        fptr.write(state)


def driver():
    """
    Driver program for the game.
    @return: None. (none)
    """
    moves = load_moves()
    arena = BattleArena(8, 8, deepcopy(K_MAP), deepcopy(I_MAP))
    arena.setup_arena()
    # Start the battle.
    for move in moves:
        print(f'\nMove: {move}')
        arena.make_a_move(move)
    final_state = arena.generate_final_state()
    save_final_state(final_state)


if __name__ == '__main__':
    driver()
