class UIController:

    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.update_queue = []

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
        self.window.FindElement('score').Update('Score: {}'.format(info['score']))
        
    def reset_canvas(self):
        self.canvas.delete("all")