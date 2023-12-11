"""Core ops"""

from typing import Union, List
from mat import Mat


def add(self, other: "Mat") -> "Mat": # the quotes in the type hint are there because we're referencing the class before it's defined (in itself)
    if self.rows != other.rows or self.cols != other.cols:
        raise ValueError("Matrices must be of equal dims")
    elif not isinstance(other, Mat):
        raise TypeError("Operand must be a Mat obj")
    else:
        newMat = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)] # Python makes this so easy
        return Mat(self.rows, self.cols, newMat)

def subtract(self, other: "Mat") -> "Mat":
    if self.rows != other.rows or self.cols != other.cols:
        raise ValueError("Matrices must be of equal dims")
    elif not isinstance(other, Mat):
        raise TypeError("Operand must be a Mat obj")
    else:
        newMat = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Mat(self.rows, self.cols, newMat)

def hadamard(self, scalar: Union[int, float]): # element-wise multiplication
    if not isinstance(scalar, (int, float)):
        raise TypeError("Operand must be a number")
    else:
        newMat = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Mat(self.rows, self.cols, newMat)

def transpose(self):
    newMat = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
    return Mat(self.cols, self.rows, newMat)

def inverse(self):
    raise NotImplementedError

def matmul(self, other): # dot
    raise NotImplementedError