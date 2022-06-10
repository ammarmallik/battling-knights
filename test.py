##############################################################################
# @author: Malik Ammar Akbar                                                 #
# @date: June 02, 2022                                                       #
##############################################################################
from copy import deepcopy
from unittest import TestCase, main

from battlearena import BattleArena
from main import K_MAP, I_MAP, save_final_state


class TestBattlingKnights(TestCase):
    """
    This class provides test cases for different use-cases of the game.
    """

    def setUp(self):
        self.arena = BattleArena(8, 8,
                                 k_map=deepcopy(K_MAP),
                                 i_map=deepcopy(I_MAP))
        self.arena.setup_arena()

    def test1_pick_item(self):
        """Pick M on block 5:2 using Knight-B."""
        print('Test1 started')
        self.arena.make_a_move('G:N')
        self.arena.make_a_move('G:N')
        self.arena.make_a_move('G:W')
        self.arena.make_a_move('G:W')
        self.assertEqual(self.arena.k_map['G'].item, self.arena.i_map['H'])
        self.assertNotEqual(self.arena.k_map['G'].item, self.arena.i_map['M'])
        print('Test1 ended\n')

    def test2_drown_a_knight(self):
        """Drown Knight-Y by moving towards North"""
        print('Test2 started')
        self.arena.make_a_move('Y:N')
        self.assertEqual(self.arena.k_map['Y'].status, 'DROWNED')
        self.assertEqual(self.arena.k_map['Y'].block, None)
        # Check if we can play using this knight, watch the print statement
        self.arena.make_a_move('Y:S')
        print('Test2 ended\n')

    def test3_kill_a_knight(self):
        """Kill Knight-B by Knight-R"""
        print('Test3 started')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.assertEqual(self.arena.k_map['B'].status, 'DEAD')
        self.assertEqual(self.arena.k_map['B'].block.x, 7)
        self.assertEqual(self.arena.k_map['B'].block.y, 0)
        print('Test3 ended\n')

    def test4_defend_a_knight_using_item(self):
        """Defend Knight-G using Item-H against Knight-R"""
        print('Test4 started')
        self.arena.make_a_move('G:N')
        self.arena.make_a_move('G:N')
        self.arena.make_a_move('G:W')
        self.arena.make_a_move('G:W')
        self.arena.make_a_move('R:E')
        self.arena.make_a_move('R:E')
        self.arena.make_a_move('R:E')
        self.arena.make_a_move('R:E')
        self.arena.make_a_move('R:E')
        self.arena.make_a_move('R:E')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:S')
        self.arena.make_a_move('R:W')
        self.assertEqual(self.arena.k_map['R'].status, 'DEAD')
        state = self.arena.generate_final_state()
        save_final_state(state)
        print('Test4 ended')


if __name__ == '__main__':
    main(verbosity=1)
