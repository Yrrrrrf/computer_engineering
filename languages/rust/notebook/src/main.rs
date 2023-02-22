#![allow(unused_must_use)] // ignore must use result
#![allow(unused_imports)]  // ignore unused imports
#![allow(dead_code)]  // ignore unused functions


use std::io;  // io library is part of the standard library (std)
use std::io::Read;  // io library is part of the standard library (std) (Read trait)
use std::io::Write;  // io library is part of the standard library (std) (Write trait)

mod files;
mod algebra;
mod terminal;
mod control_flow;
mod util;

fn main() {
    // App entry point

    // terminal::clear();  // Clear and cursor position
    // terminal::set_fg();  // Set foreground color
    // terminal::set_bg();  // Set background color
    // terminal::reset_color();  // Reset color

    // println!("{}", util::ask_int());  // Ask for an integer
    // println!("{}", util::ask_float());  // Ask for a float
    // println!("{}", util::ask_str());  // Ask for a string

    // algebra::second_grade_equation(1.0, 2.0, 3.0);

    // control_flow::get_rand_average(8);
    // control_flow::test_if();

    files::hello_file();
    files::read_file("foo.txt");

}



fn add(x: i32, y: i32) -> i32 {
    // Function with parameters and return type
    x + y
}




fn user_input() {
    let mut input = String::new();  // String::new() is a constructor (used when you want to modify a string)
    print!("Enter something: ");
    io::stdout().flush().unwrap();  // Allows the print!() to be flushed to the console otherwise it will wait for the next println!()
    io::stdin().read_line(&mut input).unwrap();  // Read input from the console
    println!("You entered: {}", input.trim());  // Trim the input to remove the newline character
}


fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())  // print the type of T
}


fn data() {
    let s = "Hello";  // &str (string slice) === immutable reference to a string
    let i = 42;  // i32 === 32-bit signed integer

    print_type_of(&s); // &str
    print_type_of(&i); // i32
    print_type_of(&main); // playground::main
    print_type_of(&print_type_of::<i32>); // playground::print_type_of<i32>
    print_type_of(&{ || "Hi!" }); // playground::main::{{closure}}
}


// ? NUMERIC TYPES (int & float) i === signed, u === unsigned, f === float ------------------------------------------------
fn numeric_types() {
    let age: i8 = 30;  // i8, i16, i32, i64 === n-bit signed integer
    let height: u8 = 72;  // u8, u16, u32, u64 === n-bit unsigned integer
    let weight: f32 = 180.5;  // f32, f64 === n-bit floating point number
    // ? String format (int & float)
    println!("{} {} {}", age, height, weight);  // decimal
    println!("{:#?} {:#?}", age, height);  // type & value
    println!("{:.2}", weight);  // round to 2 decimal places
    println!("{:#e} {:#e}", weight, height as f32);  // scientific notation
    println!("{:#b} {:#b}", age, height);  // binary
    println!("{:#o} {:#o}", age, height);  // octal
    println!("{:#x} {:#x}", age, height);  // hex
}


fn char_and_bool() {
    // ? CHAR TYPE (single character) & BOOLEAN TYPE (true or false) ----------------------------------------------------------
    let letter: char = 'a';  // single character
    let letter2 = char::from(65);  // char::from() is a constructor (used when you want to modify a char)   
    println!("{:#?}", letter);  // (type & value)
    println!("{:#?}", letter2);  // (type & value)
    
    let is_true: bool = true;  // true or false    
    println!("{:?}", is_true);  // (type & value)
}


fn strings() {
    // ? STRINGS (immutable) --------------------------------------------------------------------------------------------------
    // String::new() is a constructor (used when you want to modify a string)
    // let mut greeting = String::new();  // "" === empty string
    let mut greeting = String::from("Hello, ");  // "Hello, " === string literal    
    let name: &str = "John";  // This is a string literal, which is immutable (for non-mutable references...)

    greeting.push_str(name);  // Push a string slice (output: Hello, John)
    greeting.push('!');  // Push a single character

    println!("{}", greeting);  // Hello, John!
    println!("{}", greeting.len());  // 12 (length of string)
    println!("{}", greeting.is_empty());  // false (is string empty?)
    println!("{}", greeting.contains("John"));  // true (does string contain substring?)
    println!("{}", greeting.replace("John", "Jane"));  // Hello, John! -> Hello, Jane!
}
