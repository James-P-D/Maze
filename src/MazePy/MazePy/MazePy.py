import pygame # Tested with pygame v1.9.6
from UIControls import Button
from constants import *
import numpy as np

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
    for c in range(COLS):
        for r in range(ROWS):
            grid[c, r] = EMPTY
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
    for c in range(COLS):
        for r in range(ROWS):
            if(grid[c,r] == START and not start_cell_dragging):
                pygame.draw.rect(screen, START_CELL_COLOR, (c * CELL_WIDTH, r * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)        
            elif (grid[c,r] == END and not end_cell_dragging):
                pygame.draw.rect(screen, END_CELL_COLOR, (c * CELL_WIDTH, r * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)            
            elif (grid[c,r] == WALL):
                pygame.draw.rect(screen, WALL_CELL_COLOR, (c * CELL_WIDTH, r * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)            
            else: #(grid[c,r] == EMPTY):
                pygame.draw.rect(screen, EMPTY_CELL_COLOR, (c * CELL_WIDTH, r * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)            
    
    if(start_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_x = int(mouse_x / CELL_WIDTH)
        cell_y = int(mouse_y / CELL_HEIGHT)                    
        pygame.draw.rect(screen, START_CELL_COLOR, (cell_x * CELL_WIDTH, cell_y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)
    #else:
    #    pygame.draw.rect(screen, START_CELL_COLOR, (start_cell_col * CELL_WIDTH, start_cell_row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)

    if(end_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_x = int(mouse_x / CELL_WIDTH)
        cell_y = int(mouse_y / CELL_HEIGHT)                    
        pygame.draw.rect(screen, END_CELL_COLOR, (cell_x * CELL_WIDTH, cell_y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)
    #else:
    #    pygame.draw.rect(screen, END_CELL_COLOR, (end_cell_col * CELL_WIDTH, end_cell_row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 0)
    

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
                if((cell_x < COLS) and (cell_y < ROWS)):
                    if(grid[cell_x, cell_y] == START):
                        start_cell_dragging = True
                    elif(grid[cell_x, cell_y] == END):
                        end_cell_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if clear_button.is_over(mouse_x, mouse_y):
                    pass
                elif create_maze_button.is_over(mouse_x, mouse_y):
                    pass
                elif solve_maze_button.is_over(mouse_x, mouse_y):
                    pass
                elif quit_button.is_over(mouse_x, mouse_y):
                    game_exit = True
                elif start_cell_dragging:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    cell_x = int(mouse_x / CELL_WIDTH)
                    cell_y = int(mouse_y / CELL_HEIGHT)
                    grid[start_cell_col, start_cell_row] = EMPTY
                    start_cell_col = cell_x
                    start_cell_row = cell_y
                    grid[start_cell_col, start_cell_row] = START
                    start_cell_dragging = False
                elif end_cell_dragging:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    cell_x = int(mouse_x / CELL_WIDTH)
                    cell_y = int(mouse_y / CELL_HEIGHT)
                    grid[end_cell_col, end_cell_row] = EMPTY
                    end_cell_col = cell_x
                    end_cell_row = cell_y
                    grid[end_cell_col, end_cell_row] = END
                    end_cell_dragging = False

        draw_grid()
        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()
    #quit()


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
    

