class UIController:

    def __init__(self, canvas):
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