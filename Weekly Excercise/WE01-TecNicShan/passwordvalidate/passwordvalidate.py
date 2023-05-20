# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER
import string
import random
def validate(password):
    upper = False
    lower = False 
    number = False
    specialChar = False
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    decimals = list(x for x in range(0,10))
    special = list("!-$%&’()*+,./:;<=>?_[]^‘{|}~")
    if len(password) < 8:
        return "Invalid"
    if " " in password or "@" in password or "#" in password:
        return "Invalid"
    for x in uppercase:
        if x in password:
            upper = True
    for x in lowercase:
        if x in password:
            lower = True
    for x in decimals:
        if str(x) in password:
            number = True
    for x in special:
        if x in password:
            specialChar = True
    if upper == True and lower == True and number == True and specialChar == True:
        return "Secure"
    else:
        return "Insecure"

def generate(n):
    final_password = []
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    decimals = list(str(x) for x in range(0,10))
    special = list("!-$%&’()*+,./:;<=>?_[]^‘{|}~")
    
    
    for char in range(n-4):
        insertChar = random.randint(0,3)
        if insertChar == 0:
            final_password.append(uppercase[random.randint(0,25)])
        if insertChar == 1:
            final_password.append(lowercase[random.randint(0,25)])
        if insertChar == 2:
            final_password.append(decimals[random.randint(0,8)])
        if insertChar == 3:
            final_password.append(special[random.randint(0,27)])
    
    final_password.insert(random.randint(0,len(final_password)),uppercase[random.randint(0,25)])
    final_password.insert(random.randint(0,len(final_password)),lowercase[random.randint(0,25)])    
    final_password.insert(random.randint(0,len(final_password)),decimals[random.randint(0,8)])
    final_password.insert(random.randint(0,len(final_password)),special[random.randint(0,27)])

    return "".join(final_password)

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    pass

