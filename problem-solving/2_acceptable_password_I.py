# <!-- 
# You are at the beginning of a password series. Every mission is based on the previous one. The missions that follow will become slightly more complex.

# In this mission, you need to create a password verification function.
# The verification condition is:
# the length should be bigger than 6.

int_pass=input('Enter your password string: ')

def acceptable_password(int_pass):
    if len(int_pass)<=6:
        result=False
    else:
        result=True
    return result

print(acceptable_password(int_pass))


# Input: A string (str).

# Output: A logic value (bool). -->