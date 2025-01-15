def encrypt_text(raw_text, n, m):

    encrypted_chars = []
    classification = []

    for char in raw_text:
        if char.islower():
            if 'a' <= char <= 'm':
                shifted = chr(((ord(char) - ord('a') + n*m) % 26) + ord('a'))
                encrypted_chars.append(shifted)
                classification.append('lower_first')
            else:
                shifted = chr(((ord(char) - ord('a') - (n+m)) % 26) + ord('a'))
                encrypted_chars.append(shifted)
                classification.append('lower_second')
        elif char.isupper():
            if 'A' <= char <= 'M':
                shifted = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
                encrypted_chars.append(shifted)
                classification.append('upper_first')
            else:
                shifted = chr(((ord(char) - ord('A') + m*m) % 26) + ord('A'))
                encrypted_chars.append(shifted)
                classification.append('upper_second')
        else:
            encrypted_chars.append(char)
            classification.append('no_shift')
    return "".join(encrypted_chars), classification

def decrypt_text(encrypted_text, n, m, classification):

    decrypted_chars = []

    for i, char in enumerate(encrypted_text):
        print(i, char)
        rule = classification[i]
        if rule == 'lower_first':
            original = chr(((ord(char) - ord('a') - n*m) % 26) + ord('a'))
            decrypted_chars.append(original)
        elif rule == 'lower_second':
            original = chr(((ord(char) - ord('a') + (n+m)) % 26) + ord('a'))
            decrypted_chars.append(original)
        elif rule == 'upper_first':
            original = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            decrypted_chars.append(original)
        elif rule == 'upper_second':
            original = chr(((ord(char) - ord('A') - m*m) % 26) + ord('A'))
            decrypted_chars.append(original)
        else:
            decrypted_chars.append(char)

    return "".join(decrypted_chars)

def check_decryption(raw_text, decrypted_text):
    return raw_text == decrypted_text

def read_raw_text(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_encrypted_text(filename, encrypted_text):
    with open(filename, 'w') as file:
        file.write(encrypted_text)

def main():
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))
    raw_text = read_raw_text('raw_text.txt')

    encrypted_text, classification = encrypt_text(raw_text, n, m)

    write_encrypted_text('encrypted_text.txt', encrypted_text)

    decrypted_text = decrypt_text(encrypted_text, n, m, classification)

    if check_decryption(raw_text, decrypted_text):
        print("Decryption is successful. The text is correct.")
    else:
        print("Decryption failed. The text is incorrect.")

if __name__ == "__main__":
    print(__name__)
    main()