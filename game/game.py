from .stage import Stage
import PySimpleGUI as sg 


KEYS_UP = ["Up:111", "KP_Up:80"]
KEYS_DOWN = ["Down:116", "KP_Down:88"]
KEYS_LEFT = ["Left:113", "KP_Left:83"]
KEYS_RIGHT = ["Right:114", "KP_Right:85"]

MOVE_UP = (-1, 0)
MOVE_DOWN = (1, 0)
MOVE_LEFT = (0, -1)
MOVE_RIGHT = (0, 1)


class Game:

    def __init__(self, stage_id, ui):
        self.stage = Stage(stage_id, ui)
        self.ui = ui
        self.game_state = 'running'
        self.player_info = {
            'needs_update': False,
            'score': 0
        }

    def setup_stage(self):
        self.stage.load()
        self.ball = self.stage.ball

    def run_one_iteration(self, event, value):

        if event != sg.TIMEOUT_KEY:
            print(event, value)

        # Updates ball's moving intent.
        if event in KEYS_UP:
            self.ball.update_moving_intent(MOVE_UP)
        elif event in KEYS_DOWN:
            self.ball.update_moving_intent(MOVE_DOWN)
        elif event in KEYS_LEFT:
            self.ball.update_moving_intent(MOVE_LEFT)
        elif event in KEYS_RIGHT:
            self.ball.update_moving_intent(MOVE_RIGHT)
        else:
            self.ball.update_moving_intent(None)

        # Actually moves the ball, and let the stage handle the event.
        self.stage.move_ball(self.player_info)

        if self.player_info['needs_update'] == True:
            self.player_info['needs_update'] = False
            self.ui.update_player_info(self.player_info)

        if self.stage.check_win() == True:
            sg.Popup('Congrats! You win!')
            raise Exception('Done!')