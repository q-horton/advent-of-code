pub mod read_input;

use crate::read_input::*;
use std::collections::HashMap;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    println!("{}", challenge_two(input_data));
}

fn space_num_list_to_vec(list: &str) -> Vec<u32> {
    let num_chars: Vec<&str> = list.split(' ').collect::<Vec<&str>>();
    let mut nums: Vec<u32> = vec![];
    for i in num_chars {
        if i.trim() == "" {
            continue;
        }
        nums.push(i.trim().parse::<u32>().unwrap());
    }
    nums
}

fn challenge_one(data: Vec<String>) -> u32 {
    let mut sum: u32 = 0;
    for line in data {
        let card_data: Vec<&str> = line.split(':').collect::<Vec<&str>>()[1].split('|').collect::<Vec<&str>>();
        let win_nums: Vec<u32> = space_num_list_to_vec(card_data[0]);
        let my_nums: Vec<u32> = space_num_list_to_vec(card_data[1]);
        let mut matches: u32 = 0;
        for i in my_nums {
            for j in &win_nums {
                if i == *j {
                    matches += 1;
                    break;
                }
            }
        }
        if matches > 0 {
            sum += 2u32.pow(matches - 1);
        }
    }
    sum
}

fn challenge_two(data: Vec<String>) -> u32 {
    let mut match_mappings: HashMap<u32, u32> = HashMap::new();
    for line in data {
        let card: Vec<&str> = line.split(':').collect::<Vec<&str>>();
        let card_num: u32 = card[0].get(4..).unwrap().trim().parse::<u32>().unwrap();
        let card_data: Vec<&str> = card[1].split('|').collect::<Vec<&str>>();
        let win_nums: Vec<u32> = space_num_list_to_vec(card_data[0]);
        let my_nums: Vec<u32> = space_num_list_to_vec(card_data[1]);
        let mut matches: u32 = 0;
        for i in my_nums {
            for j in &win_nums {
                if i == *j {
                    matches += 1;
                    break;
                }
            }
        }
        match_mappings.insert(card_num, matches);
    }
    let mut card_counts: HashMap<u32, u32> = HashMap::new();
    for i in 1..(match_mappings.len() + 1) {
        card_counts.insert(i as u32, 1);
    }
    for i in 1..(match_mappings.len() + 1) {
        for j in 1..(match_mappings[&(i as u32)] + 1) {
            if (i as u32) + j > (card_counts.len() as u32) {
                break;
            }
            card_counts.insert((i as u32) + j, card_counts[&((i as u32) + j)] + card_counts[&(i as u32)]);
        }
    }
    let mut sum: u32 = 0;
    for i in card_counts {
        sum += i.1;
    }
    sum
}
