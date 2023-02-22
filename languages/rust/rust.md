# [Rust](https://www.rust-lang.org/learn)

This repository contains notes on [Rust](https://www.rust-lang.org/learn) programming language.
- [Installation Guide](https://www.rust-lang.org/tools/install)

## [Cargo](https://doc.rust-lang.org/cargo/)
Is the Rust package manager. It is used to **build, test, package, and publish** Rust projects.
```bash
cargo doc  # generates the documentation

cargo new project_name  # creates a new project
cd project_name  # changes the current directory to the project directory
cargo build  # builds the project

cargo run  # builds and runs the project
cargo run --bin file_name  # runs the file without building the project

cargo check  # checks the project for errors
cargo build --release  # builds the project in release mode

cargo test  # runs the tests
cargo test -- --test-threads=1  # runs the tests in a single thread

cargo install package_name  # installs the package
cargo uninstall package_name  # uninstalls the package
```

## [main](./notebook/src/main.rs)
To run any Rust program, you need to have a `main` function. The `main` function is the entry point of the program.
```rust
fn main() {  // main is the entry point of the program
    println!("Hello, world!");  // code...
}
```


## Jupyter Notebook w/ Rust Kernel
```bash
cargo install evcxr_jupyter
evcxr_jupyter --install
```

----
## References
- [std lib](https://doc.rust-lang.org/std/index.html)
- [rsut guide](https://doc.rust-lang.org/edition-guide/introduction.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)

