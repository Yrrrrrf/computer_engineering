// ? Terminal related scripts


use std::io;  // io library is part of the standard library (std)
use std::io::Write;  // io library is part of the standard library (std) (Write trait)
use std::io::Read;  // io library is part of the standard library (std) (Read trait)


pub(crate) fn clear() {// Clear and cursor position
    print!("{}[2J", 27 as char);  // Clear the terminal
    print!("{}[1;1H", 27 as char);  // Move the cursor to the top left corner
}


pub(crate) fn set_fg() {  // Set foreground color
    print!("Select foreground color: ");
    let mut fg = String::new();  // String::new() is a constructor (used when you want to modify a string)
    io::stdout().flush().unwrap();  // Allows the print!() to be flushed to the console otherwise it will wait for the next println!()
    io::stdin().read_line(&mut fg).unwrap();  // Read input from the console
    let fg = fg.trim();  // Trim the input to remove the newline character
    match fg {  // Color in Terminal
        "red"   => print!("{}[0;31m", 27 as char),  // red
        "green" => print!("{}[0;32m", 27 as char),  // green
        "yellow"=> print!("{}[0;33m", 27 as char),  // yellow
        "blue"  => print!("{}[0;34m", 27 as char),  // blue
        "purple"=> print!("{}[0;35m", 27 as char),  // purple
        "cyan"  => print!("{}[0;36m", 27 as char),  // cyan
        "white" => print!("{}[0;37m", 27 as char),  // white
        _       => print!("{}[0;37m", 27 as char),  // white (default)
    }
    println!("{} is the foreground color", fg);
}


pub(crate) fn set_bg() {
    print!("Select background color: ");
    let mut bg = String::new();  // String::new() is a constructor (used when you want to modify a string)
    io::stdout().flush().unwrap();  // Allows the print!() to be flushed to the console otherwise it will wait for the next println!()
    io::stdin().read_line(&mut bg).unwrap();  // Read input from the console
    let bg = bg.trim();  // Trim the input to remove the newline character
    match bg {  // Color in Terminal
        "red"   => print!("{}[0;41m", 27 as char),  // red
        "green" => print!("{}[0;42m", 27 as char),  // green
        "yellow"=> print!("{}[0;43m", 27 as char),  // yellow
        "blue"  => print!("{}[0;44m", 27 as char),  // blue
        "purple"=> print!("{}[0;45m", 27 as char),  // purple
        "cyan"  => print!("{}[0;46m", 27 as char),  // cyan
        "white" => print!("{}[0;47m", 27 as char),  // white
        _       => print!("{}[0;47m", 27 as char),  // white (default)
    }
    println!("{} is the background color", bg);
}


pub(crate) fn reset_color() {
    print!("{}[0m", 27 as char);  // Reset color
}

