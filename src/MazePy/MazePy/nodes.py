class bfs_node():

    __col = -1
    __row = -1
    __parent = None

    def __init__(self, col, row, parent):
        self.__col = col
        self.__row = row
        self.__parent = parent

    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row

    def get_parent(self):
        return self.__parent
