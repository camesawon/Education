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

    def delete_row(self, row):
        new_table = self.table[:row]
        new_table.extend(self.table[row:])
        self.table = new_table

    def delete_col(self, col):
        for i in range(len(self.table)):
            changed = self.table[i][:col]
            changed.extend(self.table[i][col:])
            self.table[i] = changed

    def add_row(self, row):
        new_table = self.table[:row]
        new_table.append([0] * self.n_cols())
        new_table.extend(self.table[row:])
        self.table = new_table

    def add_col(self, col):
        for i in range(len(self.table)):
            changed = self.table[i][:col]
            changed.append(0)
            changed.extend(self.table[i][col:])
            self.table[i] = changed
