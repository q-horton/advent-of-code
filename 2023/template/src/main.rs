pub mod read_input;

use crate::read_input::*;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    for line in input_data {
        println!("{}", line.as_str());
    }
}
