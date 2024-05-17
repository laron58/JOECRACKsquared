## JOECRACK² — JOECRACKcrack(er), a fuzzer for [Joe's password cracker](https://github.com/JosephL8912/PasswordCrack)

### Explanation:
**DISCLAIMER:** This is very very very basic level fuzzing. You normally wouldn't have access to the code/backend of something you wanted to fuzz in the real world, and I only use values that are 1-2 characters long (by default, for demonstration purposes). Also, I have modified Joe's code to throw exceptions when the user enters a value that is out of bounds.

### Usage:
In their default states, the two fuzzing functions will only test single characters. This can be modified using the length argument, just add (or change) the number where the functions are called.

Also, by default, intFuzz and strFuzz will only test ASCII printables. If you want more results, you can extend the character limit with the chrLim argument (inclusive). 591 will get you through the Latin extensions.

For even more fun, check out this website to see what decimal values to plug in: https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0180

### Command line:
`python3 joecrack2.py` 

### Dependencies:
- itertools
- time
  
### Rubric (39/35)
- [x] Regular usage of version control software (3)
- [x] Data mutator (5/10)
     - [x] Begins with a valid input data for the target program (5)
     - [ ] Has command line arguments to restrict/allow specific types of input data (5)
- [x] Fuzzer (20)
     - [x] Choose a target program (10)
     - [x] Create a condition to stop the fuzzer (10)
- [x] README.md (1/2)
     - [x] Dependencies (1)
     - [ ] Commands and arguments to run (1)
- [x] Extentions (+10)
     - [x] Fuzzing program saves data that causes crashes to a file (+5)
         - Sepearate files for every test point with list of values that cause crashes
     - [x] Fuzzing program logs crashes with associated data and info (+5)
         - Full crash log with values & associated points
