"""
--------------------------------------------
Name: Nick Shan
SID: 1759726
CCID: bshan1
AnonID: 1000366406
CMPUT 274, Fall 2022

Assessment: Weekly Exercise #4
--------------------------------------------

TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""
import string
import sys


def full_preprocessing(inlist):
    processed = []
    symbols = list(string.punctuation)
    letters = list(string.ascii_lowercase)
    digits = list(string.digits)

    for x in inlist:
        containsLetters = False
        containsDigits = False
        x = x.lower()
        # print(x)
        for any in x:
            if any in symbols:
                x = x.replace(any, "")
            if any in letters:
                containsLetters = True
            if any in digits:
                containsDigits = True

        if containsLetters is True and containsDigits is True:
            for each in x:
                if each in digits:
                    x = x.replace(each, "")
        if x not in Stop_Words:
            processed.append(x)
    while " " in processed:
        processed.remove(" ")
    while "" in processed:
        processed.remove("")
    # print(processed)
    return " ".join(processed)


def keepdigits(inlist):
    processed = []
    symbols = list(string.punctuation)

    for x in inlist:
        x = x.lower()
        # print(x)
        for any in x:
            if any in symbols:
                x = x.replace(any, "")

        if x not in Stop_Words:
            processed.append(x)
    while " " in processed:
        processed.remove(" ")
    return " ".join(processed)


def keepstops(inlist):
    processed = []
    symbols = list(string.punctuation)
    letters = list(string.ascii_lowercase)
    digits = list(string.digits)

    for x in inlist:
        containsLetters = False
        containsDigits = False
        x = x.lower()
        # print(x)
        for any in x:
            if any in symbols:
                x = x.replace(any, "")
            if any in letters:
                containsLetters = True
            if any in digits:
                containsDigits = True

        if containsLetters is True and containsDigits is True:
            for each in x:
                if each in digits:
                    x = x.replace(each, "")
        processed.append(x)
    while " " in processed:
        processed.remove(" ")
    return " ".join(processed)


def keepsymbols(inlist):
    processed = []
    letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    for x in inlist:
        containsLetters = False
        containsDigits = False
        containsSymbols = False
        x = x.lower()
        # print(x)
        for any in x:
            if any in letters:
                containsLetters = True
            if any in digits:
                containsDigits = True
            if any in symbols:
                containsSymbols = True

        if containsLetters is True and containsDigits is True:
            for each in x:
                if each in digits:
                    x = x.replace(each, "")
        if containsSymbols is True and containsDigits is True:
            for each in x:
                if each in digits:
                    x = x.replace(each, "")
        if x not in Stop_Words:
            processed.append(x)
    return " ".join(processed)


# Global List
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now"
]

if __name__ == "__main__":
    correctArgs = ["keep-digits", "keep-stops", "keep-symbols"]
    if len(sys.argv) == 2 and sys.argv[1] not in correctArgs:
        print("Invalid Command Line Argument")
        print("Usage: python3 preprocess.py <optional argument>")
        print("optional arguements are: keep-digits, keep-stops, keep-symbols")
        sys.exit()
    input = list(map(str, input().split()))
    if len(sys.argv) == 2:
        if sys.argv[1] == "keep-digits":
            print(keepdigits(input))
        elif sys.argv[1] == "keep-stops":
            print(keepstops(input))
        elif sys.argv[1] == "keep-symbols":
            print(keepsymbols(input))

    elif len(sys.argv) == 1:
        print(full_preprocessing(input))
