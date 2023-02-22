#![allow(unused)]


use std::fs::File;
use std::io::prelude::*;

use crate::terminal;


// create a file and write to it
pub(crate) fn hello_file() -> std::io::Result<()> {
    let mut file = File::create("foo.txt")?;  // create a file
    
    file.write_all(b"Hello, world!")?;
    // write to the file (b before the string is a byte string)
    // write_all() returns a Result<T, E> where T is the number of bytes written

    Ok(())  // return Ok if no error
}

// read a file
pub(crate) fn read_file(name: &str) -> std::io::Result<()> {
    let mut file = File::open(name)?;  // open a file
    let mut contents = String::new();  // create a new string
    file.read_to_string(&mut contents)?;  // read the file to the string
    println!("With text:\n{}", contents);  // print the string

    Ok(())  // return Ok if no error
}