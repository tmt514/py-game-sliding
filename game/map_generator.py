import random


class Generator:
    
    def set_border(self):
        for i in range(15):
            self.board[i][0] = '#'
            self.board[i][19] = '#'
        for j in range(20):
            self.board[0][j] = '#'
            self.board[14][j] = '#'
    
    def generate(self):
        """ Randomly generate 20 x 15 list of strings (game map).
        """
        self.board = [[random.choice(['.', '#']) for _ in range(20)] for _ in range(15)]
        self.set_border()
        
        x = random.randint(1, 13)
        y = random.randint(1, 18)
        self.board[x][y] = 'S'
        
        return self.board
        
class TuGGenerator(Generator):
    
    def generate(self):
        self.board = [['?' for _ in range(20)] for _ in range(15)]
        self.set_border()
        x = random.randint(1, 13)
        y = random.randint(1, 18)
        self.board[x][y] = 'S'
        
        steps = random.randint(10, 15)
        direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        for _ in range(steps):
            
            random_turn = random.choice([False, True])
            if random_turn:
                direction = (-direction[1], direction[0])
            else:
                direction = (direction[1], direction[0])
                    
            distance = random.randint(5, 10)
            
            def can_move(pos, dir):
                return self.board[pos[0] + dir[0]][pos[1] + dir[1]] != '#'
            def check_and_set(x, y, c):
                if self.board[x][y] == '?':
                    self.board[x][y] = c
            
            for _ in range(distance):
                if can_move((x, y), direction):
                    x += direction[0]
                    y += direction[1]
                    check_and_set(x, y, '.')
            
            if can_move((x, y), direction) == False:
                continue
            while can_move((x, y), direction) and self.board[x+direction[0]][y+direction[1]] != '?':
                x += direction[0]
                y += direction[1]
            
            if self.board[x+direction[0]][y+direction[1]] == '?':
                check_and_set(x+direction[0], y+direction[1], '#')
        
        if self.board[x][y] != 'S':
            self.board[x][y] = 'E'
        for i in range(15):
            for j in range(20):
                if self.board[i][j] == '?':
                    check_and_set(i, j, random.choice(['.', '#', '$', 't']))
        return self.board            
            
generator = TuGGenerator()