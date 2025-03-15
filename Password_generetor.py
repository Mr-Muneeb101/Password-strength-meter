import string
import random

def Password_Generetor():

    Special_characters = "!@#$%^&*()_"
    Digits = "1234567890"
    C_alphabets = string.ascii_uppercase
    S_alphabets = string.ascii_uppercase
   
    Password = f"{random.choice(Special_characters)}{random.choice(Digits)}{random.choice(C_alphabets)}{random.choice(S_alphabets)}"

    Password = [
        random.choice(Special_characters),
        random.choice(Digits),
        random.choice(C_alphabets),
        random.choice(S_alphabets)
        ]
  
    all = Special_characters + Digits + C_alphabets + S_alphabets


    for i in  range(12 - len(Password)):
        random_charac = random.choice(all);
        Password.append(random_charac) 

    # print(Password)
    random.shuffle(Password)
    # print(Password)
    genreted_Password = "".join(Password)
    # print(Password)
    # print(genreted_Password)
    return genreted_Password;
    
