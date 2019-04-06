import unittest
from unittest.mock import patch, MagicMock
from .game import Game
from .ball import Ball
from collections import namedtuple

# 自主定義一個 KeyPress 物件
KeyPress = namedtuple('KeyPress', ('keysym', 'keycode', 'keychar'))
KeyPress.__new__.__defaults__ = (None, None, None)

TEST_EMPTY_BOARD = """\
##########
#S.......#
#.......E#
##########
"""

class TestGameKeyDownMethods(unittest.TestCase):

    @patch('builtins.open')
    @patch('yaml.load')
    def setUp(self, mock_yaml_load, mock_open):
        dummy_ui = MagicMock()
        mock_yaml_load.return_value = {'stages': [{
            'board': TEST_EMPTY_BOARD,
        }]}
        mock_open.return_value = ''
        self.game = Game('dummy_stage', dummy_ui)
        self.game.setup_stage()

    def tearDown(self):
        pass

    @patch.object(Ball, 'update_moving_intent')
    def test_pressing_key_up_calls_update_moving_intent(self, mock_update_moving_intent):
        self.game.on_key_down(KeyPress(keysym='Up'))
        mock_update_moving_intent.assert_called()
        pass
        
    def test_pressing_key_left_updates_key_press_count(self):
        self.game.on_key_down(KeyPress(keysym='Left'))
        self.assertEqual(self.game.player_info.get('total_keypress'), 1)
        pass