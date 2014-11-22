I Sing Of

All the necessary text is internal, but you will need Python (developed on 2.7), nltk, and the wordnet corpus. 

The program is now semi-deterministic. It seeds the random number generator with the current year, so barring changes to wordnet it should only generate one novel each calendar year. The repository contains some test output as well as the 2014 novel for the current state of the code.

The code is still a mess, and may be subject to further development, but it should run. My next step is to implement a method to prevent the program from getting stuck within small regions of wordnet that it cannot escape (tends to happen with proper nouns).