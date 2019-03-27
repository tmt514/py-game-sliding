from .stage import Stage
import PySimpleGUI as sg
import yaml
import os


KEYS_UP = ["w", "Up:111", "KP_Up:80"]
KEYS_DOWN = ["s", "Down:116", "KP_Down:88"]
KEYS_LEFT = ["a", "Left:113", "KP_Left:83"]
KEYS_RIGHT = ["d", "Right:114", "KP_Right:85"]

ALL_MOVE_KEYS = KEYS_UP + KEYS_DOWN + KEYS_LEFT + KEYS_RIGHT

MOVE_UP = (-1, 0)
MOVE_DOWN = (1, 0)
MOVE_LEFT = (0, -1)
MOVE_RIGHT = (0, 1)


class Game:

    def __init__(self, stageset_name, ui):
        self.stageset_name = stageset_name
        self.level = 0
        dir_path = os.path.dirname(__file__)
        stageset_path = os.path.join(
            dir_path, 'stageset', stageset_name + '.yaml')
        self.stageset = yaml.load(open(stageset_path, 'r'))

        self.ui = ui
        self.game_state = 'running'
        self.player_info = {
            'needs_update': False,
            'current_stage_score': 0,
            'score': 0,
            'total_keypress': 0,
        }

    def setup_stage(self):
        level_data = self.stageset['stages'][self.level]
        board = level_data['board'].splitlines()
        self.ui.update_stage_info(level_data)
        self.ui.update_player_info(self.player_info)
        self.stage = Stage(board, self.ui)
        self.stage.load()

    def run_one_iteration(self, event, value):

        if event != sg.TIMEOUT_KEY:
            print(event, value)

        # Updates ball's moving intent.
        if event in KEYS_UP:
            self.stage.ball.update_moving_intent(MOVE_UP)
        elif event in KEYS_DOWN:
            self.stage.ball.update_moving_intent(MOVE_DOWN)
        elif event in KEYS_LEFT:
            self.stage.ball.update_moving_intent(MOVE_LEFT)
        elif event in KEYS_RIGHT:
            self.stage.ball.update_moving_intent(MOVE_RIGHT)
        elif event == 'r':
            self.player_info['current_stage_score'] = 0
            self.player_info['needs_update'] = True
            self.setup_stage()
            return
        elif event == '>':
            self.level = min(self.level + 1, len(self.stageset['stages']) - 1)
            self.setup_stage()
        elif event == '<':
            self.level = max(self.level - 1, len(self.stageset['stages']) - 1)
            self.setup_stage()
        else:
            self.stage.ball.update_moving_intent(None)

        if event in ALL_MOVE_KEYS:
            self.player_info['total_keypress'] += 1
            self.player_info['needs_update'] = True

        # Actually moves the ball, and let the stage handle the event.
        self.stage.move_ball(self.player_info)

        if self.player_info['needs_update'] == True:
            self.player_info['needs_update'] = False
            self.ui.update_player_info(self.player_info)

        if self.stage.check_win() == True:
            self.level += 1
            if self.level < len(self.stageset['stages']):
                self.player_info['score'] += self.player_info['current_stage_score']
                self.player_info['current_stage_score'] = 0
                self.setup_stage()
            else:
                sg.Popup('Congrats! You win!\n按鍵次數：{} 次\n你的得分是：{} 分'.format(
                    self.player_info.get('total_keypress', '?'), self.player_info.get('score', '?')))
                raise Exception('Done!')
