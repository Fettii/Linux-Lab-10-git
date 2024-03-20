import sys

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char.upper())
            shifted_code = char_code + shift_amount
            if shifted_code > ord('Z'):
                shifted_code -= 26
            result += chr(shifted_code)
    return result

def print_encoded(encoded_text):
    for i in range(0, len(encoded_text), 5):
        print(encoded_text[i:i+5], end=' ')
        if (i // 5 + 1) % 10 == 0:
            print()
    print()

if len(sys.argv) != 2:
    print("Usage: python3 mycipher.py <shift>")
else:
    shift = int(sys.argv[1])
    message = ""
    for line in sys.stdin:
        message += line
    encoded_message = caesar_cipher(message, shift)
    print_encoded(encoded_message)

