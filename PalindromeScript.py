# how to check palindromes

# First I need a way for a user input. Ideas;
#     1. Prompt to ask for text input
#     2. Store input in variable
#     3. 

# Second, we want to perform a check if the word is a palindrome by;
#     1. copying the variable to a 2nd variable
#     2. Reversing the 2nd variable
#     3. Performing an 'is equal too' comparison
#     4. if equal then return to user that is indeed a palindrome
#     5. if not than return it isn't

# Third, we want a way to reset the variables so that the the user can restart with another word

# Functional programming
# Extras;
    # 1. Create a list that tracks the palindromes
# 2. Create a 2nd list that tracks the non-palindromes
user_input = input('Please type a word here: ')


#Palindrome script

# Function to check if word is a palindrome
def checkPalindrome(input): 
    reverse_input = input[::-1]
    if user_input == reverse_input:
        print(f'{user_input} is indeed a palindrome!')
    else:
        print(f'Womb womb! {user_input} is NOT a palindrome :(')

#Intitial data such as variables or printouts to welcome the user
msg = 'Palindrome Script'
msg2 = 'Welcome user. This script checks if the word of your liking is a palindrome or not'
print(msg)
print(msg2)
user_input = input('Please type a word here: ')

checkPalindrome(user_input)



  
# dictionary with uppercases & counts
# for loop or map: is key uppercase? then count value ot sum
