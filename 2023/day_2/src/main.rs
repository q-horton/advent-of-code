pub mod read_input;

use crate::read_input::*;

fn main() {
    let input_data: Vec<String> = read_input("input.txt");
    match challenge_two(input_data) {
        Some(x) => println!("{}", x),
        None => println!("Error!")
    }
}

fn challenge_one(games: Vec<String>) -> Option<u32> {
    let mut sum: u32 = 0;
    for game in games {
        let mut game_split = game.split(':');
        let mut game_id = game_split.next()?.split(' ');
        game_id.next();
        let game_num = game_id.next()?.parse::<u32>().unwrap();
        let mut possible: bool = true;
        for draw in game_split.next()?.split(';') {
            for colour in draw.split(',') {
                let mut dummy = colour.trim().split(' ');
                let count = dummy.next()?.parse::<u32>().unwrap();
                let val: &str = dummy.next()?;
                if (val.len() >= 3) && (val == "red") {
                    if count > 12 {
                        possible = false;
                    }
                } else if (val.len() >= 5) && (val == "green") {
                    if count > 13 {
                        possible = false;
                    }
                } else if (val.len() >= 4) && (val == "blue") {
                    if count > 14 {
                        possible = false;
                    }
                }
            }
        }
        if possible {
            sum += game_num;
        }
    }
    Some(sum)
}

fn challenge_two(games: Vec<String>) -> Option<u32> {
    let mut sum: u32 = 0;
    for game in games {
        let mut min_cubes: [u32; 3] = [0, 0, 0];
        let mut game_split = game.split(':');
        let mut game_id = game_split.next()?.split(' ');
        game_id.next();
        for draw in game_split.next()?.split(';') {
            for colour in draw.split(',') {
                let mut dummy = colour.trim().split(' ');
                let count = dummy.next()?.parse::<u32>().unwrap();
                let val: &str = dummy.next()?;
                if (val.len() >= 3) && (val == "red") {
                    if count > min_cubes[0] {
                        min_cubes[0] = count;
                    }
                } else if (val.len() >= 5) && (val == "green") {
                    if count > min_cubes[1] {
                        min_cubes[1] = count;
                    }
                } else if (val.len() >= 4) && (val == "blue") {
                    if count > min_cubes[2] {
                        min_cubes[2] = count;
                    }
                }
            }
        }
        sum += min_cubes[0] * min_cubes[1] * min_cubes[2]; 
    }
    Some(sum)
}
