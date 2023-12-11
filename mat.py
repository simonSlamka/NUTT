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

    def __add__(self, other):
        from ops import add
        return add(self, other)

    def __sub__(self, other):
        from ops import subtract
        return subtract(self, other)

    def __mul__(self, other): # element-wise
        from ops import hadamard
        return hadamard(self, other)

    def __matmul__(self, other): # dot
        from ops import matmul
        return matmul(self, other)

    def __rmul__(self, other): # scalar
        from ops import scalarmul
        return scalarmul(self, other)

    def __pow__(self, other): # power
        raise NotImplementedError

    def transpose(self):
        from ops import transpose
        return transpose(self)

    @property # property decorator makes it so that you can call this method without the parentheses (i.e. mat.T)
    def T(self):
        from ops import transpose
        return transpose(self)

    @property
    def shape(self):
        return (self.rows, self.cols)

    @property
    def det(self):
        from ops import determinant
        return determinant(self)

    @property
    def inv(self):
        from ops import inverse
        return inverse(self)