import sys

def shift_char(c, shift):
    if not c.isalpha():
        return c
    
    upper_c = c.upper()
    shifted = chr(((ord(upper_c) - 65 + shift) % 26) + 65)
    
    return shifted if c.isupper() else shifted.lower()

def caesar_cipher(text, shift):
    encoded = ''
    
    for c in text:
        shifted_char = shift_char(c, shift)
        if shifted_char:
            encoded += shifted_char
            
    return encoded

if __name__ == '__main__':
    shift = int(sys.argv[1])
    message = input().strip().replace(' ', '').replace('.', '').replace(',', '')
    
    encoded = caesar_cipher(message, shift)
    
    for i in range(0, len(encoded), 5):
        print(encoded[i:i+5], end=' ')
        if (i+5) % 50 == 0:
            print()
