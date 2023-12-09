pub mod read_input;

use crate::read_input::*;
use std::collections::hash_map::HashMap;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    println!("{}", challenge_two(input_data));
}

fn str_to_hand_vals(hand: &str, chal_two: bool) -> Vec<u8> {
    let mut hand_vals: Vec<u8> = vec![];
    for i in hand.as_bytes() {
        if (*i as char).is_digit(10) {
            if *i >= ('2' as u8) && *i <= ('9' as u8) {
                hand_vals.push(*i - ('0' as u8));
            }
        } else if *i == ('T' as u8) {
            hand_vals.push(10);
        } else if *i == ('J' as u8) {
            if chal_two {
                hand_vals.push(1);
            } else {
                hand_vals.push(11);
            }
        } else if *i == ('Q' as u8) {
            hand_vals.push(12);
        } else if *i == ('K' as u8) {
            hand_vals.push(13);
        } else if *i == ('A' as u8) {
            hand_vals.push(14);
        } else {
            hand_vals.push(0);
        }
    }
    hand_vals
}

fn hand_to_score(hand: &Vec<u8>) -> u8 {
    let hand_type: u8;
    let mut card_counts: HashMap<u8, u8> = HashMap::new();
    for i in hand {
        let mut counted: bool = false;
        for j in card_counts.keys() {
            if *i == *j {
                card_counts.insert(*i, card_counts[j] + 1);
                counted = true;
                break;
            }
        }
        if !counted {
            card_counts.insert(*i, 1);
        }
    }
    let jokers: u8;
    if card_counts.contains_key(&1) {
        jokers = card_counts[&1];
        card_counts.remove(&1);
    } else { jokers = 0; }
    let mut counts: Vec<u8> = card_counts.values().map(|x| *x).collect::<Vec<u8>>();
    counts.sort();
    let max_count: u8;
    if counts.len() == 0 {
        max_count = 0;
    } else { max_count = counts[counts.len() - 1]; }
    if max_count + jokers == 5 {
        hand_type = 6;
    } else if max_count + jokers == 4 {
        hand_type = 5;
    } else if max_count + jokers == 3 {
        if counts[counts.len() - 2] == 2 {
            hand_type = 4;
        } else {
            hand_type = 3;
        }
    } else if max_count + jokers == 2 {
        if counts[counts.len() - 2] == 2 {
            hand_type = 2;
        } else {
            hand_type = 1;
        }
    } else {
        hand_type = 0;
    }
    hand_type
}

fn challenge_one(data: Vec<String>) -> u64 {
    let mut hands: Vec<(u8, Vec<u8>, u64)> = vec![];
    for line in data {
        let hand_raw: &str = line.split_ascii_whitespace().collect::<Vec<&str>>()[0];
        let bid: u64 = line.split_ascii_whitespace().collect::<Vec<&str>>()[1].parse::<u64>().unwrap();
        let hand: Vec<u8> = str_to_hand_vals(hand_raw, false);
        hands.push((hand_to_score(&hand), hand, bid));
    }
    hands.sort();
    let mut sum: u64 = 0;
    for i in 0..hands.len() {
        sum += ((i as u64) + 1) * hands[i].2;
    }
    sum
}

fn challenge_two(data: Vec<String>) -> u64 {
    let mut hands: Vec<(u8, Vec<u8>, u64)> = vec![];
    for line in data {
        let hand_raw: &str = line.split_ascii_whitespace().collect::<Vec<&str>>()[0];
        let bid: u64 = line.split_ascii_whitespace().collect::<Vec<&str>>()[1].parse::<u64>().unwrap();
        let hand: Vec<u8> = str_to_hand_vals(hand_raw, true);
        hands.push((hand_to_score(&hand), hand, bid));
    }
    hands.sort();
    let mut sum: u64 = 0;
    for i in 0..hands.len() {
        sum += ((i as u64) + 1) * hands[i].2;
    }
    sum
}
