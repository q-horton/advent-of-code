pub mod read_input;

use crate::read_input::*;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    println!("{}", challenge_two(input_data));
}

fn challenge_one(data: Vec<String>) -> u32 {
    let mut cal_vals: Vec<u8> = vec![];

    for line in data {
        let mut nums: Vec<u8> = vec![];
        for c in line.chars() {
            if c.is_digit(10) {
                nums.push((c as u8) - ('0' as u8));
            }
        }
        let tens: u8 = nums[0];
        let ones: u8 = nums[nums.len() - 1];
        cal_vals.push(10 * tens + ones);
    }

    let mut sum: u32 = 0;
    for val in cal_vals {
        sum += val as u32;
    }
    sum
}

fn does_str_start_numword(line: &str) -> i8 {
    if (line.len() >= 4) && (&line[..4] == "zero") {
        return 0;
    } else if (line.len() >= 3) && (&line[..3] == "one") {
        return 1;
    } else if (line.len() >= 3) && (&line[..3] == "two") {
        return 2;
    } else if (line.len() >= 5) && (&line[..5] == "three") {
        return 3;
    } else if (line.len() >= 4) && (&line[..4] == "four") {
        return 4;
    } else if (line.len() >= 4) && (&line[..4] == "five") {
        return 5;
    } else if (line.len() >= 3) && (&line[..3] == "six") {
        return 6;
    } else if (line.len() >= 5) && (&line[..5] == "seven") {
        return 7;
    } else if (line.len() >= 5) && (&line[..5] == "eight") {
        return 8;
    } else if (line.len() >= 4) && (&line[..4] == "nine") {
        return 9;
    } else {
        return -1;
    }
}

fn challenge_two(data: Vec<String>) -> u32 {
    let mut cal_vals: Vec<u8> = vec![];

    for line in data {
        let mut nums: Vec<u8> = vec![];
        let line_len: usize = line.len();
        for c in 0..line_len {
            if (line.as_bytes()[c] as char).is_digit(10) {
                nums.push((line.as_bytes()[c]) - ('0' as u8));
            } else {
                let next_word_num: i8 = does_str_start_numword(&line[c..]);
                if next_word_num >= 0i8 {
                    nums.push(next_word_num as u8);
                }
            }
        }
        let tens: u8 = nums[0];
        let ones: u8 = nums[nums.len() - 1];
        cal_vals.push(10 * tens + ones);
    }

    let mut sum: u32 = 0;
    for val in cal_vals {
        sum += val as u32;
    }
    sum
}
