import itertools
import time

def intFuzz(name, max, length = 1, chrLim = 126):
    print(f"Fuzzing {name} block...")
    #Gives time for the user to terminate fuzzing
    time.sleep(1)
    charList = []
    #Exclues control codes from list
    for char in (chr(i) for i in range (32, chrLim + 1) if i not in range(127, 160)):
        charList.append(char)
    chars = "".join(charList)
    #Tests values {length} characters long and below
    for len in range(1, length + 1):
        for tuple in (itertools.product(chars, repeat = len)):
            value = "".join(tuple)
            try:
                #Value must be int to pass
                toInt = int(value)
                #Value must be in range to pass
                if toInt not in range(1, max + 1):
                    raise ValueError
                #If not caught by errors, pass
                print(f"{value} passed {name} check")
            except ValueError:
                #Adds crashing value to specific list and full log
                lists[f"{name}Crashes"].append(value)
                logList.append(f"{value} crashed \"{name}\"")

def strFuzz(name, length = 1, chrLim = 126):
    print(f"Fuzzing {name} block...")
    time.sleep(1)
    charList = []
    for char in (chr(i) for i in range (32, chrLim + 1) if i not in range(127, 160)):
        charList.append(char)
    chars = "".join(charList)
    for len in range(1, length + 1):
        for tuple in (itertools.product(chars, repeat = len)):
            value = "".join(tuple)
            try:
                #Value must be str to pass
                toStr = str(value)
                #Value must be within "printable" range
                if ord(toStr[0]) not in range (32, 127):
                    raise ValueError
                #Value must match allowed arguments
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
                logList.append(f"{value} crashed \"{name}\"")

#Big list & dictionary
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
    #Max 2
    intFuzz("choice", 2)
    #Max 3, chrLim = 591
    intFuzz("encryptMode", 3, chrLim = 591)
    #Max 2, length 2
    intFuzz("method", 2, 2)
    #Length 1, chrLim = 591
    strFuzz("password", 1, 591)
    #Length 2
    strFuzz("methodArg", 2)
    strFuzz("choiceArg", 2)
    strFuzz("encryptModeArg", 2)
#Condition to stop the fuzzer: Ctrl + C
except KeyboardInterrupt:
    print("Fuzzing stopped.")

print("Total crashes:", len(logList))
with open("crashLog.txt", "w", encoding = "utf-8") as file:
    file.write("\n".join(logList))
print("Crash log updated.")
for list in lists:
    with open(f"{list}.txt", "w", encoding = "utf-8") as file:
        file.write("\n".join(lists[list]))
print("Crash lists updated.")
