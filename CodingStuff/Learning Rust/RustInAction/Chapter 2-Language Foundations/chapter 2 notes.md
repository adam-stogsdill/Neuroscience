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

The project in "num_testing" has the code we will be talking about.

* The "use" keyword pulls crates into local scope, and the namespace operator restricts what's imported.
* _Rust does not have constructors; instead, every type has a literal form_.

>[!note] Shortcut for adding a third-party dependency to a project
> Use the command "cargo install cargo-edit". This will allow you to add packages in the console. To add a package use "cargo add {package}"

## Flow Control

### For: The central pillar of iteration

The basic form of the for loop when iterating through a sequence is:
```rust
for item in container {
	// ...
}
```

This basic form makes each successive element in **container** available as **item**. This way does have some pitfalls.
Once the block ends, accessing the container another time becomes invalid. Even though the container variables remains within local scope, its _lifetime_ has ended.

If you add an '&'-prefix to "container", it will keep the _container_.

If you need to change anything about the _item_ during the loop, you can use a _mutable reference by including the mut keyboard._
```rust
for item in &mut collection {
	// ...
}
```

### Anonymous Loops
When a local variable is not used within a block, by convention, you'll use an underscore. For example:
```rust
for _ in 0..10 {
	// ...
}
```

### Avoid managing an index variable
Using a manual index variable is largely discouraged because of two problems:
* Performance - Indexing values with the collection[index] syntax incurs runtime costs for _bounds checking_.
* Safety - Periodically accessing collection over time introduces the possibility that it changed.

## Loop: The basis for Rust's looping constructs
Rust contains a **Loop** keyword for providing more control than **for** and **while** loops.
It continues to loop until the **break** keyword is called or the program is terminated.
Loop is useful for long-running functionality (i.e. servers).

### Break from nested loops
To break outside a larger loop you can add a _loop label_. Look at the example below to see how to accomplish this.
```rust
'outer: for x in 0.. {
	for y in 0.. {
		for z in 0.. {
			if x + y + z > 1000 {
				break 'outer;
			}
		}
	}
}
```

## Match: Type-aware pattern matching
While it's possible to use if/else blocks in Rust, match provides a safer alternative. **Match** warns you if you haven't considered a relevant alternative. It is also elegant and concise:
```rust
match item {
	0 => {},
	10 ..=20 => {}, // ..= means an inclusive range
	40 | 80 => {},
	_ = > {},       // the underscore acts as the default case.
}
```

## Defining Functions

![[function_def_syntax.png]]

## Using References
A _reference_ is a value that stands in place for another value. For example, imagine that variable _a_ is a large array that is costly to duplicate. In some sense, a reference _r_ is a cheap copy of _a_. But instead of creating a duplicate, the program stores a's address in memory. When the data from _a_ is required, _r_ can be _dereferenced_ to make _a_ available. The following code shows how to perform this:
```rust
fn main() {
	let a = 42;
	let r = &a;                 // get the mem address of a assigned to r
	let b = a + *r;             // dereference the r variable to access the a value

	println!("a + a = {}", b);
}
```

## Final Project, Rendering the Mandelbrot set!
Look at the Mandelbrot folder!