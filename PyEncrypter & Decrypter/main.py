direction= input("Type 'encode' to encrypt and 'decode' to decrypt: ").strip().lower()


text= input("Enter your message: ").strip()
try:
    shift = int(input("Enter the shift number: "))

except ValueError:
    print("enter an integer to give shift number")
    exit()

def encrypt(text, shift):
    text_list = list(text)

    for n in range(0, len(text_list)):
        ascii_a = ord(text_list[n])
        shifted_ascii = ascii_a + shift
        shifted_char = chr(shifted_ascii)
        text_list[n] = shifted_char

    final_result = ''.join(text_list)
    print("Encrypted text is: " + final_result)
    return final_result
#
def decrypt(text, shift):
    output_list= list(text)
    for n in range(0, len(output_list)):
        ascii_a = ord(output_list[n])
        shifted_ascii = ascii_a - shift
        shifted_char = chr(shifted_ascii)
        output_list[n] = shifted_char
    final_result = ''.join(output_list)
    print("Decrypted text is: " + final_result)
    return final_result

if direction=='encode':
    output = encrypt(text, shift)
    with open("encode.txt", 'w') as file:
        file.write(output+ "\nShift number: "+ str(shift))
elif direction=='decode':
    output=decrypt(text, shift)
    with open("decode.txt", 'w') as file:
        file.write(output+ "\n Shift number: "+str(shift))
else:
    print("Invalid input! enter encode to encrypt and decode to decrypt.")