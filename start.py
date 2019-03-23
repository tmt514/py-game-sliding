import PySimpleGUI as sg
import math

# Very basic window.
layout = [
    [sg.Canvas(size=(640, 480), background_color='gray', key='canvas')],
    [sg.T('This is display area.')]
]

# Game Board
board = """\
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
#..........#...#...#
####################
""".splitlines()

class Ball:
    def __init__(self, position):
        self.position = position
        self.is_moving = False
        self.moving_direction = None
        self.moving_progress = 0
        self.moving_intent = None

    def move_one_step(self, direction):
        self.position = (self.position[0] + direction[0], self.position[1] + direction[1])
        self.moving_progress = 0

board_gui = [[None] * len(board[0]) for x in board]
ball_gui = None
ball = None

window = sg.Window('Canvas test', return_keyboard_events=True).Layout(layout).Finalize()
canvas = window.FindElement('canvas').TKCanvas
for i in range(len(board)):
    for j in range(len(board[0])):
        width = 1
        if board[i][j] == '#':
            fill = 'saddle brown'
        elif board[i][j] == 'E':
            fill = 'gold'
        else:
            fill = None
        bbox = (1+j*32, 1+i*32, 1+j*32+32, 1+i*32+32)
        board_gui[i][j] = canvas.create_rectangle(*bbox, width=width, fill=fill)

        if board[i][j] == 'S':
            bbox = (5+j*32, 5+i*32, 1+j*32+32-4, 1+i*32+32-4)
            ball_gui = canvas.create_oval(*bbox, fill='white')
            ball = Ball((i, j))




KEYS_UP = ["Up:111", "KP_Up:80"]
KEYS_DOWN = ["Down:116", "KP_Down:88"]
KEYS_LEFT = ["Left:113", "KP_Left:83"]
KEYS_RIGHT = ["Right:114", "KP_Right:85"]

MOVE_UP = (-1, 0)
MOVE_DOWN = (1, 0)
MOVE_LEFT = (0, -1)
MOVE_RIGHT = (0, 1)

while True:
    event, value = window.Read(timeout=15)
    
    #canvas.coords(cir, (50 + 100*math.sin(t), 50 + 100*math.cos(t), 100, 100))

    if event is None:
        break
    if event != sg.TIMEOUT_KEY:
        print(event, value)
    if event in KEYS_UP:
        ball.moving_intent = MOVE_UP
    if event in KEYS_DOWN:
        ball.moving_intent = MOVE_DOWN
    if event in KEYS_LEFT:
        ball.moving_intent = MOVE_LEFT
    if event in KEYS_RIGHT:
        ball.moving_intent = MOVE_RIGHT

    # Cancel intent if moving in the same direction.
    if ball.is_moving == True and ball.moving_direction == ball.moving_intent:
        ball.moving_intent = None
    
    # Start moving if it's not moving now.
    if ball.is_moving == False and ball.moving_intent != None:
        def can_move(board, pos, d):
            return board[pos[0] + d[0]][pos[1] + d[1]] != '#'
        if can_move(board, ball.position, ball.moving_intent) == True:
            ball.is_moving = True
            ball.moving_direction = ball.moving_intent
            ball.moving_intent = None


    # Simulate one movement to the ball.
    if ball.is_moving == True:
        ball.moving_progress += 1
        if ball.moving_progress == 4:
            ball.move_one_step(ball.moving_direction)
            if can_move(board, ball.position, ball.moving_direction) == False:
                ball.is_moving = False
                ball.moving_direction = None
    
    if ball.is_moving == True:
        bbox = (5+ball.position[1]*32 + 8*ball.moving_progress*ball.moving_direction[1],
                5+ball.position[0]*32 + 8*ball.moving_progress*ball.moving_direction[0],
                1+ball.position[1]*32+32-4 + 8*ball.moving_progress*ball.moving_direction[1],
                1+ball.position[0]*32+32-4 + 8*ball.moving_progress*ball.moving_direction[0])
    else:
        bbox = (5+ball.position[1]*32,
                5+ball.position[0]*32,
                1+ball.position[1]*32+32-4,
                1+ball.position[0]*32+32-4)
    canvas.coords(ball_gui, *bbox)

    # Check winning condition.
    def check_win(board, ball):
        return board[ball.position[0]][ball.position[1]] == 'E'
            
    if check_win(board, ball) == True:
        sg.Popup('Congrats! You win!')
        break
