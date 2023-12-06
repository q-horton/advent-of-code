pub mod read_input;

use crate::read_input::*;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    println!("{}", challenge_two(input_data));
}

fn challenge_one(data: Vec<String>) -> u64 {
    let times: Vec<u64> = data[0].split(':').collect::<Vec<&str>>()[1].trim().split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();
    let distances: Vec<u64> = data[1].split(':').collect::<Vec<&str>>()[1].trim().split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();

    let mut result: u64 = 1;

    for i in 0..times.len() {
        for j in 0..times[i] {
            if j * (times[i] - j) > distances[i] {
                result *= times[i] - 2 * j + 1;
                break;
            }
        }
    }

    result
}

fn challenge_two(data: Vec<String>) -> u64 {
    let time: u64 = data[0].split(':').collect::<Vec<&str>>()[1].trim().split_whitespace().collect::<String>().parse::<u64>().unwrap();
    let distance: u64 = data[1].split(':').collect::<Vec<&str>>()[1].trim().split_whitespace().collect::<String>().parse::<u64>().unwrap();
    
    let mut result: u64 = 0;

    for i in 0..time {
        if i * (time - i) > distance {
            result = time - 2 * i + 1;
            break;
        }
    }

    result
}
