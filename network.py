"""Network, a collection of layers."""

from .layer import Layer
from .mat import Mat



class Network:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer: Layer) -> None:
        if not isinstance(layer, Layer):
            raise TypeError("Layer must be a Layer object, duh!")
        else:
            self.layers.append(layer)

    def fwd(self, xs: Mat) -> Mat:
        output = xs
        for layer in self.layers:
            output = layer.fwd(output)
        return output

    def bwd(self):
        raise NotImplementedError() # uhh, ... yeah, I'll get to it ... eventually ...


"""
for epoch in range(epochs):
    z = np.dot(x, w) + b
    ypred = sigmoid(z).flatten()

    loss = J(y, ypred)

    grad = dJ(y, ypred)
    dw = np.dot(x.T, grad) / len(y) # derivative of loss with respect to w
    db = np.mean(grad) # derivative of loss with respect to b

    w -= eta * dw # update w
    b -= eta * db # update b

    if epoch % 1000 == 0:
        print(f"epoch {epoch + 1}: w = {w}, b = {b}, loss = {loss}")

print(f"final loss: {loss}")
"""