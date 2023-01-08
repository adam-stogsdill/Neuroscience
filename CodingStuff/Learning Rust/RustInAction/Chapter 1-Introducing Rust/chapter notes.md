Tags: #Rust #Programming

Cargo run flags!

--release
  Wont print out the error messages that pop out!

-q
  Shorthand for quiet. Reduces the amount of text that will appear in the console
  when running to just be what the program sends through stdout.

## Goal of Rust: Safety

  Rust programs are free from:
    - Dangling pointers -- Live references to data that has become invalid over the course of the program
    - Data races -- The inability to determine how a program will behave from run to run because external factors change
    - Buffer overflow -- An attempt to access the 12th element of an array with only 6 elements
    - Iterator invalidation -- An issue caused by something that is iterated over after being altered midway through

When programs are compiled in debug mode, Rust also
protects against _integer overflow_.

## Goal of Rust: Productivity

When given a choice, Rust prefers the option that is easiest for the developer. Many of its more subtle features are productivity boosts. But programmer productivity is a difficult concept to demonstrate throughout this book (that im taking notes from)!

## Goal of Rust: Control

Rust offers programmers fine-grained control over how data structures are laid out in memory and their access patterns. While Rust uses sensible defaults that align with its “zero cost abstractions” philosophy, those defaults do not suit all situations.

At times, it is imperative to manage your application’s performance. It might matter to you that data is stored in the _stack_ rather than on the _heap_. Perhaps, it might make sense to add _reference counting_ to create a shared reference to a value. Occasionally, it might be useful to create one’s own type of _pointer_ for a particular access patter. The design space is large and Rust provides the tools to allow you to implement your preferred solution.

To understand why Rust is doing something the way it is, it can be helpful to refer back to these three principles:
* The language’s first priority is safety.
* Data within Rust is immutable by default.
* Compile-time checks are strongly preferred. Safety should be a “zero-cost abstraction”

## Rust’s Big features

* Performance
* Concurrency
* Memory Efficiency

## Downsides of Rust

* Cyclic Data Structures
	* Difficult to model cyclic data like an arbitrary graph structure.
* Compile Times
	* Rust is slower at compiling code than its peer languages. The unit of compilation for a Rust program is not an individual file but a whole package (known as a _crate_).
* Strictness
	* It’s impossible/difficult to be lazy when programming with Rust. Programs won’t compile until everything is just right. The compiler is strict, but helpful.
* Size of the language
	* Rust is large! It has a rich type system, several dozen keywords, and includes some features that are unavailable in other languages.

## Where does Rust fit best?

* Command-line utilities
	* Minimal startup-time
	* low memory usage
	* easy deployment
* Data Processing
	* Rust excels at text processing and other forms of data wrangling.
* Extending applications
	* Rust is well suited for extending programs written in a dynamic language.
* Resource-constrained environments
* Server-side applications
* Desktop/Web/Mobile applications
* Systems programming