###############################################
#
# TODOs
# - Variable renaming (newx eurgh!)
#
#
###############################################

import pygame # Tested with pygame v1.9.6
from UIControls import Button
from constants import *
import numpy as np
import random
import time
import os

###############################################
# Globals
###############################################

initial_cell_row = 0
initial_cell_col = 0
initial_cell_dragging = False

terminal_cell_row = ROWS - 1
terminal_cell_col = COLS - 1
terminal_cell_dragging = False

grid = np.ndarray((COLS, ROWS), np.int8)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clear_button = Button((BUTTON_WIDTH * 0), BUTTON_STRIP_TOP, BUTTON_WIDTH, BUTTON_STRIP_HEIGHT, CLEAR_BUTTON_LABEL)
create_maze_button = Button((BUTTON_WIDTH * 1), BUTTON_STRIP_TOP, BUTTON_WIDTH, BUTTON_STRIP_HEIGHT, CREATE_MAZE_BUTTON_LABEL)
solve_maze_button = Button((BUTTON_WIDTH * 2), BUTTON_STRIP_TOP, BUTTON_WIDTH, BUTTON_STRIP_HEIGHT, SOLVE_MAZE_BUTTON_LABEL)
quit_button = Button((BUTTON_WIDTH * 3), BUTTON_STRIP_TOP, BUTTON_WIDTH, BUTTON_STRIP_HEIGHT, QUIT_BUTTON_LABEL)

###############################################
# initialise()
###############################################

def initialise():
    # Set all cells to EMPTY by default
    for col in range(COLS):
        for row in range(ROWS):
            grid[col, row] = EMPTY            

    # Set the Initial and Terminal cells
    grid[initial_cell_col, initial_cell_row] = INITIAL
    grid[terminal_cell_col, terminal_cell_row] = TERMINAL
    #print(grid)

###############################################
# create_ui()
###############################################

def create_ui():
    screen.fill(BLACK)

    clear_button.draw(screen)
    create_maze_button.draw(screen)
    solve_maze_button.draw(screen)
    quit_button.draw(screen)
    
    draw_grid()

###############################################
# draw_grid()
###############################################

def draw_grid():
    for col in range(COLS):
        for row in range(ROWS):
            # Only set the Initial cell if we are NOT dragging
            if (grid[col, row] == INITIAL and not initial_cell_dragging):
                draw_cell(INITIAL_CELL_COLOR, col * CELL_WIDTH, row * CELL_HEIGHT)        
            # Only set the Terminal cell if we are NOT dragging
            elif (grid[col, row] == TERMINAL and not terminal_cell_dragging):
                draw_cell(TERMINAL_CELL_COLOR, col * CELL_WIDTH, row * CELL_HEIGHT)        
            elif (grid[col, row] == WALL):
                draw_cell(WALL_CELL_COLOR, col * CELL_WIDTH, row * CELL_HEIGHT)        
            else: #(grid[col, row] == EMPTY):
                draw_cell(EMPTY_CELL_COLOR, col * CELL_WIDTH, row * CELL_HEIGHT)        
    
    if (initial_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_x = int(mouse_x / CELL_WIDTH)
        cell_y = int(mouse_y / CELL_HEIGHT)
        # Check the current mouse-pointer for the dragging motion is actually on the board
        if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):
            draw_cell(INITIAL_CELL_COLOR, cell_x * CELL_WIDTH, cell_y * CELL_HEIGHT)
    elif (terminal_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_x = int(mouse_x / CELL_WIDTH)
        cell_y = int(mouse_y / CELL_HEIGHT)                    
        # Check the current mouse-pointer for the dragging motion is actually on the board
        if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):
            draw_cell(TERMINAL_CELL_COLOR, cell_x * CELL_WIDTH, cell_y * CELL_HEIGHT)

###############################################
# game_loop()
###############################################

def game_loop():
    game_exit = False
    clock = pygame.time.Clock()

    global initial_cell_row
    global initial_cell_col
    global initial_cell_dragging
    
    global terminal_cell_row
    global terminal_cell_col
    global terminal_cell_dragging

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True;
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                cell_x = int(mouse_x / CELL_WIDTH)
                cell_y = int(mouse_y / CELL_HEIGHT)
                if ((cell_x < COLS) and (cell_y < ROWS)):
                    if (grid[cell_x, cell_y] == INITIAL):
                        # Set the flag for dragging the Initial cell
                        initial_cell_dragging = True
                    elif (grid[cell_x, cell_y] == TERMINAL):
                        # Set the flag for dragging the Terminal cell
                        terminal_cell_dragging = True
                    elif (not (initial_cell_dragging or terminal_cell_dragging)):
                        # Otherwise, if we have clicked with mouse and we are not dragging anything, toggle
                        # the current cell between EMPTY and WALL
                        if (grid[cell_x, cell_y] == WALL):
                            grid[cell_x, cell_y] = EMPTY
                        elif (grid[cell_x, cell_y] == EMPTY):
                            grid[cell_x, cell_y] = WALL
            elif event.type == pygame.MOUSEBUTTONUP:
                if clear_button.is_over(mouse_x, mouse_y):
                    initialise()
                elif create_maze_button.is_over(mouse_x, mouse_y):
                    create_maze()
                    pass
                elif solve_maze_button.is_over(mouse_x, mouse_y):
                    solve_maze()
                elif quit_button.is_over(mouse_x, mouse_y):
                    game_exit = True
                elif initial_cell_dragging:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    cell_x = int(mouse_x / CELL_WIDTH)
                    cell_y = int(mouse_y / CELL_HEIGHT)
                    # Make sure we have not dragged the Initial cell off the screen
                    if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):
                        # Also make sure we aren't trying to drag Initial cell on top of Terminal cell
                        if (not((cell_x == terminal_cell_col) and (cell_y == terminal_cell_row))):
                            grid[initial_cell_col, initial_cell_row] = EMPTY
                            initial_cell_col = cell_x
                            initial_cell_row = cell_y
                            grid[initial_cell_col, initial_cell_row] = INITIAL
                    # Whatever happens, cancel the dragging flag
                    initial_cell_dragging = False
                elif terminal_cell_dragging:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    cell_x = int(mouse_x / CELL_WIDTH)
                    cell_y = int(mouse_y / CELL_HEIGHT)
                    # Make sure we have not dragged the Terminal cell off the screen
                    if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):                    
                        # Also make sure we aren't trying to drag Terminal cell on top of Initial cell
                        if (not((cell_x == initial_cell_col) and (cell_y == initial_cell_row))):
                            grid[terminal_cell_col, terminal_cell_row] = EMPTY
                            terminal_cell_col = cell_x
                            terminal_cell_row = cell_y
                            grid[terminal_cell_col, terminal_cell_row] = TERMINAL
                    # Whatever happens, cancel the dragging flag
                    terminal_cell_dragging = False

        draw_grid()
        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()
    #quit()


###############################################
# create_maze()
###############################################

def create_maze():

    ###############################################
    ## make_holes()
    ################################################

    def make_holes(new_x1, new_y1, new_x2, new_y2, vertical, horizontal):
        #print(f"\tmake_holes({new_x1}, {new_y1}, {new_x2}, {new_y2}, {vertical}, {horizontal})")        

        all_lists = []

        list = []
        for y in range(new_y1, horizontal):
            #print(f"\tChecking ({vertical}, {y})")
            if (has_horizontal_empty(vertical, y)):
                list.append((vertical, y))
        if (len(list) > 0):
            all_lists.append(list)
        #print("---")
        
        list = []
        for y in range(horizontal + 1, new_y2):
            #print(f"\tChecking ({vertical}, {y})")
            if (has_horizontal_empty(vertical, y)):
                list.append((vertical, y))
        if (len(list) > 0):
            all_lists.append(list)
        #print("---")
        
        list = []
        for x in range(new_x1, vertical):
            #print(f"\tChecking ({x}, {horizontal})")
            if (has_vertical_empty(x, horizontal)):
                list.append((x, horizontal))
        if (len(list) > 0):
            all_lists.append(list)
        
        #print("---")
        
        list = []
        for x in range(vertical + 1, new_x2):
            #print(f"\tChecking ({x}, {horizontal})")
            if (has_vertical_empty(x, horizontal)):
                list.append((x, horizontal))
        if (len(list) > 0):
            all_lists.append(list)

        #print(all_lists)
        if (len(all_lists) == 4):
            item_index_to_remove = random.randint(0, 3)
            del (all_lists[item_index_to_remove])
        #print(all_lists)
        
        for sub_list in all_lists:
            (hole_x, hole_y) = sub_list[random.randint(0, len(sub_list) - 1)]
            draw_cell(EMPTY_CELL_COLOR, hole_x * CELL_WIDTH, hole_y * CELL_HEIGHT)
            grid[hole_x, hole_y] = EMPTY

    ###############################################
    ## divide()
    ################################################

    def divide(x1, y1, x2, y2):
        #print(f"divide({x1}, {y1}, {x2}, {y2})")

        vertical = x2
        if ((x2 - x1) > 2):
            vertical = int(((x2 - x1) / 2) + x1)
            #vertical = random.randint(x1 + 1, x2 - 2)
            for row in range(y1, y2):
                draw_cell(WALL_CELL_COLOR, vertical * CELL_WIDTH, row * CELL_HEIGHT)
                grid[vertical, row] = WALL

        horizontal = y2
        if ((y2 - y1) > 2):                
            horizontal = int(((y2 - y1) / 2) + y1)
            #horizontal = random.randint(y1 + 1, y2 - 2)
            for col in range(x1, x2):
                draw_cell(WALL_CELL_COLOR, col * CELL_WIDTH, horizontal * CELL_HEIGHT)
                grid[col, horizontal] = WALL

        # top-left
        new_x1 = x1
        new_y1 = y1
        new_x2 = vertical
        new_y2 = horizontal
        if (((new_x2 - new_x1) > 2) or ((new_y2 - new_y1) > 2)):
            (new_vertical, new_horizontal) = divide(new_x1, new_y1, new_x2, new_y2)
            make_holes(new_x1, new_y1, new_x2, new_y2, new_vertical, new_horizontal)
                
        # top-right
        new_x1 = vertical + 1
        new_y1 = y1
        new_x2 = x2
        new_y2 = horizontal
        if (((new_x2 - new_x1) > 2) or ((new_y2 - new_y1) > 2)):
            (new_vertical, new_horizontal) = divide(new_x1, new_y1, new_x2, new_y2)
            make_holes(new_x1, new_y1, new_x2, new_y2, new_vertical, new_horizontal)
            
        # bottom-left
        new_x1 = x1
        new_y1 = horizontal + 1
        new_x2 = vertical
        new_y2 = y2
        if (((new_x2 - new_x1) > 2) or ((new_y2 - new_y1) > 2)):
            (new_vertical, new_horizontal) = divide(new_x1, new_y1, new_x2, new_y2)
            make_holes(new_x1, new_y1, new_x2, new_y2, new_vertical, new_horizontal)
            
        # bottom-right
        new_x1 = vertical + 1
        new_y1 = horizontal + 1
        new_x2 = x2
        new_y2 = y2
        if (((new_x2 - new_x1) > 2) or ((new_y2 - new_y1) > 2)):
            (new_vertical, new_horizontal) = divide(new_x1, new_y1, new_x2, new_y2)
            make_holes(new_x1, new_y1, new_x2, new_y2, new_vertical, new_horizontal)
            
        #time.sleep(0.1)
        pygame.display.update()

        return (vertical, horizontal)

    (new_vertical, new_horizontal) = divide(0, 0, COLS, ROWS)
    make_holes(0, 0, COLS, ROWS, new_vertical, new_horizontal)
    grid[initial_cell_col, initial_cell_row] = INITIAL
    grid[terminal_cell_col, terminal_cell_row] = TERMINAL

###############################################
# MISC FUNCTIONS
###############################################

def has_horizontal_neighbours(x, y, cell_types):
    left_x = x - 1
    right_x = x + 1
    if (left_x >= 0) and (right_x < COLS):
        return (grid[left_x, y] in cell_types) and (grid[right_x, y] in cell_types)

    return False

def has_vertical_neighbours(x, y, cell_types):
    above_y = y - 1
    below_y = y + 1
    if (above_y >= 0) and (below_y < ROWS):
        return (grid[x, above_y] in cell_types) and (grid[x, below_y] in cell_types)

    return False

def has_horizontal_empty(x, y):
    return has_horizontal_neighbours(x, y, [EMPTY, INITIAL, TERMINAL])

def has_vertical_empty(x, y):
    return has_vertical_neighbours(x, y, [EMPTY, INITIAL, TERMINAL])

###############################################
# solve_maze()
###############################################

def solve_maze():
    pass

###############################################
# draw_cell()
###############################################

def draw_cell(color, x, y):
    pygame.draw.rect(screen, color, (x, y, CELL_WIDTH, CELL_HEIGHT), 0)        

###############################################
# main()
###############################################

def main():
    pygame.init()
    
    initialise()
    create_ui()

    game_loop()

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()
