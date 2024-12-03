pub mod read_input;

use crate::read_input::*;
use std::collections::hash_map::HashMap;
use num::integer::*;

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
    let mut iterations: Vec<u64> = vec![];
    for i in 0..current.len() {
        iterations.push(0);
        while current[i].as_bytes()[2] != 'Z' as u8 {
            let action: char = instructions[(iterations[i] as usize) % instructions.len()] as char;
            if action == 'L' {
                current[i] = maps[&current[i]][0].clone();
            } else if action == 'R' {
                current[i] = maps[&current[i]][1].clone();
            } else {
                panic!("{} is not an action", action);
            }
            iterations[i] += 1;
        }
    }
    
    let mut tot_iterations: u64 = 1;
    for i in 0..iterations.len() {
        tot_iterations = tot_iterations.lcm(&iterations[i]);
    }
    tot_iterations
}
