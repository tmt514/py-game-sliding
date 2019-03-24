
class Item:
    def __init__(self, position, stage, ui_controller):
        self.position = position
        self.stage = stage
        self.ui_controller = ui_controller

    def pass_through(self, player_info):
        pass
        
class Trap(Item):
    def __init__(self, position, stage, ui_controller):
        self.position = position
        self.stage = stage
        self.ui_controller = ui_controller
        
        def add_trap(self, canvas):
            bbox = (1+32*self.position[1]+8, 1+32*self.position[0]+8,
                    1+32*self.position[1]+16, 1+32*self.position[0]+16)
            self.ui = canvas.create_rectangle(bbox, fill='black')

        ui_controller.use_canvas(self, add_trap)
        
    def pass_through(self, player_info):
        player_info['score'] -= 1
        player_info['needs_update'] = True
        return False

class Coin(Item):
    def __init__(self, position, stage, ui_controller):
        self.position = position
        self.stage = stage
        self.ui_controller = ui_controller

        def add_coin(self, canvas):
            pos = (1+32*self.position[1]+16, 1+32*self.position[0]+16)
            self.ui = canvas.create_text(*pos, text='$', font=('Times', 24, 'bold'), fill='orange')

        ui_controller.use_canvas(self, add_coin)

    def pass_through(self, player_info):
        """ Returns true if this object needs destroy. """
        player_info['score'] += 5
        player_info['needs_update'] = True

        def destroy_ui(self, canvas):
            canvas.delete(self.ui)

        self.ui_controller.add_update(self, destroy_ui)
        return True