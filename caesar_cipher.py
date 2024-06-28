def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Shift character within the alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Leave non-alphabet characters unchanged
            result += char

    return result

# User inputs
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Perform encryption or decryption
output = caesar_cipher(text, shift, mode)
print(f"Output: {output}")
