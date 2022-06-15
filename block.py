##############################################################################
# @author: Malik Ammar Akbar                                                 #
# @date: June 01, 2022                                                       #
##############################################################################
import json
from operator import attrgetter


class Block:
    """
    Block is a two dimensional position on the arena board where knight/item
    can be placed.
    """

    def __init__(self, x, y, item=None, knight=None):
        self.x = x
        self.y = y
        self.knight = knight
        self.item = []
        if item:
            self.item.append(item)

    def is_available(self):
        """
        Check if the block is available.
        @return: True if available else false. (boolean)
        """
        return self.knight is None and len(self.item) == 0

    def has_knight(self):
        """
        Check if another knight has taken the block.
        @return: True if taken otherwise False. (boolean)
        """
        return self.knight is not None

    def has_item(self):
        """
        Check if item is placed in this block.
        @return: True if it contains the items otherwise false. (boolean)
        """
        return len(self.item) > 0

    def sort_items(self):
        """
        Sort items on the basis of their abilities.
        @return: None. (none)
        """
        self.item.sort(key=attrgetter('order'))

    def __repr__(self):
        return json.dumps([self.x, self.y])
