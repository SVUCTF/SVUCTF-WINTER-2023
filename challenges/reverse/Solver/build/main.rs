use itertools::Itertools;
use std::io;
use std::io::Write;

fn banner() {
    print!(
        "************************************\n\
        *       Welcome to the Rust!       *\n\
        *   And Welcome to the bin world!  *\n\
        *  Let's try to Reverse the world! *\n\
        ************************************\n"
    );
}

fn flag_checker(mut a: i64, mut b: i64, mut c: i64, mut d: i64, mut e: i64) {
    let flag = format!("flag{{S_{}_V_{}_U_{}_C_{}_T_{}_F}}", a, b, c, d, e);

    a = a ^ 0xfda;
    b = b ^ 0xedb;
    c = c ^ 0xddc;
    d = d ^ 0xcdd;
    e = e ^ 0xbde;

    if a * 0xfdb55 + b * 0x8048e + c * 0x7f880 - d * 0x0a854 + e * 0x7f8048 == 0x6b659a58b &&
        a * 0xfef55 + b * 0x8cd8e + c * 0x7f450 - d * 0x0fa54 + e * 0x7f548 == 0x1e3a8d33b &&
        a * 0xace55 + b * 0x34f8e + c * 0x0a340 - d * 0xf354 + e * 0x7fed8 == 0xfbc657eb &&
        a * 0xfdc55 + b * 0x4888e + c * 0x7fe20 - d * 0xa054 + e * 0xf548 == 0x1683d53eb &&
        a * 0xaeb55 + b * 0x8048e + c * 0x10a0e - d * 0xa0854 + e * 0x0f0fe == 0x7a95e0d9
    {
        println!("{flag}");
    } else {
        println!("Oh,No!");
    }
}

fn read_numbers() -> (i64, i64, i64, i64, i64) {
    let mut buffer = String::new();

    "abcde"
        .chars()
        .map(|c| {
            print!("{c}: ");
            io::stdout().flush().unwrap();
            io::stdin()
                .read_line(&mut buffer)
                .expect("Failed to read line");
            let number = buffer.trim().parse().expect("Failed to parse number");
            buffer.clear();
            number
        })
        .collect_tuple()
        .expect("Excepted five numbers")
}

fn main() {
    banner();
    println!("Give me 5 numbers, I'll give you flag!");

    let (a, b, c, d, e) = read_numbers();
    flag_checker(a, b, c, d, e);
}
