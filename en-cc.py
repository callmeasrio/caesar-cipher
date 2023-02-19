def caesar_cipher(text):
    shift = 3
    result = ""
    # loop through each character in the text
    for char in text:
        # check if the character is an uppercase letter
        if char.isupper():
            # shift the character by the shift amount and wrap around if necessary
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # check if the character is a lowercase letter
        elif char.islower():
            # shift the character by the shift amount and wrap around if necessary
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # if the character is not a letter, leave it as-is
        else:
            result += char
    
    return result

text = str(input("Enter Your Text: "))
encrypted_text = caesar_cipher(text)
print("Encrypted Text: " + encrypted_text)
