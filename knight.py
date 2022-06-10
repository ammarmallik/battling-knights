##############################################################################
# @author: Malik Ammar Akbar                                                 #
# @date: June 01, 2022                                                       #
##############################################################################
import json


class Knight:
    """
    Knight is the player who fights in the arena.
    """

    def __init__(self, name, block):
        self.name = name
        self.block = block
        self.status = 'LIVE'
        self.item = None
        self.attack = 1
        self.defence = 1

    def got_drowned_or_killed(self, status, block=None):
        """
        Change state of the knight according to rule of getting drowned/dead.
        @param status: DROWNED | DEAD. (string)
        @param block: Block of dead knight. (object)
        @return: None. (none)
        """
        self.status = status
        self.attack = 0
        self.defence = 0
        self.block = block
        self.item = None

    def is_drowned_or_dead(self):
        """
        Check if knight has drowned.
        @return: True if drowned else False. (boolean)
        """
        return self.block is None or self.status == 'DEAD'

    def pick_item(self):
        """
        Pick item from the block.
        @return: None. (none)
        """
        if not self.item:
            self.block.sort_items()
            self.item = self.block.item.pop()
            self.item.equipped = True
            print(f'Knight-{self.name} has picked Item-{self.item.name}')

    def drop_item(self):
        """
        Drop item on the last block.
        @return: None. (none)
        """
        if self.item:
            self.item.block = self.block
            self.item.equipped = False
            self.block.item.append(self.item)
            self.block.sort_items()
            print(f'Knight-{self.name} has dropped Item-{self.item.name}')
            self.item = None

    def move_to_new_block(self, new_block):
        """
        Move knight to new block.
        @param new_block: Block object. (object)
        @return: None. (none)
        """
        self.block = new_block
        new_block.knight = self
        if self.item:
            self.item.block = new_block

    def attack_and_move(self, defender):
        """
        Attack the defender, kill or get killed!
        @param defender: Knight object. (object)
        @return: None. (none)
        """
        # Calculate points for both attacker and defender
        a_points = self.attack + 0.5
        if self.item:
            a_points += self.item.attack
        d_points = defender.defence
        if defender.item:
            d_points += defender.item.defence
        # Let's find out who wins.
        if a_points > d_points:
            # Attacker wins.
            self.move_to_new_block(defender.block)
            defender.drop_item()
            defender.got_drowned_or_killed(status='DEAD',
                                           block=defender.block)
            print(f'Knight-{defender.name} is dead :(')
        else:
            # Defender wins.
            self.move_to_new_block(defender.block)
            self.drop_item()
            self.got_drowned_or_killed(status='DEAD',
                                       block=defender.block)
            print(f'Knight-{self.name} is dead :(')

    def __repr__(self):
        """
        Update the representation method of Knight class.
        @return: Output for the final result. (string)
        """
        output = [json.loads(self.block.__repr__()) if self.block else None,
                  self.status,
                  self.item.name if self.item else None,
                  self.attack,
                  self.defence]
        return json.dumps(output)
