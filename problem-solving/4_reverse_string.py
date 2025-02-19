# Reverse a string and print it

str1=input('Enter your string: ')

def revese_str(str1):
    rev_str1=''
    
    for i in range(len(str1)-1,0,-1):
        rev_str1+=str1[i]        
        
    return rev_str1
    
print(revese_str(str1))
