fn main() {
    let mut letters = vec![             // Creates a mutable vector letters
        "a", "b", "c"
    ];

    for letter in letters {
        println!("{}", letter);
        letters.push(letter.clone());   // Copies each letter and appends it to the end fo letters
    }
}
