import itertools #importing all the modules
import string
import sys
import hashlib
import bcrypt

alpha = string.printable #set alpha equal too all the printible a

def bruteForce(mode, pwd):
    counter = 0 #counter for how many tries it takes

    for length in range(1, 999): #tries all lengths from 1 to max
        for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
            target = "".join(comb)
            counter += 1
            if (mode == 0): #plain
                if (target == pwd): #compare guess to the password
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
            elif (mode == 1): #md5
                hashedTarget = hashlib.md5(target.encode('utf-8')).hexdigest() #hashes target with MD5
                if (hashedTarget == pwd): #compare guess hash with actual hash
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
            elif (mode == 2): #sha256
                hashedTarget = hashlib.sha256(target.encode('utf-8')).hexdigest() #hashes target with sah256
                if (hashedTarget == pwd): #compare guess hash with actual hash
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
            elif (mode == 3): #bcrypt
                encodeTarget = target.encode('utf-8') 
                if (bcrypt.checkpw(encodeTarget, pwd.encode('utf-8'))): #compare guess to the hash using bcrypt 
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program

def dictionaryAtk(mode, pwd):
    counter = 0 #counter for how many tries it takes
    passList = open("passList.txt", "r").read() #read file
    pList = passList.splitlines() #create a list of passwords
    for p in pList: #itterates over the passwords
        counter += 1
        if (mode == 0):
            if (p == pwd): #compare guess to the password
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
        
        elif (mode == 1):
            hashedp = hashlib.md5(p.encode('utf-8')).hexdigest() #hashes target with MD5
            if (hashedp == pwd): #compare guess to the password
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
        
        elif (mode == 2):
            hashedp = hashlib.sha256(p.encode('utf-8')).hexdigest() #hashes target with sha256
            if (hashedp == pwd): #compare guess to the password
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
                
        elif (mode == 3):
            encodep = p.encode('utf-8') 
            if (bcrypt.checkpw(encodep, pwd.encode('utf-8'))): #compare guess to the hash using bcrypt
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
        
        if (counter == 10000):
            print ("Password wasn't found in dictionary :(")


def intFuzz(value, point):
    try:
        toInt = int(value)
        print(f"{value} passed point #{point}")
        if point == "1":
            if value == "2":
                #choice === 2 (1a)
                for char in (chr(i) for i in range (32, 127)):
                    #encrypt method
                    intFuzz(char, "1b")
            for char in (chr(i) for i in range (32, 127)):
                #crack method
                intFuzz(char, "2")
        elif point == "2":
            for char in (chr(i) for i in range (32, 127)):
                #target
                strFuzz(char, "3")
    except:
        print(f"{value} failed point #{point}")

for char in (chr(i) for i in range (32, 127)):
    #choice
    intFuzz(char, "1")

""" 
choice = int(input("\n\n*******MENU*******\n\n1.Plaintext\n2.Encrpyted\nHow is the password stored: "))

if choice == 2:
    encryptMode = int(input("1.MD5\n2.SHA-256\n3.BCrypt (very slow)\nWhat encrpytion cracking mode: "))
    
method = int(input("1.BruteForce\n2.Dictionary\nWhat method: "))

password = str(input("What is the target? "))

if (choice == 1): #plaintext cracking
    if (method == 1): #bruteforce
        bruteForce(0,password)
        
    elif (method == 2): #dictionary
        dictionaryAtk(0, password)
                
if (choice == 2): #hash cracking
    if (method == 1): #bruteforce
        bruteForce(encryptMode,password)
                        
    if (method == 2): #dictionary
        dictionaryAtk(encryptMode,password)
"""
