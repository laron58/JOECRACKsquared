import time

methodList = []
def intFuzz(name, max, repeat = 1, chrLim = 126, value = ""):
    if repeat == 0:
        if value == " " or value == "  ":
            print(f"Fuzzing {name} block...")
            time.sleep(1)
        try:
            toInt = int(value)
            if toInt > max or toInt < 1:
                raise ValueError
            print(f"{value} passed {name} check")
        except ValueError:
            #print(f"{value} failed point #{point}")
            lists[f"{name}Crashes"].append(value)
            logList.append(f"{value} crashed {name} check")
    else:
        for char in (chr(i) for i in range (32, chrLim + 1)):
            # Creates value recursively
            newVal = value + char
            intFuzz(name, max, repeat - 1, chrLim, newVal)

def strFuzz(name, repeat = 1, chrLim = 126, value = ""):
    if repeat == 0:
        if value == " " or value == "  ":
            print(f"Fuzzing {name} block...")
            time.sleep(1)
        #print(value)
        try:
            toStr = str(value)
            if ord(toStr[0]) < 32 or ord(toStr[0]) > 126:
                raise ValueError
            if name == "methodArg":
                if toStr != "-b" and toStr != "-d":
                    raise ValueError
            elif name == "choiceArg":
                if toStr != "-p" and toStr != "-e":
                    raise ValueError
            elif name == "encryptModeArg":
                if toStr != "-m" and toStr != "-s" and toStr != "-b":
                    raise ValueError
            if name != "password":
                print(f"{value} passed {name} check")
        except ValueError:
            #print(f"{value} failed point #{point}")
            lists[f"{name}Crashes"].append(value)
            logList.append(f"{value} crashed {name} check")
    else:
        for char in (chr(i) for i in range (32, chrLim + 1)):
            # Creates value recursively
            newVal = value + char
            strFuzz(name, repeat - 1, chrLim, newVal)

logList = []
lists = {
    "choiceCrashes":[],
    "choiceArgCrashes":[],
    "methodCrashes":[],
    "methodArgCrashes":[],
    "encryptModeCrashes":[],
    "encryptModeArgCrashes":[],
    "passwordCrashes":[],
}

try:
    intFuzz("choice", 2, 2)
    intFuzz("encryptMode", 3)
    intFuzz("method", 2)
    strFuzz("password", 2, 591)
    strFuzz("methodArg", 2)
    strFuzz("choiceArg", 2)
    strFuzz("encryptModeArg", 2)
except KeyboardInterrupt:
    print("Fuzzing stopped.")

print("Total crashes:", len(logList))
#print(lists)

with open("crashLog.txt", "w", encoding = "utf-8") as file:
    file.write("\n".join(logList))
print("Crash log updated.")
for list in lists:
    with open(f"{list}.txt", "w", encoding = "utf-8") as file:
        file.write("\n".join(lists[list]))
print("Crash lists updated.")
    
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