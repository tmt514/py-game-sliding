
class Ball:
    def __init__(self, stage, ui, position):
        self.stage = stage
        self.ui = ui
        self.position = position
        self.is_moving = False
        self.moving_direction = None
        self.moving_progress = 0
        self.moving_intent = None

    def move_one_step(self, direction):
        self.position = (self.position[0] + direction[0], self.position[1] + direction[1])
        self.moving_progress = 0

    def update_moving_intent(self, intent):
        if intent != None:
            self.moving_intent = intent

        # Cancel intent if moving in the same direction.
        if self.is_moving == True and self.moving_direction == self.moving_intent:
            self.moving_intent = None
        
        # Start moving if it's not moving now.
        if self.is_moving == False and self.moving_intent != None:
            if self.stage.can_move(self.position, self.moving_intent) == True:
                self.is_moving = True
                self.moving_direction = self.moving_intent
                self.moving_intent = None
