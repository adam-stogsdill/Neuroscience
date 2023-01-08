fn main() {                             // Rust is flexible where the main function is located
    let a = 10;                         // Types can be inffered by the compiler
    let b:i32 = 20;                     // we can also explicitly declared by the programmer
    let c = 30i32;
    let d = 30_i32;                     // underscores are just for readability when it comes to number and dont affect the value
    let e = add(add(a,b), add(c,d));    //function call!

    println!("(a+b)+(c+d) = {}", e);
}

fn add(i:i32, j:i32) -> i32 {           // this is how we structure the naming of functions
    i+j                                 // the last line (without the ';') will be returned
}
