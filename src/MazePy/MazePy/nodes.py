class dfs_node():

    __left_visited = False
    __above_visited = False
    __right_visited = False
    __below_visited = False
    __col = -1
    __row = -1

    def __init__(self, col, row):
        __col = col
        __row = row

    def has_unvisited_neighbours():
        return __left_visited and __above_visted and __right_visited and __below_visited

