"""Neuron, the basic unit of a neural network."""

from .mat import Mat
from .randomizer import Randomizer



class Neuron:
    def __init__(self, nInputs: int, bias: float) -> None:
        self.weights = self.init_weights(nInputs)
        self.bias = bias
        self.output = None
        self.error = None
        self.activation = None
        self.rand = Randomizer()

    def init_weights(self, nInputs: int) -> Mat:
        w = [[self.rand.random() for _ in range(nInputs)]]
        return Mat(nInputs, 1, w)

    def sigmoid(self, x: Mat) -> Mat:
        return 1 / (1 + (-x).exp())

    def activate(self, x: Mat) -> Mat:
        if x.shape[0] != self.weights.shape[0] or x.shape[1] != 1:
            raise ValueError("Inputs must be a col vect of the same dims as the weights")
        wSum = self.weights @ x
        wSum += self.bias

        self.output = self.sigmoid(wSum)

    def calc_err(self, target: float) -> None:
        self.error = 0.5 * ((target - self.output) ** 2) # MSE

    def J(self, y: float, ypred: float): # cross entropy
        if ypred == 0 or ypred == 1:
            ypred = max(min(ypred, 1 - 1e-15), 1e-15)

        return - (y * ypred.log() + (1 - y) * (1 - ypred).log())