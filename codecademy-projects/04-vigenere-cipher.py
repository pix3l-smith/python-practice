alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def vigenere_cipher(original_text, keyword, encode_or_decode):
    cypher_text = ""
    key_index = 0

    for letter in original_text:
        if letter in alphabet:
            shift_letter = keyword[key_index % len(keyword)]

            if encode_or_decode == "encode":
                shift_amount = alphabet.index(shift_letter) * -1

            else:
                shift_amount = alphabet.index(shift_letter)

            message_code = alphabet.index(letter) + shift_amount
            cypher_text += alphabet[message_code % len(alphabet)]

            key_index += 1

        else:
            cypher_text += letter

    print(f"HERE IS THE {encode_or_decode.upper()}D RESULT: {cypher_text}\n")


should_continue = True

while should_continue == True:
    direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    key = input("Type the keyword: ")

    vigenere_cipher(text, key, direction)

    restart = input("Would you like to encode or decode something else? Type 'yes' or 'no': ").lower()

    if restart != "yes":
        print("Goodbye!")
        should_continue = False
