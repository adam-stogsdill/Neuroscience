/*
To add the dependency to the package use the toml file.
add the words 'num = "0.4"'
*/
use num::complex::Complex;              // Bring the Complex type into local scope.

fn main() {
    let a = Complex {re: 2.1, im: -1.2};        // Every Rust type has a literal syntax
    let b = Complex::new(11.1, 22.2);           // Most types Implement a new() static method.
    let result = a + b;
    println!("{} + {}i", result.re, result.im); // Access fields with the dot operator
}
