# [Rust](https://www.rust-lang.org/learn)

Rust is a systems [[programming language]] that **runs blazingly fast, prevents segfaults, and guarantees thread safety**.

It is designed to be a **safe, concurrent, and practical language**. It accomplishes these goals by being memory safe without using garbage collection.

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

cargo test  # runs the tests
cargo test -- --test-threads=1  # runs the tests with one thread
cargo test -- --show-output  # runs the tests and shows the output
cargo check  # checks the project for errors

cargo build --release  # builds the project in release mode

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
- [rust guide](https://doc.rust-lang.org/edition-guide/introduction.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/) - A collection of runnable examples that illustrate various Rust concepts and standard libraries.

