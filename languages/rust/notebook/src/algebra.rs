// rust square root method

use std::io;  // io library is part of the standard library (std)
use std::io::Write;  // io library is part of the standard library (std) (Write trait)
use std::io::Read;  // io library is part of the standard library (std) (Read trait)


pub(crate) fn square_root(n: f32) -> f32 {
    let sqrt = n.sqrt();
    println!("The square root of {} is {}", n, sqrt);
    return sqrt;
}


pub(crate) fn second_grade_equation(a: f32, b: f32, c: f32) -> (f32, f32) {
    if a == 0.0 {
        println!("a = {} means indeterminate form", a);
        return (0.0, 0.0);  // return a tuple
    } else {  // a != 0.0
        println!("The equation {}x^2 + {}x + {} = 0 is a second grade equation", a, b, c);

        let delta: f32 = (b.powi(2) - 4.0 * a * c)  / (2.0 * a);  // delta = b^2 - 4ac
        let real_part: f32 = -b / (2.0 * a);
        let mut x1: f32 = real_part;
        let mut x2: f32 = real_part;
        // println!("delta = {}", -delta);  // debug
        // println!("delta square root = {}", delta.abs().sqrt());  // delta square root

        if delta == 0.0 {
            println!("The equation has a DOUBLE solution");
            println!("x1 = x2 = {}", real_part);  // x1 = x2 = -b / 2a
        } else if delta < 0.0 {  // delta < 0.0
            println!("The equation has a COMPLEX solution");
            x1 += delta.sqrt();
            x2 += delta.sqrt();
            println!("x1 = {:.2} + {:.2}i", real_part, delta.abs().sqrt());
            println!("x2 = {:.2} - {:.2}i", real_part, delta.abs().sqrt());
        } else {  // delta > 0.0
            println!("The equation has TWO DIFFERENT solutions");
            x1 -= delta.sqrt();
            x2 += delta.sqrt();   
            println!("x1 = {}", x1);
            println!("x2 = {}", x2);
        }

        return (x1, x2);  // return a tuple
    }
}



// todo: create struct complex number

struct ComplexNumber {
    real: f32,  // real part
    imaginary: f32,  // imaginary part
}
