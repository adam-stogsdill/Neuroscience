A probabilistic DL model is a Deep Learning Model who's output returns a vector of values for the output classes with the probability of that class being the actual output.

For example, if I have a model where the purpose is to identify the number values of images from MNIST (which are 0-9), it will return a vector of size n where n is the number of possible classes (10 because of 0-9). In that vector we will have values that are between 0.0 and 1.0 and all those values will total 1.0.

For information on the non-probabilistic deep learning model: [[Non-Probabilistic Deep Learning Model]].

#probabilisticDL 