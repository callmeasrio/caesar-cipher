def caesar_cipher_decode(text):
    shift = 3
    result = ""
    # loop through each character in the text
    for char in text:
        # check if the character is an uppercase letter
        if char.isupper():
            # shift the character by the negative shift amount and wrap around if necessary
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # check if the character is a lowercase letter
        elif char.islower():
            # shift the character by the negative shift amount and wrap around if necessary
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # if the character is not a letter, leave it as-is
        else:
            result += char
    
    return result

encrypted_text = str(input("Enter Your Encrypted Text: "))
decrypted_text = caesar_cipher_decode(encrypted_text)
print("Decrypted Text: " + decrypted_text)
