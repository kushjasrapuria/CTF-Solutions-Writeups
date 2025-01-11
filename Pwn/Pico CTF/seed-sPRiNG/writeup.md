# Challange Info

Name : seed-sPRiNG

Difficulty : Hard

Category : Binary Exploitation

Link : https://play.picoctf.org/practice/challenge/50?category=6&page=5

# Writeup

The binary wants you to guess 30 random numbers in row to get the flag.

Using ghidra and reading pseudo C code we can see that the time NULL is passed to srand.

So if we sync the timing of number generation and challange execution we'll get sequence of correct randoom numbers.

I wrote solve.c to generate 30 random numbers.

```bash
./solve && nc jupiter.challenges.picoctf.org 8311
```

This will give the sequence of numbers which if entered correctly will give the flag.

`Note : For this to work your internet connection needs to be good or else seed will differ.`
