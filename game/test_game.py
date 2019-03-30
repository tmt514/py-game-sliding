import unittest
from unittest.mock import patch, MagicMock
from .game import Game
from collections import namedtuple

class TestGameKeyDownMethods(unittest.TestCase):

    @patch('builtins.open')
    @patch('yaml.load')
    def setUp(self, mock_yaml_load, mock_open):
        dummy_ui = MagicMock()
        mock_yaml_load.return_value = {'stages': []}
        mock_open.return_value = ''
        self.game = Game('dummy_stage', dummy_ui)
        self.game.setup_stage()

    def tearDown(self):
        pass

    def test_press_key_up(self):
        KeyPress = namedtuple('KeyPress', ('keysym', 'keycode', 'keychar'))
        KeyPress.__new__.__defaults__ = (None, None, None)
        
        self.game.on_key_down(KeyPress(keysym='Up', keycode=83))
        pass