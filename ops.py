"""Core ops"""

from typing import Union, List
from mat import Mat

# these are all the operations that can be performed on Mat objects, even thought they're separate from the Mat class itself
# it's just because I want to keep things neat and tidy and sexy


def add(mat1: Mat, mat2: Mat) -> Mat: # element-wise addition
	if mat1.rows != mat2.rows or mat1.cols != mat2.cols:
		raise ValueError("Matrices must be of equal dims")
	elif not isinstance(mat1, Mat) or not isinstance(mat2, Mat):
		raise TypeError("Operand must be a Mat obj")
	else:
		newMat = [[mat1.data[i][j] + mat2.data[i][j] for j in range(mat1.cols)] for i in range(mat1.rows)] # Python makes this so easy
		return Mat(mat1.rows, mat1.cols, newMat)

def subtract(mat1: Mat, mat2: Mat) -> Mat: # elem-wise subtraction
	if mat1.rows != mat2.rows or mat1.cols != mat2.cols:
		raise ValueError("Matrices must be of equal dims")
	elif not isinstance(mat1, Mat) or not isinstance(mat2, Mat):
		raise TypeError("Operand must be a Mat obj")
	else:
		newMat = [[mat1.data[i][j] - mat2.data[i][j] for j in range(mat1.cols)] for i in range(mat1.rows)]
		return Mat(mat1.rows, mat1.cols, newMat)

def hadamard(mat1: Mat, mat2: Mat) -> Mat: # element-wise multiplication
	if mat1.rows != mat2.rows or mat1.cols != mat2.cols:
		raise ValueError("Matrices must be of equal dims")
	if not isinstance(mat1, Mat) or not isinstance(mat2, Mat):
		raise TypeError("Operand must be a Mat obj")
	else:
		newMat = [[mat1.data[i][j] * mat2.data[i][j] for j in range(mat1.cols)] for i in range(mat1.rows)]
		return Mat(mat.rows, mat.cols, newMat)

def scalarmul(mat: Mat, scalar: Union[int, float]) -> Mat: # scalar mul
	if not isinstance(mat, Mat) or not isinstance(scalar, (int, float)):
		raise TypeError("Operand must be a Mat obj and a scalar, respectively")
	else:
		newMat = [[mat.data[i][j] * scalar for j in range(mat.cols)] for i in range(mat.rows)]
		return Mat(mat.rows, mat.cols, newMat)

def transpose(mat: Mat) -> Mat: # just flips the rows and cols
	newMat = [[mat.data[j][i] for j in range(mat.rows)] for i in range(mat.cols)]
	return Mat(mat.cols, mat.rows, newMat)

def determinant(mat: Mat) -> Union[int, float]: # computes the determinant of a Mat
	if mat.rows != mat.cols:
		raise ValueError("Mat must square be") # Yoda speak 😂
	elif mat.rows == 2:
		return mat.data[0][0] * mat.data[1][1] - mat.data[0][1] * mat.data[1][0]
	else:
		det = 0
		for i in range(mat.rows):
			det += ((-1)**i) * mat.data[0][i] * mat.minor(0, i).determinant()
		return det

def inverse(mat: Mat) -> Mat: # only works for 2x2 matrices ('cause I'm a lazy bastard)
	if mat.rows != mat.cols:
		raise ValueError("Mat square must be") # YOOOOODA!
	elif mat.rows != 2:
		# ! TODO: implement inverse for matrices of arbitrary size
		raise NotImplementedError # ! I'm too lazy to implement this rn lol 
	else:
		det = mat.determinant()
		if det == 0:
			raise ValueError("Mat not invertible (det = 0). Check your Mat next time, doofus!")
		else:
			inv = 1/det
			newMat = [
				[mat.data[1][1] * inv, -mat.data[0][1] * inv],
				[-mat.data[1][0] * inv, mat.data[0][0] * inv]
			
			]
			return Mat(mat.rows, mat.cols, newMat)

def matmul(mat1: Mat, mat2: Mat) -> Mat: # dot
	if mat1.cols != mat2.rows:
		raise ValueError("Matrices must be of compatible dims")
	elif not isinstance(mat1, Mat) or not isinstance(mat2, Mat):
		raise TypeError("Operand must be a Mat obj")
	else:
		newMat = [[sum([mat1.data[i][k] * mat2.data[k][j] for k in range(mat1.cols)]) for j in range(mat2.cols)] for i in range(mat1.rows)] # holy moly guacamole, that's a lot of Python right there
		return Mat(mat1.rows, mat2.cols, newMat)