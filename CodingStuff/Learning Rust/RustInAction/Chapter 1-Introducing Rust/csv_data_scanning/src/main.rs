fn main() {                 // Executable functios require a main function
    let penguin_data = "\
    common name,length (cm)
    Little penguin,33
    Yellow-eyed penguin,65
    Fiordland penguin,60
    Invalid,data
    ";
  
    let records = penguin_data.lines();
  
    for (i, record) in records.enumerate() {
      if i == 0 || record.trim().len() == 0 {  // Skips header row and lines with only whitespace
        continue;
      }
  
      let fields: Vec<_> = record     // Starts with a line of text. Vec is shorthand for vector and the underscore is to ask rust to infer the input type.
        .split(',')                   // splits records into fields
        .map(|field| field.trim())    // trims whitespace of each field
        .collect();                   // builds a collection of fields
  
      if cfg!(debug_assertions) {              // cfg! checks configuration at compile time
        eprintln!("debug: {:?} -> {:?}",
                   record, fields);            // eprintln! prints to standard error (stderr)
      }
  
      let name = fields[0];           // 
      if let Ok(length) = fields[1].parse::<f32>() { // Attempts to parse field as a floating-point number
          println!("{}, {}cm", name, length);        // println! prints to standard out (stdout)
      }
    }
  }