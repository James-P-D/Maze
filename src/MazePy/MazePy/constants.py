# UI Component sizes

# Large maze
ROWS = 150
COLS = ROWS
CELL_WIDTH = 5

# Medium maze
#ROWS = 80
#COLS = ROWS
#CELL_WIDTH = 10

# Small maze
#ROWS = 7
#COLS = 7
#CELL_WIDTH = 100

CELL_HEIGHT = CELL_WIDTH
BUTTON_STRIP_HEIGHT = 50
BUTTON_STRIP_TOP = ROWS * CELL_HEIGHT
WINDOW_WIDTH = COLS * CELL_WIDTH
WINDOW_HEIGHT = BUTTON_STRIP_TOP + BUTTON_STRIP_HEIGHT
BUTTON_WIDTH = WINDOW_WIDTH / 4

# RGB Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (125, 125, 125)

# Button Details

BUTTON_BORDER_SIZE = 2
BUTTON_BORDER_COLOR = WHITE
BUTTON_COLOR = BLACK
BUTTON_LABEL_COLOR = WHITE

CLEAR_BUTTON_LABEL = "CLEAR"
CREATE_MAZE_BUTTON_LABEL = "CREATE MAZE"
SOLVE_MAZE_BUTTON_LABEL = "SOLVE MAZE"
QUIT_BUTTON_LABEL = "QUIT"

# CellType

EMPTY = 0
WALL = 1
START = 2  # TODO: Do we need these?
END = 3    # TODO: Do we need these?

START_CELL_COLOR = GREEN
END_CELL_COLOR = RED
EMPTY_CELL_COLOR = WHITE
WALL_CELL_COLOR = BLACK

# PyGame

CLOCK_TICK = 30