# Miller Rabin and Fast Exponentiation

## Files
- main.c
- Makefile
- README.md

## Compile Steps
- make all          (Will compile all nessacery file with error flags)
- make clean        (Will clean/remove the created files by the compilers)


## Run Instructions
./main -a <int>, -b <int> and -n <int> (fast exponentiation)
./main -n <int> and -a <int> or -s <int> (Miller–Rabin algorithm)


## Author
### 👤 Yekaalo Habtemichael
* Github: [@ymikea](https://github.com/ymikea)


## Implementation
Fast exponentiation is a method to calculate large number of exponent. The recursive method could work fine just it will be very slow especially for encryption of data. The method we used makes it fasted because it uses modular arithmetic rule. For example (a*b) mod n is equivalent to [(a mod n) * (b mod n)] mod n which by factoring we can accomplish multiplying large numbers efficently.


Miller Rabin is typically used to test a large number for primality. The Miller-Rabin test picks a random 'a'. Given 'n' find 's' so that 'n-1 = (2^s)*q' for some odd 'q'. Then we implement a single Miller-Rabin:
 1. Pick a random 'a' which 1 < a > n-1.
 2. If a^q = 1 then 'n' passes.
 3. Otherwise, " for i = 0 to s-1 if a^((2^i)*q) == -1or(n-1) then 'n' passes"
 4. Otherwise 'n' is composite.  
 The randome number 'a' can be picked by the user or by the program. We call this random number a witness. If you decide that n is composite, you will know that this is the correctanswer. If you guess that n is prime, there is some chance that you were just unlucky. But if you guess that n is prime, the chance that you are wrong is less than (.25)^k.


## License
[MIT](https://choosealicense.com/licenses/mit/) &copy; 2020 Yekaalo Habtemichael 
