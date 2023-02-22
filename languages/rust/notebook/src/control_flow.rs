// ? [Control Flow](https://doc.rust-lang.org/stable/rust-by-example/flow_control.html)

// Path: src\control_flow.rs

// ignore unused imports
#![allow(unused_imports)]  // ignore unused imports
#![allow(unused_variables)]  // ignore unused imports

#![allow(dead_code)]  // ignore unused functions

use std::io;  // io library is part of the standard library (std)
use std::io::Write;  // io library is part of the standard library (std) (Write trait)
use std::io::Read;  // io library is part of the standard library (std) (Read trait)

// import random number generator
use rand;  // import random number generator
use rand::Rng;  // import random number generator
use rand::thread_rng;  // import random number generator


// ? for loop's ---------------------------------------------------------------------------------------------------------------

fn sum_n_odd(n: i16) -> i16 {  // sum of n first odd numbers
    let mut sum = 0;
    for x in 0..n {  // n odd numbers
        sum += 2 * x + 1;  // sum the next odd number
        print!("{} + ", 2 * x + 1)
    }

    println!("0 = {sum}", sum=sum);  // print the sum
    println!("n^2 = {n}", n=n*n);  // print n^2
    return sum;
}


pub(crate) fn ask_first_n_odd() {
    let mut input = String::new();
    print!("Enter n: ");
    io::stdout().flush().unwrap();  // Allows the print!() to be flushed to the console otherwise it will wait for the next println!()
    io::stdin().read_line(&mut input).unwrap();  // Read input from the console
    let n = input.trim().parse::<i16>().unwrap();  // Trim the input to remove the newline character    
    sum_n_odd(n);  // sum n first odd numbers
}


pub(crate) fn get_rand_average(n: i16) -> f32 {
    let mut input = String::new();
    print!("Enter n: ");  // ask for n random numbers
    io::stdout().flush().unwrap();  // Allows the print!() to be flushed to the console otherwise it will wait for the next println!()
    io::stdin().read_line(&mut input).unwrap();  // Read input from the console
    let n = input.trim().parse::<i16>().unwrap();  // Trim the input to remove the newline character

    let mut sum: f32 = (0..n).map(|_| rand::thread_rng().gen_range(0.00, 10.00)).sum();
    // sum(rand(0, 10) for i in range(n))  // sum of n random numbers

    let n = n as f32;  // cast n as float
    sum /= n;  // average of n random numbers
    println!("Average = {sum}", sum=sum);  // print the average

    return sum;  // return the average
}


// ? if loop's ----------------------------------------------------------------------------------------------------------------

pub(crate) fn test_if() {
    let n = 5;
    if n < 0 {
        println!("{} is negative", n);
    } else if n > 0 {
        println!("{} is positive", n);
    } else {
        println!("{} is zero", n);
    }
}





