Tags: #Rust #Programming

## This chapter covers:
* Coming to grips with the Rust syntax
* Learning fundamental types and data structures
* Building command-line utilities
* Compiling programs.

## Compiling a program
To compile a single file written in Rust into a working program:
	1. Save your source code to a file. (ends with .rs)
	2. Make sure that the source code includes a "main()" function.
	3. Open a shell window.
	4. Execute the command "rust {filename}".
	5. To run the file type "./{filename_without_'.rs'}"

## Compiling Rust projects with cargo
Migrating from a single file workflow managed by rustc to one managed by cargo is a two-stage process.
	1. Move that original file into an empty directory. 
	2. Then execute the "cargo init" command.
	3. Then use "cargo run" to run the application.

## Defining Variables and calling Functions
Look more at the code in the "variables_functions" folder to see more info for this section.

Variables are _immutable_ by default, meaning that they are read-only rather than read-write.

The print statement in line 8:
```rust
println!("(a+b)+(c+d)={}", e);
```

This statement is a _macro_, which is function-like but returns code rather than values. When printing to the console, every input data type has its own way of being represented as a text string.

## Numbers

* _Rust includes a large number of numeric types._ You will declare the size in bytes.
* _Conversions between types are always explicit._ Rust does not automatically convert types!
* _Rust number can have methods._ For example, to round 24.5 to the nearest integer, a rust programmer would say. "24.5_f32.round()". The type suffix is required because a concrete type is necessary.

### Integers with base 2, base 8, and base 16 notation

We have numeric literals for base values. Look at "base_notation" folder.
![[rust_types_scalar_chart.png]]

### Comparing Numbers

>[!note] Comparing Collision
>We can't compare different types! Rust will be very angry at us if we do!

In rust though we can cast as such:
```rust
fn main() {
	let a: i32 = 10;
	let b: u16 = 100;
	if a < (b as i32) {
		println!("Ten is less than one hundred.");
	}
}
```

It is safest to case the smaller type to a larger one. (Also known as a promotion!) If we move to a smaller size, we could potentially corrupt the data.

If the conversion could possibly fail we need to use another method!
```rust
use std::convert::TryInto;

fn main() {
	let a: i32 = 10;
	let b: u16 = 100;

	let b_ = b.try_into().unwrap();

	if a < b_ {
		println!("Ten is less than one hundred.")
	}
}
```

The line where we use try_into returns a Result type which when unwrapped returns the final value. If the conversion fails, it crashes the program.

### Rational, Complex numbers, and other numeric types

Rust lacks:
* Many mathematical objects for working with rational numbers and complex numbers
* Arbitrary size integers and arbitrary precision floating-point numbers for working with very large or very small numbers
* fixed-point decimal numbers for working with currencies.

To fix this we use the "num crate" which is a package that introduces the concept to the values.