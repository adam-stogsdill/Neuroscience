fn main() {
    let fruit = vec!['🥝', '🍌', '🍇'];
  
    let buffer_overflow = fruit[4];    // Rust will cause a crash rather than asign an invalid memory location to a variable
  
    assert_eq!(buffer_overflow, '🍉')  // assert_eq!() tests that arguments are equal.
  }