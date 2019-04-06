from game import Game, UIController
from tkinter import *
import math


ui = UIController()
game = Game("default", ui)
game.setup_stage()

def run_one_iteration():
    global game, ui
    game.run_one_iteration()
    ui.update_all()
    ui.root.after(15, run_one_iteration)

ui.root.after(0, run_one_iteration)
ui.mainloop()
