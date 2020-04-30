import pygame # Tested with pygame v1.9.6
from UIControls import Button
from constants import *

def create_ui():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    button_width = WINDOW_WIDTH / 4
    clear_button = Button((button_width * 0), BUTTON_STRIP_TOP, button_width, BUTTON_STRIP_HEIGHT, CLEAR_BUTTON_LABEL)
    create_maze_button = Button((button_width * 1), BUTTON_STRIP_TOP, button_width, BUTTON_STRIP_HEIGHT, CREATE_MAZE_BUTTON_LABEL)
    solve_maze_button = Button((button_width * 2), BUTTON_STRIP_TOP, button_width, BUTTON_STRIP_HEIGHT, SOLVE_MAZE_BUTTON_LABEL)
    quit_button = Button((button_width * 3), BUTTON_STRIP_TOP, button_width, BUTTON_STRIP_HEIGHT, QUIT_BUTTON_LABEL)

    clear_button.draw(screen)
    create_maze_button.draw(screen)
    solve_maze_button.draw(screen)
    quit_button.draw(screen)
    
###############################################
# game_loop()
###############################################

def game_loop():
    game_exit = False
    clock = pygame.time.Clock()

    while not game_exit:
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        pygame.quit()
        #        quit()

        #game_display.fill(background)        
        pygame.display.update()
        clock.tick(90)

###############################################
# main()
###############################################

def main():
    pygame.init()
    
    create_ui()

    game_loop()

###############################################
# Startup
###############################################

if __name__ == "__main__":
    #Single line comment
    '''
    Multi-line comment
    Multi-line comment
    Multi-line comment
    '''
    main()
    #pygame.quit()

