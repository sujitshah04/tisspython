# This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.

# Input: Two arguments. Both are of type int.
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))


# Output: Int.
def mult_two(a,b):
    ans=a*b
    return ans

print(f"Multiplication of {a} and {b} is: {mult_two(a,b)}")
# Examples:

# assert mult_two(3, 2) == 6
# assert mult_two(0, 1) == 0