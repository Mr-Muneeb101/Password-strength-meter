# PASSWORD STRENGTH METER
import re
import streamlit as st
import random
import string

# Password Generetor
def Password_Generetor():
    Special_characters = "!@#$%^&*()_"
    Digits = "1234567890"
    C_alphabets = string.ascii_uppercase
    S_alphabets = string.ascii_lowercase
   
    Password = f"{random.choice(Special_characters)}{random.choice(Digits)}{random.choice(C_alphabets)}{random.choice(S_alphabets)}"

    Password = [
        random.choice(Special_characters),
        random.choice(Digits),
        random.choice(C_alphabets),
        random.choice(S_alphabets)
        ]
  
    all = Special_characters + Digits + C_alphabets + S_alphabets


    for _ in range(8 - len(Password)):
        random_charac = random.choice(all);
        Password.append(random_charac) 

    # print(Password)
    random.shuffle(Password)
    # print(Password)
    genreted_Password = "".join(Password)
    # print(Password)
    # print(genreted_Password)
    return genreted_Password;
    


# my logic
def password_strength_meter(password):
    score = 0

    weak_passwords = {
    "password", "password123", "123456", "12345678", "qwerty", "abc123", 
    "letmein", "monkey", "football", "iloveyou", "admin", "welcome"
    }
    
    if(password.lower() in weak_passwords):
        st.error("This Password is very common and Weak that is why it is block.")
    else:
    # check 1
     if(len(password)>=8):
        score = score + 2
        # print("condition 1 pass" ,score);
        st.success("condition 1 pass, The password contain 8 or mre than 8 characters" );
     else:
        st.error("the password should be atleast 8 characters long");
# check 2
     if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score = score + 1
        # print("condition 2 pass" ,score);
        st.success("condition 2 pass,The password contain atleast 1 small alphabet and 1 capital" );
     else:
        st.error("the password should have atleast 1 upper case and 1 lower case character");
# check 3
     if re.search(r"[!@#$%^&*]",password):
        score = score + 1
        # print("condition 3 pass" ,score);
        st.success("condition 3 pass, The password contain atleast 1 speacial character" );
     else:
        st.error("The Password should contain atleast 1 special character");
# check 4 
     if re.search(r"[0-9]",password):
        score= score + 1;
        # print("condition 1 pass" ,score);
        st.success("condition 4 pass, The Password contain atleast 1" );
     else:
        # print("the password should contain atleast one digit");
        st.error("the password should contain atleast one digit");
# last check for checking total strength
     if(score == 5):
        st.success(f"your score is {score}")
        st.success("The Password is Very Very Strong NICE!")
     elif(score == 4 or score == 3):
      st.success(f"your score is {score}")
      st.success("The Password is not Very Strong NICE!!, make it better")
     elif(score < 2 or score == 2):
        st.warning(f"your score is {score}")
        st.warning("The Passowrd is very Weak, try another password or make it strong.")
 
# title
st.title("NEEB PASSWORD CHECKER");


user_name = st.text_input("PLese Enter your User name")
if user_name:
    st.success(f"{user_name} accepeted Successfully")
user_pas = st.text_input("PLese Enter your Password",type="password");
if user_pas:

    password_strength_meter(user_pas);

if st.button("generate a Strong Password (recomended)"):
    strong_passowrd = Password_Generetor()
    st.success(f"Your new Strong Password is : \"{strong_passowrd}\" ");
    st.text_input("Your Generated Password:",value=strong_passowrd, key="password_display")
   



