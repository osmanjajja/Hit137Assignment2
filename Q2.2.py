# Part 1: Process the string, convert even numbers and uppercase letters to ASCII

def process_string(s):
    # Separate numbers and letters
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])

    # Convert even numbers in the number string to ASCII
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_even_numbers = [ord(str(num)) for num in even_numbers]

    # Convert uppercase letters in the letter string to ASCII
    uppercase_letters = [char for char in letter_string if char.isupper()]
    ascii_uppercase_letters = [ord(char) for char in uppercase_letters]

    # Output results
    print("Numbers in the string:", number_string)
    print("Letters in the string:", letter_string)
    print("Even numbers:", even_numbers)
    print("ASCII Decimal of Even Numbers:", ascii_even_numbers)
    print("Uppercase Letters:", uppercase_letters)
    print("ASCII Decimal of Uppercase Letters:", ascii_uppercase_letters)


# Example string to process
s = '56aAww1984ktsr725270yNm145s785fSq31D0'
process_string(s)


# Part 2: Decrypt the cryptogram using Caesar cipher and find the correct shift key

# Function to decrypt the Caesar cipher
def decrypt_caesar_cipher(ciphertext, shift_key):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_key - shift) % 26 + shift)
        else:
            decrypted_text += char  # Keep spaces and other symbols unchanged
    return decrypted_text

# Function to try all possible shifts and find the correct one


def find_correct_shift(ciphertext):
    for shift in range(1, 26):  # Shift values from 1 to 25
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")


# Provided cryptogram
ciphertext = """
VZ FRNYSVFU VZCNVGNAQ NAQ N YVGGYR VARFHPRE V ZNXR ZVFGNGRF V NZ BHG BS PBAGEBY
NAGRQ GVZR UNEQ GB UNGXR OHG VS LBH PHAG UNGXR ZR NG ZL JBEFG GURA LBAI FHER NF
URYYQBAG QRFRER ZR NG ZL ORFG ZNEVYL ZBABER
"""

# Try all possible shifts
find_correct_shift(ciphertext)
