# Function to encrypt text
def encrypt_text(text, n, m):
    encrypted_text = ""  # Start with an empty string to store the encrypted result

    # Go through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter (ignores numbers and special characters)
            if char.islower():  # If the character is lowercase
                if char < 'n':  # First half (a-m)
                    shift = n * m  # Shift forward by n * m
                else:  # Second half (n-z)
                    shift = -(n + m)  # Shift backward by n + m
                ascii_base = 97  # ASCII value of 'a'
            else:  # If the character is uppercase
                if char < 'N':  # First half (A-M)
                    shift = -n  # Shift backward by n
                else:  # Second half (N-Z)
                    shift = m ** 2  # Shift forward by m squared
                ascii_base = 65  # ASCII value of 'A'

            # Get the position of the letter in the alphabet (0-25)
            letter_pos = ord(char) - ascii_base

            # Apply the shift and wrap around using modulo 26
            new_pos = (letter_pos + shift) % 26

            # Convert the new position back to a character
            encrypted_text += chr(new_pos + ascii_base)
        else:
            # If it's not a letter, leave it as is
            encrypted_text += char

    return encrypted_text  # Return the final encrypted text

# Function to decrypt text
def decrypt_text(text, n, m):
    decrypted_text = ""  # Start with an empty string to store the decrypted result

    # if there are no values for n and m, set them to 1
    if n == 0 or m == 0:
        n = 1
        m = 1

    # Go through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():  # If the character is lowercase
                if char < 'n':  # First half (a-m)
                    shift = -(n * m)  # Reverse the forward shift
                else:  # Second half (n-z)
                    shift = n + m  # Reverse the backward shift
                ascii_base = 97  # ASCII value of 'a'
            else:  # If the character is uppercase
                if char < 'N':  # First half (A-M)
                    shift = n  # Reverse the backward shift
                else:  # Second half (N-Z)
                    shift = -(m ** 2)  # Reverse the forward shift
                ascii_base = 65  # ASCII value of 'A'

            # Get the position of the letter in the alphabet (0-25)
            letter_pos = ord(char) - ascii_base

            # Apply the reverse shift and wrap around using modulo 26
            new_pos = (letter_pos + shift) % 26

            # Convert the new position back to a character
            decrypted_text += chr(new_pos + ascii_base)
        else:
            # If it's not a letter, leave it as is
            decrypted_text += char

    return decrypted_text  # Return the final decrypted text

# Function to check if decryption works
def verify_decryption(original, decrypted):
    return original == decrypted  # Return True if original matches decrypted

# Main function
def main():
    try:
        # Ask for two inputs from the user
        n = int(input("Enter value for n: "))  # e.g., 2
        m = int(input("Enter value for m: "))  # e.g., 4

        # Open the raw_text.txt file and read its content
        with open("raw_text.txt", "r") as file:
            original_text = file.read()

        # Encrypt the original text
        encrypted_text = encrypt_text(original_text, n, m)

        # Save the encrypted text to a file
        with open("encrypted_text.txt", "w") as file:
            file.write(encrypted_text)

        # Decrypt the text to check if it works
        decrypted_text = decrypt_text(encrypted_text, n, m)

        # Verify if decryption matches the original text
        if verify_decryption(original_text, decrypted_text):
            print("Encryption and decryption were successful!")
            print(f"Encrypted text: {encrypted_text}")
        else:
            print("Decryption failed. The text does not match the original.")

    except FileNotFoundError:
        print("Error: raw_text.txt file not found!")

# Run the program
if __name__ == "__main__":
    decrypt_text()