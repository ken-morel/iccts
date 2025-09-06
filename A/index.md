# Problem A: Neural network components

Identifying neural network components.

## `W(1)21`: The weight of a node

This represents the weight of the connection between two neurons. It's a decimal value which ideates to the strength of the connection between the two neurons. It is also one of the important values that are adjusted when the model is trained.

## `Σ`: Weighted sum

This represents the `weighted sum`, it is simply the sum of the outputs from the previous layer after each have been scaled by their connection weight, it will later be added a bias which will give the model's final output after being passed to the activation function.

## `f`: An activation function

This function takes the previous [Weighted sum] and transforms it before we get the finals neuron output, it makes the output non-linear with curves like that of the `sigmoid` activation function, and even more complex patterns. The `sigmoid` for example transforms any real decimal to a decimal between 0 and 1, and used form probability output.

## `Red circle`: Input Neuron

This represents a neuron in the [Input layer], which receives a single `feature` from the initial data provided to the model to the next layer.

## `Orange circle`: Bias term

This represents a [Bias term]. This value is applied to the on every neuron after the weighted sum and before the activation function, literaly permiting to move the output higher or lower in the activation function, and tuning again better the model's output. This is usualy a single decimal which is added to the weighted sum.

## `Green circle`: An Output Neuron

It is a neuron in the [Output layer], which does the final model output.

## `Box A`: Hidden Layer

A hidden layer is a layer of neurons between input and output layers which usually hides more complex features from the input data, making the output even more complex. The numbe rof hidden layers represent the `depth` of a neural network.

## `Box B`: Output Layer

This is the final layer of neurons in the network, which produces the model's output or prediction.

## `ŷ`: Predicted Output

This symbol represents the final value predicted by the network, produced by the output layer.

