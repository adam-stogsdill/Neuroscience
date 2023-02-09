#[derive(Debug)] // Allows the println macro to print the Cereal enum

enum Cereal {               // An enum is a type iwht a fixed number of legal variants.
    Barley, Millet, Rice,
    Rye, Spelt, Wheat
}

fn main() {
    let mut grains: Vec<Cereal> = vec![];       // Initializes an empty vector of Cereal
    grains.push(Cereal::Rye);                   // Adds one item to the grains vector
    drop(grains);                               // Deletes grains and its contents
    println!("{:?}", grains);                   // Attempts to access the deleted value
}
