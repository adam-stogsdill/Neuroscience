#[
  Write an algorithm that computes the norm of a vector by translating 
  (||v|| = sig{i->n}(v_i ** 2)).
  Confirm using random vectors with different dimensionalities and orientations, 
  that you get the same result as np.lingalg.norm().
  This exercise is designed to give you more experience with indexing Numpy arrays
  and translating formulas into code; in practice, its often easier to use
  the numpy function!
]#

#import nimpy
import arraymancer
import std/random
import std/math

randomize()

# Create a vector of given dimensionality or size
proc create_vector(size: int8): Tensor[int] =
  var 
    resulting_vector: seq[int]
  for index in 0 ..< size:
    resulting_vector.add(rand(10))
  resulting_vector.toTensor()

proc calculate_norm(vector: Tensor[int]): float64 =
  var
    resulting_sum: float64 = 0
  for i in 0 ..< vector.shape[0]:
    resulting_sum += math.pow(vector[i].float64, 2.0)
  math.pow(resulting_sum, 0.5)

let rand_vector = create_vector(2)
echo "Vector: ", rand_vector
echo "Norm: ", calculate_norm(rand_vector)

let rand_vector2 = create_vector(2)
echo "Vector: ", rand_vector2
echo "Norm: ", calculate_norm(rand_vector2)
echo ""

let rand_vector3 = create_vector(2)
echo "Vector: ", rand_vector3
echo "Norm: ", calculate_norm(rand_vector3)
echo ""