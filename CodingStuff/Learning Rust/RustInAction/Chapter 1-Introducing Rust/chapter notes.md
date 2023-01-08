Cargo run flags!

--release
  Wont print out the error messages that pop out!

-q
  Shorthand for quiet. Reduces the amount of text that will appear in the console
  when running to just be what the program sends through stdout.

Goal of Rust: Safety

  Rust programs are free from:
    - Dangling pointers -- Live references to data that has become
        invalid over the course of the program
    - Data races -- The inability to determine how a program
        will behave from run to run because external factors change
    - Buffer overflow -- An attempt to access the 12th element of an
        array with only 6 elements
    - Iterator invalidation -- An issue caused by something that is
        iterated over after being altered midway through

When programs are compiled in debug mode, Rust also
protects against _integer overflow_.