class Table:
    def __init__(self, rows, cols):
        self.table = []
        for i in range(rows):
            self.table.append([0] * cols)

    def get_value(self, row, col):
        if row >= len(self.table) or col >= len(self.table[0]) or row < 0 or col < 0:
            return None
        return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0])
