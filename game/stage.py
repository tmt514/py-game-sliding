from .ball import Ball

class Stage:

    def __init__(self, stage_id, ui):
        self.id = stage_id
        self.ui = ui
        self.board = None
        self.board_ui = None

    def load(self):
        """Loads a stage correctly depending on the stage id.
        """
        self.board = """\
####################
#.#................#
#..S.............###
#..................#
#..................#
#..#...............#
##.......#......##.#
##...............#.#
##................##
#...#...........E.##
#...........#......#
##......#..........#
#..........#.......#
#..........#.......#
####################
""".splitlines()

        self.board_ui = [[None] * len(self.board[0]) for x in self.board]
        self.ball = Ball(self, self.ui, self.get_initial_ball_position())
        self.ball_ui = None

        def create_board(self, canvas):
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    width = 1
                    if self.board[i][j] == '#':
                        fill = 'saddle brown'
                    elif self.board[i][j] == 'E':
                        fill = 'gold'
                    else:
                        fill = None
                    bbox = (1+j*32, 1+i*32, 1+j*32+32, 1+i*32+32)
                    self.board_ui[i][j] = canvas.create_rectangle(*bbox, width=width, fill=fill)

        def create_ball(self, canvas):
            i, j = self.ball.position
            bbox = (5+j*32, 5+i*32, 1+j*32+32-4, 1+i*32+32-4)
            self.ball_ui = canvas.create_oval(*bbox, fill='white')
        
        self.ui.use_canvas(self, create_board)
        self.ui.use_canvas(self, create_ball)

    def get_initial_ball_position(self):
        """Obtains initial ball position from the stage board.
        """
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] == 'S':
                    return (x, y)
        return None

    def can_move(self, pos, d):
        return self.board[pos[0] + d[0]][pos[1] + d[1]] != '#'

    def check_win(self):
        return self.board[self.ball.position[0]][self.ball.position[1]] == 'E'

    def move_ball(self):
        # Simulate one movement to the ball.
        if self.ball.is_moving == True:
            self.ball.moving_progress += 1
            if self.ball.moving_progress == 4:
                self.ball.move_one_step(self.ball.moving_direction)
                if self.can_move(self.ball.position, self.ball.moving_direction) == False:
                    self.ball.is_moving = False
                    self.ball.moving_direction = None
        
        if self.ball.is_moving == True:
            bbox = (5+self.ball.position[1]*32
                        +8*self.ball.moving_progress*self.ball.moving_direction[1],
                    5+self.ball.position[0]*32
                        +8*self.ball.moving_progress*self.ball.moving_direction[0],
                    1+self.ball.position[1]*32+32-4
                        +8*self.ball.moving_progress*self.ball.moving_direction[1],
                    1+self.ball.position[0]*32+32-4
                        +8*self.ball.moving_progress*self.ball.moving_direction[0])
        else:
            bbox = (5+self.ball.position[1]*32,
                    5+self.ball.position[0]*32,
                    1+self.ball.position[1]*32+32-4,
                    1+self.ball.position[0]*32+32-4)
        
        def update_ball_coords(self, canvas):
            canvas.coords(self.ball_ui, *bbox)
        self.ui.add_update(self, update_ball_coords)