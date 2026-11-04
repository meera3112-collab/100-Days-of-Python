# TODO-1
# Import and print the logo from art.py when the program starts.

from art import logo
print(logo)

# TODO-2:
# What happens if the user enters a number/symbol/space that's not in the List alphabet?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g.

# original_text = "meet me at 3!"
# cipher_text = "XXXX XX XX 3!"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_over = False

def encrypt(text, shift):
    encrypted_text = []
    for letter in text:
        if letter not in alphabet:
            encrypted_text+=letter
        else:
            index = (alphabet.index(letter) + shift) % 26
            encrypted_text += alphabet[index]
    print("".join(encrypted_text))

def decrypt(text, shift):
    encrypted_text = []
    for letter in text:
        if letter not in alphabet:
            encrypted_text+=letter
        else:
            index = (alphabet.index(letter) - shift) % 26
            # if index < 0:
            #     index = 26 - index
            encrypted_text += alphabet[index]
    print("".join(encrypted_text))

# TODO-3:
# Can you figure out a way to restart the cipher program?

# e.g.

# Type 'yes' if you want to go again. Otherwise, type 'no'.

# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.

def caesar(direction):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input!!!")

while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    caesar(direction)
    continue_game = input("Type 'yes' if you want to go again. Otherwise, type 'no': \n").lower()
    if continue_game == 'no':
        game_over = True

    
