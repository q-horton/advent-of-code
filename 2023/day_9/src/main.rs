pub mod read_input;

use crate::read_input::*;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    println!("{}", challenge_two(input_data));
}

fn challenge_one(data: Vec<String>) -> i64 {
    let mut predictions: Vec<i64> = vec![];
    for line in data {
        let mut differences: Vec<Vec<i64>> = vec![];
        let mut last_elem: Vec<i64> = line.split(' ').map(|x| x.parse::<i64>().unwrap()).collect::<Vec<i64>>();
        differences.push(last_elem.clone());
        while (last_elem.iter().map(|x| {if *x == 0 {return 0;}; 1})).collect::<Vec<u8>>().contains(&1) {
            let mut diff: Vec<i64> = vec![];
            for i in 0..(last_elem.len() - 1) {
                diff.push(last_elem[i + 1] - last_elem[i]);
            }
            last_elem = diff;
            differences.push(last_elem.clone());
        }
        for i in (0..differences.len()-1).rev() {
            let curr_end: i64 = differences[i+1][differences[i+1].len()-1];
            let next_end: i64 = differences[i][differences[i].len()-1];
            differences[i].push(next_end + curr_end);
        }
        predictions.push(differences[0][differences[0].len()-1]);
    }
    predictions.iter().sum()
}

fn challenge_two(data: Vec<String>) -> i64 {
    let mut predictions: Vec<i64> = vec![];
    for line in data {
        let mut differences: Vec<Vec<i64>> = vec![];
        let mut last_elem: Vec<i64> = line.split(' ').map(|x| x.parse::<i64>().unwrap()).collect::<Vec<i64>>();
        differences.push(last_elem.clone());
        while (last_elem.iter().map(|x| {if *x == 0 {return 0;}; 1})).collect::<Vec<u8>>().contains(&1) {
            let mut diff: Vec<i64> = vec![];
            for i in 0..(last_elem.len() - 1) {
                diff.push(last_elem[i + 1] - last_elem[i]);
            }
            last_elem = diff;
            differences.push(last_elem.clone());
        }
        for i in (0..differences.len()-1).rev() {
            let curr_start: i64 = differences[i+1][0];
            let next_start: i64 = differences[i][0];
            differences[i].insert(0, next_start - curr_start);
        }
        predictions.push(differences[0][0]);
    }
    predictions.iter().sum()
}
