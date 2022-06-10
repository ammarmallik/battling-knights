##############################################################################
# @author: Malik Ammar Akbar                                                 #
# @date: June 01, 2022                                                       #
##############################################################################
import json


class Item:
    """
    Item is a special weapon to enhance the abilities of the knight for
    attack/defence.
    """

    def __init__(self, name, block, attack, defence, order):
        self.name = name
        self.block = block
        self.equipped = False
        self.attack = attack
        self.defence = defence
        self.order = order

    def __repr__(self):
        """
        Update the representation method for item class.
        @return: Item object for the final output.
        """
        return json.dumps([[self.block.x, self.block.y], self.equipped])
