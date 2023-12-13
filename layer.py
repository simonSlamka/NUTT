"""Layer, a collection of neurons."""

from .mat import Mat
from .neuron import Neuron



class Layer:
    def __init__(self, inputSize: int, neuronCount: int, bias: float = 0.0) -> None:
        if not all(isinstance(neuron, Neuron) for neuron in neurons):
            raise TypeError("Neurons must be a list of Neuron objects")
        else:
            self.neurons = [Neuron(weights=Mat(inputSize, 1), bias=bias) for _ in range(neuronCount)]
            self.count = neuronCount

    def fwd(self, xs: Mat) -> Mat:
        outputs = []
        for neuron in self.neurons:
            neuron.activate(xs)
            outputs.append(neuron.output)
        return Mat(self.count, 1, [outputs])

    def bwd(self):
        raise NotImplementedError() # laziness wins again ...