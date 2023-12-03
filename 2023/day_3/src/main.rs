pub mod read_input;

use crate::read_input::*;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    match challenge_two(input_data) {
        Some(x) => println!("{}", x),
        None => println!("Error!")
    }
}

fn clamp(value: isize, min: usize, max: usize) -> usize {
    if value < 0 {
        return min;
    }
    let val: usize = value as usize;
    if val < min {
        return min;
    } else if val > max {
        return max;
    } else {
        return val;
    }
}

fn is_part_no(data: &Vec<String>, row: usize, start: usize, end: usize) -> bool {
    let mut is_part_no: bool = false;
    for i in clamp((start as isize) - 1, 0, data[row].len())..clamp((end as isize) + 1, 0, data[row].len()) {
        for j in clamp((row as isize) - 1, 0, data.len())..clamp((row as isize) + 2, 0, data.len()) {
            if !((data[j].as_bytes()[i] as char).is_digit(10) || (data[j].as_bytes()[i] as char) == '.') {
                is_part_no = true;
                break;
            }
        }
        if is_part_no {
            break;
        }
    }
    is_part_no
}

fn challenge_one(data: Vec<String>) -> Option<i32> {
    let mut sum: i32 = 0;
    for row in 0..data.len() {
        let mut start_num: usize = data[row].len();
        let mut end_num: usize = 0;
        for col in 0..data[row].len() {
            if (data[row].as_bytes()[col] as char).is_digit(10) {
                if col > end_num || start_num > col {
                    start_num = col;
                    end_num = data[row].len();
                }
            } else if col < end_num {
                end_num = col;
                if is_part_no(&data, row, start_num, end_num) {
                    let dummy: i32 = data[row].as_str().get(start_num..end_num)?.parse::<i32>().unwrap();
                    sum += dummy;
                }
            }
        }
        if (data[row].as_bytes()[data[row].len() - 1] as char).is_digit(10) {
            if is_part_no(&data, row, start_num, data[row].len()) {
                let dummy: i32 = data[row].as_str().get(start_num..)?.parse::<i32>().unwrap();
                sum += dummy;
            }
        }
    }
    Some(sum)
}

fn get_num(row: &String, col: usize) -> Option<i32> {
    let mut curr_col: isize = col as isize;
    let start: usize;
    let end: usize;
    while curr_col >= 0 && (row.as_bytes()[curr_col as usize] as char).is_digit(10) {
        curr_col -= 1;
    }
    start = (curr_col + 1) as usize;
    curr_col = col as isize;
    while curr_col < (row.len() as isize) && (row.as_bytes()[curr_col as usize] as char).is_digit(10) {
        curr_col += 1;
    }
    end = curr_col as usize;
    let value: i32 = row.as_str().get(start..end)?.parse::<i32>().unwrap();
    Some(value)
}

fn part_of_same_num(nums: &Vec<[usize; 2]>, row: usize, col: usize) -> bool {
    for i in nums {
        if i[0] == row && i[1].abs_diff(col) <= 1 {
            return true;
        }
    }
    false
}

fn challenge_two(data: Vec<String>) -> Option<i32> {
    let mut sum: i32 = 0;
    for row in 0..data.len() {
        for col in 0..data[row].len() {
            if (data[row].as_bytes()[col] as char) == '*' {
                let mut nums: Vec<[usize; 2]> = vec![];
                let mut distinct_nums: Vec<[usize; 2]> = vec![];
                for i in clamp((row as isize) - 1, 0, data.len())..clamp((row as isize) + 2, 0, data.len()) {
                    for j in clamp((col as isize) - 1, 0, data[row].len())..clamp((col as isize) + 2, 0, data[row].len()) {
                        if (data[i].as_bytes()[j] as char).is_digit(10) {
                            if !part_of_same_num(&nums, i, j) {
                                distinct_nums.push([i, j]);
                            }
                            nums.push([i, j]);
                        }
                    }
                }
                if distinct_nums.len() == 2 {
                    let mut product: i32 = 1;
                    for i in distinct_nums {
                        let num: i32 = get_num(&data[i[0]], i[1])?;
                        product *= num;
                    }
                    sum += product;
                }
            }
        }
    }
    Some(sum)
}
