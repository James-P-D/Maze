###############################################
# UI Component sizes
###############################################

# Huge maze
#ROWS = 300
#COLS = ROWS
#CELL_WIDTH = 3

# Large maze
#ROWS = 150
#COLS = ROWS
#CELL_WIDTH = 6

# Medium maze
#ROWS = 80
#COLS = ROWS
#CELL_WIDTH = 10

# Small maze
ROWS = 40
COLS = ROWS
CELL_WIDTH = 20

# Tiny maze
#ROWS = 7
#COLS = ROWS
#CELL_WIDTH = 100

CELL_HEIGHT = CELL_WIDTH
BUTTON_STRIP_HEIGHT = 50
BUTTON_STRIP_TOP = ROWS * CELL_HEIGHT
WINDOW_WIDTH = COLS * CELL_WIDTH
WINDOW_HEIGHT = BUTTON_STRIP_TOP + BUTTON_STRIP_HEIGHT
TOTAL_BUTTONS = 5
BUTTON_WIDTH = WINDOW_WIDTH / TOTAL_BUTTONS

###############################################
# RGB Colors
###############################################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

###############################################
# Button Details
###############################################

BUTTON_BORDER_SIZE = 2
BUTTON_BORDER_COLOR = WHITE
BUTTON_COLOR = BLACK
BUTTON_LABEL_COLOR = WHITE

# If adding a button, rememeber to update TOTAL_BUTTONS
CLEAR_BUTTON_LABEL = "Clear"
CREATE_BUTTON_LABEL = "Create"
DFS_BUTTON_LABEL = "DFS"
BFS_BUTTON_LABEL = "BFS"
QUIT_BUTTON_LABEL = "Quit"

###############################################
# CellType
###############################################

EMPTY = 0
WALL = 1
INITIAL = 2  # TODO: Do we need these?
TERMINAL = 3    # TODO: Do we need these?
VISITED = 4
PATH = 5

INITIAL_CELL_COLOR = GREEN
TERMINAL_CELL_COLOR = RED
EMPTY_CELL_COLOR = WHITE
WALL_CELL_COLOR = BLACK
PATH_CELL_COLOR = BLUE
VISITED_CELL_COLOR = YELLOW

###############################################
# PyGame
###############################################

CLOCK_TICK = 30
SMALL_SLEEP = 0.01
BIG_SLEEP = 0.5