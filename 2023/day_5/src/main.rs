pub mod read_input;

use crate::read_input::*;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    println!("{}", challenge_two(input_data));
}

fn challenge_one(data: Vec<String>) -> u64 {
    let mut latest: Vec<Vec<u64>> = vec![];
    let seeds: &str = data[0].split(':').collect::<Vec<&str>>()[1].trim();
    latest.push(seeds.split(' ').map(|x| x.trim().parse::<u64>().unwrap()).collect::<Vec<u64>>());

    let mut is_mapping: bool = false;
    let mut mapping: Vec<Vec<u64>> = vec![];
    for line in &data[2..] {
        if line.as_str() == "" {
            is_mapping = false;

            let mut new_level: Vec<u64> = vec![];
            for i in &latest[latest.len() - 1] {
                let mut converted: bool = false;
                for j in &mapping {
                    if (*i >= j[1]) && (*i <= j[1] + j[2]) {
                        new_level.push(j[0] + (*i - j[1]));
                        converted = true;
                        break;
                    }
                }
                if !converted {
                    new_level.push(*i);
                }
            }
            latest.push(new_level);
            mapping = vec![];

            continue;
        } else if !(line.as_bytes()[0].is_ascii_digit()) {
            is_mapping = true;
            continue;
        }

        if is_mapping {
            mapping.push(line.split(' ').map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>());
        }
    }

    let mut new_level: Vec<u64> = vec![];
    for i in &latest[latest.len() - 1] {
        let mut converted: bool = false;
        for j in &mapping {
            if (*i >= j[1]) && (*i <= j[1] + j[2]) {
                new_level.push(j[0] + (*i - j[1]));
                converted = true;
                break;
            }
        }
        if !converted {
            new_level.push(*i);
        }
    }

    let mut lowest: i64 = -1;
    for i in new_level {
        if lowest < 0 || i < (lowest as u64) {
            lowest = i as i64;
        }
    }

    lowest as u64
}

fn challenge_two(data: Vec<String>) -> u64 {
    let mut start: Vec<u64> = vec![];
    let mut range: Vec<u64> = vec![];
    let mut latest: Vec<Vec<[u64;2]>> = vec![];
    let seeds: Vec<u64> = data[0].split(':').collect::<Vec<&str>>()[1].trim().split(' ')
        .map(|x| x.trim().parse::<u64>().unwrap()).collect::<Vec<u64>>();
    for i in 0..seeds.len() {
        if i % 2 == 0 {
            start.push(seeds[i]);
        } else {
            range.push(seeds[i]);
        }
    }
    let mut earliest: Vec<[u64; 2]> = vec![];
    for i in 0..start.len() {
        earliest.push([start[i], range[i]]);
    }
    latest.push(earliest);

    let mut is_mapping: bool = false;
    let mut mapping: Vec<Vec<u64>> = vec![];
    for line in &data[2..] {
        if line.as_str() == "" {
            is_mapping = false;

            let mut frontier: Vec<[u64; 2]> = vec![];
            let mut yet_to_check: Vec<[u64; 2]> = latest[latest.len() - 1].clone();
            let mut index: usize = 0;
            while index < yet_to_check.len() {
                let i: [u64; 2] = yet_to_check[index];
                let mut mapped: bool = false;
                for j in &mapping {
                    if (i[0] >= j[1]) && (i[0] < j[1] + j[2]) {
                        if i[0] + i[1] <= j[1] + j[2] {
                            frontier.push([j[0] + i[0] - j[1], i[1]]);
                        } else {
                            frontier.push([j[0] + i[0] - j[1], (j[1] + j[2] - 1 - i[0])]);
                            yet_to_check.push([j[1] + j[2], i[1] - (j[1] + j[2] - 1 - i[0])]);
                        }
                        mapped = true;
                        break;
                    } else if (i[0] + i[1] > j[1]) && (i[0] + i[1] <= j[1] + j[2]) {
                        yet_to_check.push([i[0], j[1] - i[0]]);
                        frontier.push([j[0], i[1] - (j[1] - i[0])]);
                        mapped = true;
                        break;
                    } else if (i[0] < j[1]) && (i[0] + i[1] > j[1] + j[2]) {
                        frontier.push([j[0], j[2]]);
                        yet_to_check.push([i[0], j[1] - i[0]]);
                        yet_to_check.push([j[1] + j[2], (i[0] + i[1]) - (j[1] + j[2])]);
                        mapped = true;
                        break;
                    }
                }
                if !mapped {
                    frontier.push(i);
                }

                index += 1;
            }
            latest.push(frontier);
            mapping = vec![];

            continue;
        } else if !(line.as_bytes()[0].is_ascii_digit()) {
            is_mapping = true;
            continue;
        }

        if is_mapping {
            mapping.push(line.split(' ').map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>());
        }
    }

    let mut frontier: Vec<[u64; 2]> = vec![];
    let mut yet_to_check: Vec<[u64; 2]> = latest[latest.len() - 1].clone();
    let mut index: usize = 0;
    while index < yet_to_check.len() {
        let i: [u64; 2] = yet_to_check[index];
        let mut mapped: bool = false;
        for j in &mapping {
            if (i[0] >= j[1]) && (i[0] < j[1] + j[2]) {
                if i[0] + i[1] <= j[1] + j[2] {
                    frontier.push([j[0] + i[0] - j[1], i[1]]);
                } else {
                    frontier.push([j[0] + i[0] - j[1], (j[1] + j[2] - 1 - i[0])]);
                    yet_to_check.push([j[1] + j[2], i[1] - (j[1] + j[2] - 1 - i[0])]);
                }
                mapped = true;
                break;
            } else if (i[0] + i[1] > j[1]) && (i[0] + i[1] <= j[1] + j[2]) {
                yet_to_check.push([i[0], j[1] - i[0]]);
                frontier.push([j[0], i[1] - (j[1] - i[0])]);
                mapped = true;
                break;
            } else if (i[0] < j[1]) && (i[0] + i[1] > j[1] + j[2]) {
                frontier.push([j[0], j[2]]);
                yet_to_check.push([i[0], j[1] - i[0]]);
                yet_to_check.push([j[1] + j[2], (i[0] + i[1]) - (j[1] + j[2])]);
                mapped = true;
                break;
            }
        }
        if !mapped {
            frontier.push(i);
        }

        index += 1;
    }

    let mut lowest: i64 = -1;
    for i in frontier {
        if lowest < 0 || i[0] < (lowest as u64) {
            lowest = i[0] as i64;
        }
    }

    lowest as u64
}
