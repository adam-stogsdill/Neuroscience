#[
  Create a Python Function that will take a vector as input and output a unit
  vector in teh same direction. What happens when you input the zeros vector?

  Ecosystem overview - SciNim Getting Started
  https://scinim.github.io/getting-started/overview/index.html

]#

import arraymancer
import neo
import std/random
import std/math

randomize()
proc create_vector(size: int8): Tensor[float64] =
  var 
    resulting_vector: seq[float64]
  for index in 0 ..< size:
    resulting_vector.add(rand(10.0))
  resulting_vector.toTensor()

proc calculate_norm(vector: Tensor[float64]): float64 =
  var
    resulting_sum: float64 = 0
  for i in 0 ..< vector.shape[0]:
    resulting_sum += math.pow(vector[i].float64, 2.0)
  math.pow(resulting_sum, 0.5)

proc calculate_unit_vector(vector: Tensor[float64]): Tensor[float64] =
  var resulting_vector: Tensor[float64] = vector.deepCopy()
  let norm = calculate_norm(vector)
  for i in 0 ..< resulting_vector.shape[0]:
    resulting_vector[i] /= norm
  resulting_vector

let vect = create_vector(3)
echo "Vector: ", vect

let unit = calculate_unit_vector(vect)
echo "Unit: ", unit

echo "UnitMag: ", calculate_norm(unit)