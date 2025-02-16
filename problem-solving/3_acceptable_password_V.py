# In this mission you need to create a password verification function.

# The verification conditions are:

# the length should be bigger than 6;
# should contain at least one digit, but it cannot consist of just digits;
# having numbers or containing just numbers does not apply to the password longer than 9;
# a string should not contain the word "password" in any case.

int_pass=input('Enter your password string: ')

def acceptable_password_v(int_pass):
    if len(int_pass)<=6 :
        result=False
        
    elif len(int_pass)<=9 and (int_pass.isdigit()==True or int_pass.find("password")>0):
        result=False
        
    elif int_pass.find("password")>0:
        result=False
        
    else:
        result=True
        
    return result

print(acceptable_password_v(int_pass))

# Input: A string (str).

# Output: A logic value (bool).