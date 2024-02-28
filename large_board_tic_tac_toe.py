"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 4
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1]/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
        self.game_reset()

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)
        # Draw the grid
        
        for row in range(self.GRID_SIZE):
         for col in range(self.GRID_SIZE):
            # Get the x and y coordinates of the current grid location
            x = col * (self.WIDTH + self.MARGIN) + self.MARGIN
            y = row * (self.HEIGHT + self.MARGIN) + self.MARGIN
            # Draw the rectangle for the current grid location
            pygame.draw.rect(self.screen, self.WHITE, (x, y, self.WIDTH, self.HEIGHT))
        
        pygame.display.update()

    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        # Get the x and y coordinates of the center of the circle
        cx = x + self.WIDTH/2
        cy = y + self.HEIGHT/2
    # Draw the circle
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (cx, cy), self.WIDTH//2)
        

    def draw_cross(self, x, y):
        cx1 = x + self.WIDTH/4
        cy1 = y + self.HEIGHT/4
        cx2 = x + self.WIDTH*3/4
        cy2 = y + self.HEIGHT/4
    # Draw the cross
        pygame.draw.line(self.screen, self.CROSS_COLOR, (cx1, cy1), (cx2, cy2))
        pygame.draw.line(self.screen, self.CROSS_COLOR, (cx1, cy1), (cx2, cy2))

    def is_game_over(self):

        # Check if the game is over
        terminal = self.game_state.is_terminal()

         # If the game is over, return True
        if terminal:
         
         return True

         # Otherwise, return False
         return False
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self):
        if self.algorithm_select == "Minimax":
         best_move = minimax(self.game_state, self.player_O)

        elif self.algorithm_select == "Negamax":
         best_move = negamax(self.game_state, self.player_O)

    # Draw the nought (or circle, depending on the symbol chosen for the AI player) at the best move returned by the algorithm
        self.draw_cross(*best_move)
        
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        self.game_state.get_scores(terminal)


    def game_reset(self):
        self.draw_game()
        
        self.game_state = GameStatus(self.GRID_SIZE, turn_O=True)
        
        pygame.display.update()

    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()


        while not done:
            for event in pygame.event.get():  # User did something
                

             if event.type == pygame.QUIT:
                    done = True
             elif event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    pos = pygame.mouse.get_pos()
                    # Get the row and column of the current grid location
                    row = pos[1] // (self.WIDTH + self.MARGIN)
                    col = pos[0] // (self.HEIGHT + self.MARGIN)
                    # Check if the current grid location is empty
                    if self.game_state.board[row][col] == 0:
                        self.move((row, col))
                        self.draw_cross(*pos)
                        self.change_turn()
                        pygame.display.update()
                        terminal = self.game_state.is_terminal()
                        self.game_state.get_scores(terminal)
                        self.play_ai()
                        self.draw_cross(*pos)
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe()

tictactoegame.play_game()
