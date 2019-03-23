from game import Game, UIController
import PySimpleGUI as sg
import math

# Very basic window.
layout = [
    [sg.Canvas(size=(640, 480), background_color='gray', key='canvas')],
    [sg.T('遊戲說明：\n方向鍵按下去以後，會滑到底才可以決定下一個行進方向。\n遊戲目標是要移動到金色區域（出口）。'),
        sg.T('Score: 0', key='score')]
]

window = sg.Window('Canvas test', return_keyboard_events=True).Layout(layout).Finalize()
canvas = window.FindElement('canvas').TKCanvas

ui = UIController(window, canvas)
game = Game("defualt", ui)
game.setup_stage()

while True:
    event, value = window.Read(timeout=15)

    if event is None:
        break

    try:
        game.run_one_iteration(event, value)
        ui.update_all()
    except Exception as e:
        if str(e) == "Done!":
            break
        else:
            raise e


    
