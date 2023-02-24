Neurons are the basic units use to make Neural Networks work and are the foundational units of [[Deep Learning]]. Neurons consist of the:

1. The number in which they hold 
2. The activation function ([[Linear]], [[Step Function]], [[Sigmoid]], [[Softmax]], [[Logistic]], [[Tanh]], [[ReLU]])

### Calculating the number 

To calculate the number associated with the neuron, we need to first: calculate the summation of the values of the inputs or previous layers times the weights of our layer (or just in this case the weights associated with the neurons).

In the folowing equation we show how to calculate the value of the neuron, where *x* is the input value of the function, *w* is the weight, *b* is the bias term, and *a* is the activation function which takes in a scaler.

$$y = a([\sum_i w_i(x_i)] + b)$$
If we want to look at a Linear Algebra interpretation of this we can actually perform operations for a whole layer of neurons (we are going to assume a basis neuron where the associated value is 1).

$$Y = a(Wx)$$

*X* is a matrix of shape m * n where the rows corresponds to the neuron of the layer we are calculating values for and the columns are the individual weights for those neurons.

*x* is a column vector corresponding to the outputs of the previous layer.

Lastly, a again is the function that converts all values within the resulting column vector, given by Wx, and transforms it by our activation function.

#deeplearning #dl_component 