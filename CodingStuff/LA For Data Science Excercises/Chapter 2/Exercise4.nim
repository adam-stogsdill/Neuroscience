#[
  You know how to create unit vectors; what if you want
  to create a vector of any arbitrary magnitude?
  Write a function that will take a vector and a desired
  magnitude as inputs and will return a vector
  in the same direction but with a magnitude corresponding
  to the second input.
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

proc calculate_vector_value_sum(vector: Tensor[float64]): float64 =
  var result: float64 = 0
  for i in 0 ..< vector.shape[0]:
    result += pow(vector[i], 2.0)
  result

proc calculate_mag(vector: Tensor[float64]): float64 =
  var
    resulting_sum: float64 = 0
  for i in 0 ..< vector.shape[0]:
    resulting_sum += math.pow(vector[i].float64, 2.0)
  math.pow(resulting_sum, 0.5)

proc vec_with_mag(vector: Tensor[float64], mag: float64): Tensor[float64] =
  var gamma:float64 = pow(pow(mag, 2.0) / (calculate_vector_value_sum(vector)), 0.5)
  var resulting_vector: Tensor[float64] = vector.deepCopy()
  gamma * resulting_vector

let vect = @[5.0, 5.0, 5.0].toTensor()
echo "Vector: ", vect
let desired_mag = 5.0
let new_vect = vec_with_mag(vect, desired_mag)
echo "New Vector: ", new_vect
echo "New Mag: ", calculate_mag(new_vect)