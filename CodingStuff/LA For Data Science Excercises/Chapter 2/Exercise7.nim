#[
  Write code to demonstrate that the dot product is commutative.
  Commutative means that a x b = b x a, which, for the vector
  dot product means that aTb = bTa.
]#

import arraymancer
import std/math
import std/random

randomize()

proc vector_dot_product(a: Tensor[int], b: Tensor[int]): float64 =
  var result: float64 = 0.0 
  for i in 0 ..< a.shape[0]:
    result += (a[i] * b[i]).toFloat()
  result

var a: Tensor[int] = @[3, 5, 7].toTensor()
var b: Tensor[int] = @[7, 4, 2].toTensor()

echo "a x b = ", vector_dot_product(a, b)
echo "b x a = ", vector_dot_product(b, a)