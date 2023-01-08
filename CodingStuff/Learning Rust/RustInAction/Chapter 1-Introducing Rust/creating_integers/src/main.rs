use std::rc::Rc;
use std::sync::{Arc, Mutex};


fn main() {
    let a = 10;                         // Integer on the stack
    let b = Box::new(20);               // Integer on the heap, also known as a BOXED INTEGER
    let c = Rc::new(Box::new(30));      // Boxed integer wrapped within a reference counter
    let d = Arc::new(Mutex::new(40));   // Integer wrapped in an atomic reference counter and protected by a mutual exclusion lock
}
