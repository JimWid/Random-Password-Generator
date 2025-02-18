# collect user preferences
# - lenght
# - should contain uppercase
# - should contain special characters
# - should contain digits

# create all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure lenght is valid

import random
import string

def generate_password():  #creating function to generate password
    lenght = int(input("Enter desired password length: ").strip()) #asking for length
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() #asking if should include uppercase letters
    include_special = input("Include special characters? (yes/no): ").strip().lower() #asking if should include special characters
    include_digits = input("Include digits? (yes/no): ").strip().lower() #askign if should include digits

    if lenght < 4: #veryfing if length is valid
        print("The password lenght must be at least 4 characters.")
        return
    
    lower = string.ascii_lowercase #calling string. library to print all lowercase letters and putting it on a variable
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else "" #calling all uppercase letters 
    special = string.punctuation if include_special == "yes" else "" # same for special characters
    digits = string.digits if include_digits == "yes" else "" #same for digits
    all_characters = lower + uppercase + special + digits #adding all characters in ONE variable

    requires_characters = [] #creating a list for the required characters
    if include_uppercase == "yes":
        requires_characters.append(random.choice(uppercase)) #adding a random character from the uppercase variable
    if include_special == "yes":
        requires_characters.append(random.choice(special)) #same for the special characters
    if include_digits == "yes":
        requires_characters.append(random.choice(digits)) #same for the digits

    remaining_length = lenght - len(requires_characters) #counting the remaining length
    password = requires_characters # renaming required_characters to password

    for _ in range(remaining_length): #for loop to add random characters to the password for the remaining length
        character = random.choice(all_characters) #creating varible character = random characters from all characters
        password.append(character) #adding them to password (still a list)
    
    random.shuffle(password) #shuffle the password

    global str_password #global variable
    str_password = "".join(password) #making the list a string
    return str_password

generate_password() #calling the function
print(str_password) #printing final password

