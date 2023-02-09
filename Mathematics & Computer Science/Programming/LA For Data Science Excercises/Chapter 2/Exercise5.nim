#[
  Write a for loop to transpose a row vector
  into a column vector without using a bilt-in
  function or method such as np.transpose()
  or v.T. This exercise will help you create and index
  orientation-endowed vectors.
]#

import arraymancer
import neo
import std/random
import std/math

randomize()
proc create_row_vector(size: int8): Tensor[float] =
  var 
    resulting_vector: seq[float]
  for index in 0 ..< size:
    resulting_vector.add(rand(10.0))
  @[resulting_vector].toTensor()

proc transpose_row_to_col(vector: Tensor[float]): Tensor[float] =
  var
    resulting_vector: Tensor[float] = zeros[float]([vector.shape[1], vector.shape[0]])
  for col in 0 ..< vector.shape[1]:
    resulting_vector[col, 0] = vector[0, col]
  return resulting_vector

let vec = create_row_vector(5)
echo vec
echo transpose_row_to_col(vec)