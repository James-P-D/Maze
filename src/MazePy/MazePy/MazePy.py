import pygame # Tested with pygame v1.9.6
from UIControls import Button
from constants import *
import numpy as np
import random
import time

###############################################
# Globals
###############################################

start_cell_row = 0
start_cell_col = 0
start_cell_dragging = False

end_cell_row = ROWS - 1
end_cell_col = COLS - 1
end_cell_dragging = False

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
    # Set the Start and End cells
    grid[start_cell_col, start_cell_row] = START
    grid[end_cell_col, end_cell_row] = END
    print(grid)

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
            # Only set the Start cell if we are NOT dragging
            if (grid[col, row] == START and not start_cell_dragging):
                pygame.draw.rect(screen, START_CELL_COLOR, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)        
            # Only set the End cell if we are NOT dragging
            elif (grid[col, row] == END and not end_cell_dragging):
                pygame.draw.rect(screen, END_CELL_COLOR, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)            
            elif (grid[col, row] == WALL):
                pygame.draw.rect(screen, WALL_CELL_COLOR, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)            
            else: #(grid[col, row] == EMPTY):
                pygame.draw.rect(screen, EMPTY_CELL_COLOR, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)            
    
    if (start_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_x = int(mouse_x / CELL_WIDTH)
        cell_y = int(mouse_y / CELL_HEIGHT)
        # Check the current mouse-pointer for the dragging motion is actually on the board
        if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):
            pygame.draw.rect(screen, START_CELL_COLOR, (cell_x * CELL_WIDTH, cell_y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)
    elif (end_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_x = int(mouse_x / CELL_WIDTH)
        cell_y = int(mouse_y / CELL_HEIGHT)                    
        # Check the current mouse-pointer for the dragging motion is actually on the board
        if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):
            pygame.draw.rect(screen, END_CELL_COLOR, (cell_x * CELL_WIDTH, cell_y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)

###############################################
# game_loop()
###############################################

def game_loop():
    game_exit = False
    clock = pygame.time.Clock()

    global start_cell_row
    global start_cell_col
    global start_cell_dragging
    
    global end_cell_row
    global end_cell_col
    global end_cell_dragging

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True;
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                cell_x = int(mouse_x / CELL_WIDTH)
                cell_y = int(mouse_y / CELL_HEIGHT)
                if ((cell_x < COLS) and (cell_y < ROWS)):
                    if (grid[cell_x, cell_y] == START):
                        # Set the flag for dragging the Start cell
                        start_cell_dragging = True
                    elif (grid[cell_x, cell_y] == END):
                        # Set the flag for dragging the End cell
                        end_cell_dragging = True
                    elif (not (start_cell_dragging or end_cell_dragging)):
                        # Otherwise, if we have clicked with mouse and we are not dragging anything, toggle
                        # the current cell between EMPTY and WALL
                        if (grid[cell_x, cell_y] == WALL):
                            grid[cell_x, cell_y] = EMPTY
                        elif (grid[cell_x, cell_y] == EMPTY):
                            grid[cell_x, cell_y] = WALL
            elif event.type == pygame.MOUSEBUTTONUP:
                if clear_button.is_over(mouse_x, mouse_y):
                    pass
                elif create_maze_button.is_over(mouse_x, mouse_y):
                    create_maze()
                    pass
                elif solve_maze_button.is_over(mouse_x, mouse_y):
                    pass
                elif quit_button.is_over(mouse_x, mouse_y):
                    game_exit = True
                elif start_cell_dragging:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    cell_x = int(mouse_x / CELL_WIDTH)
                    cell_y = int(mouse_y / CELL_HEIGHT)
                    # Make sure we have not dragged the Start cell off the screen
                    if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):
                        # Also make sure we aren't trying to drag Start cell on top of End cell
                        if (not((cell_x == end_cell_col) and (cell_y == end_cell_row))):
                            grid[start_cell_col, start_cell_row] = EMPTY
                            start_cell_col = cell_x
                            start_cell_row = cell_y
                            grid[start_cell_col, start_cell_row] = START
                    # Whatever happens, cancel the dragging flag
                    start_cell_dragging = False
                elif end_cell_dragging:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    cell_x = int(mouse_x / CELL_WIDTH)
                    cell_y = int(mouse_y / CELL_HEIGHT)
                    # Make sure we have not dragged the End cell off the screen
                    if ((cell_x >= 0) and (cell_x < COLS) and (cell_y >= 0) and (cell_y < ROWS)):                    
                        # Also make sure we aren't trying to drag End cell on top of Start cell
                        if (not((cell_x == start_cell_col) and (cell_y == start_cell_row))):
                            grid[end_cell_col, end_cell_row] = EMPTY
                            end_cell_col = cell_x
                            end_cell_row = cell_y
                            grid[end_cell_col, end_cell_row] = END
                    # Whatever happens, cancel the dragging flag
                    end_cell_dragging = False

        draw_grid()
        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()
    #quit()

def create_maze():

    def divide(x1, y1, x2, y2):
        print(f"divide({x1}, {y1}, {x2}, {y2})")
        vertical = x1
        if ((x2 - x1) > 3):
            vertical = int(((x2 - x1) / 2) + x1) # random.randint(x1 + 1, x2 - 1)
            for row in range(y1, y2):
                pygame.draw.rect(screen, WALL_CELL_COLOR, (vertical * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)
                grid[vertical, row] = WALL

        horizontal = y1
        if ((y2 - y1) > 3):                
            horizontal = int(((y2 - y1) / 2) + y1) # random.randint(y1 + 1, y2 - 1)
            for col in range(x1, x2):
                pygame.draw.rect(screen, WALL_CELL_COLOR, (col * CELL_WIDTH, horizontal * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)
                grid[col, horizontal] = WALL

        # top-left
        new_x1 = x1 + 1
        new_y1 = y1 + 1
        new_x2 = vertical - 1
        new_y2 = horizontal - 1
        if (((new_x2 - new_x1) > 3) and ((new_y2 - new_y1) > 3)):
            divide(new_x1, new_y1, new_x2, new_y2)
        
        # top-right
        new_x1 = vertical + 1
        new_y1 = y1 + 1
        new_x2 = x2 - 1
        new_y2 = horizontal - 1
        if (((new_x2 - new_x1) > 3) and ((new_y2 - new_y1) > 3)):
            divide(new_x1, new_y1, new_x2, new_y2)
        
        # bottom-left
        new_x1 = x1 + 1
        new_y1 = horizontal + 1
        new_x2 = vertical - 1
        new_y2 = y2 - 1
        if (((new_x2 - new_x1) > 3) and ((new_y2 - new_y1) > 3)):
            divide(new_x1, new_y1, new_x2, new_y2)
        
        # bottom-right
        new_x1 = vertical + 1
        new_y1 = horizontal + 1
        new_x2 = x2 - 1
        new_y2 = y2 - 1
        if (((new_x2 - new_x1) > 3) and ((new_y2 - new_y1) > 3)):
            divide(new_x1, new_y1, new_x2, new_y2)

        time.sleep(0.01)
        pygame.display.update()


    divide(0, 0, COLS, ROWS)


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
