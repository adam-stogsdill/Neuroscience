#[
  Here's an interesting fact: you can compute the squared norm of a vector
  as the dot product of that vector with itself. Look back at Exercise 2.
  Then comfirm this yourself with code.
]#

import arraymancer
import std/math

proc calculate_norm(vector: Tensor[int]): float64 =
  var
    resulting_sum: float64 = 0
  for i in 0 ..< vector.shape[0]:
    resulting_sum += math.pow(vector[i].float64, 2.0)
  math.pow(resulting_sum, 0.5)

proc vector_dot_product(a: Tensor[int], b: Tensor[int]): float64 =
  var result: float64 = 0.0 
  for i in 0 ..< a.shape[0]:
    result += (a[i] * b[i]).toFloat()
  result

let vec: Tensor[int] = @[5, 5, 5].toTensor()
echo "Squared Norm: ", math.pow(calculate_norm(vec), 2.0)
echo "Dot Product: ", vector_dot_product(vec, vec)