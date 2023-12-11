"""The Mat module"""

"""
funny thing is that this project is my, like, 4th attempt at doing an OOP design schema in Python
previously, I'd just write functions on the 1st level (col 1) and call it a day
"""

from typing import List, Union, Tuple
import logging

logging.basicConfig(level=logging.INFO)



class Mat:
    """Matrix class"""
    def __init__(self, rows = None, cols = None, data: List[List[Union[float, int]]] = None):
        if rows is None and cols is None and data is None:
            raise ValueError("Need to specify either rows, cols, or data to construct a Mat")
        elif rows is None and cols is None:
            self.rows = len(data)
            self.cols = len(data[0])
        else:
            # fixed an issue here where I was accidentally overwriting the rows and cols attrs with None
            self.rows = rows
            self.cols = cols
        if data is None:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            if not all(len(row) == len(data[0]) for row in data):
                raise ValueError("All rows must be of the same length")
            else:
                self.data = data


    def __str__(self):
        return "\n".join(" ".join(f"{num:4}" for num in row) for row in self.data)

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
        from ops import power
        return power(self, other)

    def __eq__(self, other): # equality
        from ops import equals
        return equals(self, other)

    def __getitem__(self, coords: Tuple): # indexing
        # TODO: validate the __getitem__ method
        return self.data[coords[0]][coords[1]]

    def __setitem__(self, key, value): # setting
        self.data[key] = value # hmm
        # TODO: fix the __setitem__ placeholder

    def __iter__(self): # iteration
        for row in self.data:
            yield row

    def transpose(self):
        from ops import transpose
        return transpose(self)

    @property # property decorator makes it so that you can call this method without the parentheses (i.e. mat.T)
    def T(self): # mat.T (can also do mat.transpose())
        from ops import transpose
        return transpose(self)

    @property
    def shape(self): # mat.shape
        return (self.rows, self.cols)

    @property
    def det(self): # mat.det
        from ops import determinant
        return determinant(self)

    @property
    def inv(self): # mat.inv
        from ops import inverse
        return inverse(self)

    @property
    def bInv(self): # mat.bInv (just a quick and shorter way to check if a Mat is invertible)
        from ops import determinant
        if determinant(self) == 0:
            return False
        else:
            return True