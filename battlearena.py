##############################################################################
# @author: Malik Ammar Akbar                                                 #
# @date: May 31, 2022                                                        #
##############################################################################
import sys
import json

from block import Block


class BattleArena:
    """
    Arena is a two-dimensional board where knights battle using the items
    placed on fixed positions.
    """

    d_map = {'N': 'North', 'E': 'East', 'W': 'West', 'S': 'South'}

    def __init__(self, x, y, k_map, i_map):
        self.x = x
        self.y = y
        self.board = []
        self.k_map = k_map
        self.i_map = i_map

    def _place_knights(self, **kwargs):
        """
        Place knights on the board.
        @keyword kwargs:
            @key R: Red knight. (object)
            @key G: Green knight. (object)
            @key B: Blue knight. (object)
            @key Y: Yellow knight. (object)
        @return: None. (none)
        """
        self.board[0][0].knight = kwargs['R']
        self.board[0][7].knight = kwargs['Y']
        self.board[7][0].knight = kwargs['B']
        self.board[7][7].knight = kwargs['G']

    def _place_items(self, **kwargs):
        """
        Place items on the board.
        @keyword kwargs:
            @key A: Axe. (object)
            @key H: Helmet. (object)
            @key M: MagicStaff. (object)
            @key D: Dagger. (object)
        @return: None. (none)
        """
        self.board[2][2].item.append(kwargs['A'])
        self.board[2][5].item.append(kwargs['D'])
        self.board[5][2].item.append(kwargs['M'])
        self.board[5][5].item.append(kwargs['H'])

    def setup_arena(self):
        """
        Initialize board with blocks containing knights and items.
        @return: None. (none)
        """
        for i in range(0, self.x):
            row = []
            for j in range(0, self.y):
                row.append(Block(i, j))
            self.board.append(row)
        self._place_knights(**self.k_map)
        self._place_items(**self.i_map)

    def get_new_block(self, curr_block, direction):
        """
        Get new block using the given direction from current block.
        @param curr_block: Knight's current block. (object)
        @param direction: Direction key. (string)
        @return: New block of the knight or None. (object/none)
        """
        if direction not in self.d_map:
            print(f'Invalid direction: "{direction}"')
            sys.exit(1)
        x, y = -1, -1
        if direction == 'N':
            x, y = curr_block.x - 1, curr_block.y
        elif direction == 'S':
            x, y = curr_block.x + 1, curr_block.y
        elif direction == 'E':
            x, y = curr_block.x, curr_block.y + 1
        elif direction == 'W':
            x, y = curr_block.x, curr_block.y - 1
        if x < 0 or x > self.x - 1 or y < 0 or y > self.y - 1:
            return None
        return self.board[x][y]

    def make_a_move(self, move):
        """
        Move the knight to the new position according to the given move.
        @param move: Moving strategy. (string)
        @return: None. (none)
        """
        try:
            k_name, direction = move.split(':')
        except ValueError:
            print(f'Invalid move: "{move}"')
            sys.exit(1)
        if k_name not in self.k_map:
            print(f'Unsupported knight found in the game: "{k_name}"')
            sys.exit(1)
        knight = self.k_map[k_name]
        if knight.is_drowned_or_dead():
            print('Cant play with the drowned/dead knight')
            return None
        print(f'Moving Knight-{k_name} towards {self.d_map[direction]}')
        c_block = self.board[knight.block.x][knight.block.y]
        n_block = self.get_new_block(knight.block, direction)
        c_block.knight = None
        if n_block is None:
            knight.drop_item()
            knight.got_drowned_or_killed(status='DROWNED')
            print(f'Knight-{k_name} has drowned')
            return None
        if n_block.is_available():
            # Block with no knight/item.
            knight.move_to_new_block(n_block)
        elif n_block.has_knight():
            # Let's start the attack.
            print(f'Knight-{knight.name} attacks Knight-{n_block.knight.name}')
            knight.attack_and_move(n_block.knight)
        elif n_block.has_item():
            # Item has been found. Let's pick it.
            knight.move_to_new_block(n_block)
            knight.pick_item()
        return None

    def generate_final_state(self):
        """
        Generate final state of the arena board.
        @return: final state. (string)
        """
        json_state = {'red':         json.loads(self.k_map['R'].__repr__()),
                      'blue':        json.loads(self.k_map['B'].__repr__()),
                      'green':       json.loads(self.k_map['G'].__repr__()),
                      'yellow':      json.loads(self.k_map['Y'].__repr__()),
                      'magic_staff': json.loads(self.i_map['M'].__repr__()),
                      'helmet':      json.loads(self.i_map['H'].__repr__()),
                      'dagger':      json.loads(self.i_map['D'].__repr__()),
                      'axe':         json.loads(self.i_map['A'].__repr__())}
        str_state = '{\n'
        for index, (key, val) in enumerate(json_state.items()):
            str_state += f'  "{key}": {json.dumps(val)}'
            if index < len(json_state) - 1:
                str_state += ',\n'
        str_state += '\n}'
        return str_state
