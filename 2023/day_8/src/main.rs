pub mod read_input;

use crate::read_input::*;
use std::collections::hash_map::HashMap;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    println!("{}", challenge_two(input_data));
}

fn challenge_one(data: Vec<String>) -> u64 {
    let dummy: String = data[0].clone();
    let instructions: &[u8] = dummy.as_bytes();
    let mut maps: HashMap<String, [String; 2]> = HashMap::new();
    for line in &data[2..] {
        let node: String = line.split('=').collect::<Vec<&str>>()[0].trim().to_owned();
        let moves: &str = line.split('=').collect::<Vec<&str>>()[1].trim();
        let left: String = moves.split(',').collect::<Vec<&str>>()[0].trim().replace('(', "");
        let right: String = moves.split(',').collect::<Vec<&str>>()[1].trim().replace(')', "");
        maps.insert(node, [left, right]);
    }
    let mut current: String = "AAA".to_owned();
    let mut iteration: u64 = 0;
    while current.as_str() != "ZZZ" {
        let action: char = instructions[(iteration as usize) % instructions.len()] as char;
        if action == 'L' {
            current = maps[&current][0].clone();
        } else if action == 'R' {
            current = maps[&current][1].clone();
        } else {
            panic!("{} is not an action", action);
        }
        iteration += 1;
    }

    iteration
}

fn is_finished(current: &Vec<String>) -> bool {
    for i in current {
        if i.as_bytes()[2] != 'Z' as u8 {
            return false;
        }
    }
    true
}

fn challenge_two(data: Vec<String>) -> u64 {
    let dummy: String = data[0].clone();
    let instructions: &[u8] = dummy.as_bytes();
    let mut maps: HashMap<String, [String; 2]> = HashMap::new();
    for line in &data[2..] {
        let node: String = line.split('=').collect::<Vec<&str>>()[0].trim().to_owned();
        let moves: &str = line.split('=').collect::<Vec<&str>>()[1].trim();
        let left: String = moves.split(',').collect::<Vec<&str>>()[0].trim().replace('(', "");
        let right: String = moves.split(',').collect::<Vec<&str>>()[1].trim().replace(')', "");
        maps.insert(node, [left, right]);
    }
    let mut current: Vec<String> = vec![];
    for i in maps.keys() {
        if i.as_bytes()[2] == 'A' as u8 {
            current.push((*i).clone());
        }
    }
    let mut iteration: u64 = 0;
    while !is_finished(&current) {
        let action: char = instructions[(iteration % (instructions.len() as u64)) as usize] as char;
        let index: usize;
        if action == 'L' {
            index = 0;
        } else if action == 'R' {
            index = 1;
        } else {
            panic!("{} is not an action", action);
        }
        let mut next: Vec<String> = vec![];
        for i in &current {
            next.push(maps[i][index].clone());
        }
        current = next;
        iteration += 1;
        if iteration % 1000000 == 0 {
            println!("{}", iteration);
        }
    }

    iteration
}
