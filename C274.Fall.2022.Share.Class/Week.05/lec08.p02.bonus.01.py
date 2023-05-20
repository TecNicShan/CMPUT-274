place = {}
place["Canada"] = "Alberta"
place["Netherlands"] = "Zeeland"
place["USA"] = [ "California", "New York" ]
place["United Kingdom"] = [ "England", "Wales" ]
place["Italy"] = [ "Calabria", "Liguria" ]
print("place:  ", place)
print()

import sys

Debug = False   # Sometimes, print for debugging
InputFilename = "file.input.txt"
OutputFilename = "file.output.txt"


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def open_output(filename=OutputFilename):
    try:
        f = open(filename, "w")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, out=None, prompt=""):
    if out is None:
        out = sys.stdout
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            line = f.readline()
            if Debug:
                print("readline: ", line, file=out, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF", file=out)
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)

for i in place.keys():
    print(i)
print()
for i in place.values():
    print(i)

cFlag = True
while cFlag:
    line1, cFlag = safe_input(prompt="Key:   ")
    if not cFlag:
        break
    line2, cFlag = safe_input(prompt="Value: ")
    if not cFlag:
        break
    place[line1] = line2

print(place)

