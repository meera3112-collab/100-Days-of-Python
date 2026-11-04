alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = []
    for letter in text:
        if letter not in alphabet:
            encrypted_text+=letter
        else:
            index = (alphabet.index(letter) + shift) % 26
            encrypted_text += alphabet[index]
    print("".join(encrypted_text))
    
# # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
# #  by the shift amount and print the decrypted text.

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

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


def caesar(direction):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)




