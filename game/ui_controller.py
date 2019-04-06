from tkinter import *
from os import system
from platform import system as platform

class UIController:

    def __init__(self):
        self.root = Tk()
        self.root.lift()
        self.root.wm_attributes("-topmost", True)
        self.root.after_idle(self.root.call, 'wm', 'attributes', '.', "-topmost", False)
        self.root.after(1, lambda: self.root.focus_force())
        if platform() == 'Darwin':  # How Mac OS X is identified by Python
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


        top_frame = Frame(self.root)
        top_frame.pack()

        stage_name = Label(top_frame, text='第 000 關', font=("Helvetica", 16))
        stage_name.pack(side=LEFT)

        mid_frame = Frame(self.root)
        mid_frame.pack()

        canvas = Canvas(mid_frame, height=480, width=640, bg='gray')
        canvas.pack()

        bottom_frame = Frame(self.root)
        bottom_frame.pack(fill=X)

        info_message = Label(bottom_frame,
            justify=LEFT,
            text='遊戲說明：\n方向鍵按下去以後，會滑到底才可以決定下一個行進方向。\n遊戲目標是要移動到金色區域（出口）。')
        info_message.pack(side=LEFT)

        score = Label(bottom_frame,
            text='Score: 0\nMoves: 0')
        score.pack(side=RIGHT)
        
        self.stage_name = stage_name
        self.canvas = canvas
        self.score = score
        self.update_queue = []


    def mainloop(self):
        self.root.mainloop()


    def use_canvas(self, obj, f):
        """E.g. add Item to canvas."""
        f(obj, self.canvas)

    def add_update(self, obj, f):
        """Update Item."""
        self.update_queue.append([obj, f])

    def update_all(self):
        for obj, f in self.update_queue:
            f(obj, self.canvas)

        self.update_queue = []

    def update_player_info(self, info):
        self.score.config(text='Score: {}\nMoves: {}'.format(
            info.get('score', 0) + info.get('current_stage_score'), info['total_keypress']))

    def update_stage_info(self, level_data):
        self.stage_name.config(text='第 {} 關： {}'.format(
            level_data.get('level', '?'), level_data.get('title', '')))

    def reset_canvas(self):
        self.canvas.delete("all")
