alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar_cypher(original_text, shift_amount, encode_or_decode):
    cypher_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabet:
            message_code = alphabet.index(letter) + shift_amount
            cypher_text += alphabet[message_code % len(alphabet)]
        
        else:
            cypher_text += letter
    
    print(f"HERE IS THE {encode_or_decode.upper()}D RESULT: {cypher_text}\n")


should_continue = True

while should_continue == True:
    direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))

    caesar_cypher(text, shift, direction)

    restart = input("Would you like to encode or decode something else? Type 'yes' or 'no': ").lower()

    if restart != "yes":
        print("Goodbye!")
        should_continue = False
