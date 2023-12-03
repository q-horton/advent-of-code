// This is standard code used each day to read in the input file.
//
// The code borrows from that that I wrote for ratlab

// Library imports
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;
use std::path::Path;

/* Reads in the file with the specified path.
 */
pub fn read_input(file_path: &str) -> Vec<String> {
    file_to_vec(open_file(file_path))
}

/* Opens up the file given by the path and returns the File struct.
 */
fn open_file(file_path: &str) -> File {
    let path = Path::new(file_path);

    let file = match File::open(&path) {
        Err(why) => panic!("Couldn't open file '{}', due to {}.", file_path, why),
        Ok(file) => file,
    };

    file
}

/* Converts the provided file into a vector of lines.
 */
fn file_to_vec(file: File) -> Vec<String> {
    let reader = BufReader::new(file);
    let mut lines_vec: Vec<String> = vec![];

    for line in reader.lines() {
        if let Ok(line) = line {
            lines_vec.push(line);
        } else {
            panic!("File contains corrupted data!\n")
        }
    }

    lines_vec
}
