"""The Mat module"""
###
# funny thing is that this project is my, like, 4th attempt at doing an OOP design schema in Python
# previously, I'd just write functions on the 1st level (col 1) and call it a day
###



class Mat:
    """Matrix class"""
    def __init__(self, rows, cols, data: List = None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [0] * (rows * cols) # init with zeros
        else:
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError("Data must be a list of lists of equal dims")
            else:
                self.data = data

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])