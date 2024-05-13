## JOECRACK² — JOECRACKcrack(er), a fuzzer for [Joe's password cracker](https://github.com/JosephL8912/PasswordCrack)

### Explanation:
Disclaimer: This is very very very basic level fuzzing; I only use values that are 1-2 characters long. And you probably wouldn't have access to the code/backend of something you wanted to fuzz in the real world. Also, I have modified Joe's code to throw exceptions when the user enters a value that is out of bounds.

### Usage:
In its default state, the program will only test single characters for intFuzz and strings that are 2 characters long for strFuzz. This can be modified using the repeat argument, just add (or change) the number where the functions are called.
Also, the strFuzz function will never throw exceptions because it only tests ASCII printables. Thus, passwordCrashes.txt will be blank. If you want more results, you can extend the range of strFuzz on line 4(?) to 592 for extended Latin characters.
For even more fun, check out this website to see what decimal value you need to plug in for your unicode characters: https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0180


### Command line:
Too lazy lol

`python3 joecrack2.py` 

### Dependencies:
- time
  
### Rubric (/55)
- [x] Regular usage of version control software (3)
- [x] Data mutator (10)
     - [x] Begins with a valid input data for the target program (5)
     - [ ] Has command line arguments to restrict/allow specific types of input data (5)
- [x] Fuzzer (20)
     - [x] Choose a target program (10)
     - [x] Create a condition to stop the fuzzer (10)
- [ ] Presentation (20)
     - [x] Well-Designed Slides (5)
     - [x] Engaging (10)
     - [x] Responds to questions well (5)
- [x] README.md (2)
     - [x] Dependencies (1)
     - [ ] Commands and arguments to run (1)
- [x] Extentions (10)
     - [x] Fuzzing program saves data that causes crashes to a file (5)
     - [x] Fuzzing program logs crashes with associated data and info (5)
