use std::thread;                    // Brings multi-threading into local scope

fn main() {
    let mut data = 100;

    thread::spawn(|| {data = 500;});    // thread::spawn() takes a closure as an argument
    thread::spawn(|| {data = 1000;});   // These are attempting to set the value of the data value.
    println!("{}", data);
}
